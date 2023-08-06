# Copyright 2021 The Cirq Developers
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Client for making requests to SuperstaQ's API."""

import sys
import textwrap
import time
import urllib
from typing import Any, Callable, cast, Dict, List, Optional, Union

import qubovert as qv
import requests

import applications_superstaq


class _SuperstaQClient:
    """Handles calls to SuperstaQ's API.

    Users should not instantiate this themselves,
    but instead should use `$client_superstaq.Service`.
    """

    RETRIABLE_STATUS_CODES = {
        requests.codes.service_unavailable,
    }
    SUPPORTED_TARGETS = {"qpu", "simulator"}
    SUPPORTED_VERSIONS = {
        applications_superstaq.API_VERSION,
    }

    def __init__(
        self,
        remote_host: str,
        api_key: str,
        client_name: str,
        default_target: Optional[str] = None,
        api_version: str = applications_superstaq.API_VERSION,
        max_retry_seconds: float = 3600,  # 1 hour
        verbose: bool = False,
    ):
        """Creates the SuperstaQClient.

        Users should use `$client_superstaq.Service` instead of this class directly.

        The SuperstaQClient handles making requests to the SuperstaQClient,
        returning dictionary results. It handles retry and authentication.

        Args:
            remote_host: The url of the server exposing the SuperstaQ API. This will strip anything
                besides the base scheme and netloc, i.e. it only takes the part of the host of
                the form `http://example.com` of `http://example.com/test`.
            api_key: The key used for authenticating against the SuperstaQ API.
            default_target: The default target to run against. Supports one of 'qpu' and
                'simulator'. Can be overridden by calls with target in their signature.
            api_version: Which version fo the api to use, defaults to client_superstaq.API_VERSION,
                which is the most recent version when this client was downloaded.
            max_retry_seconds: The time to continue retriable responses. Defaults to 3600.
            verbose: Whether to print to stderr and stdio any retriable errors that are encountered.
        """

        self.api_key = api_key
        self.client_name = client_name
        self.api_version = api_version
        self.default_target = default_target
        self.max_retry_seconds = max_retry_seconds
        self.verbose = verbose
        url = urllib.parse.urlparse(remote_host)
        assert url.scheme and url.netloc, (
            f"Specified remote_host {remote_host} is not a valid url, for example "
            "http://example.com"
        )

        assert (
            self.api_version in self.SUPPORTED_VERSIONS
        ), f"Only API versions {self.SUPPORTED_VERSIONS} are accepted but got {self.api_version}"
        assert (
            default_target is None or default_target in self.SUPPORTED_TARGETS
        ), f"Target can only be one of {self.SUPPORTED_TARGETS} but was {default_target}."
        assert max_retry_seconds >= 0, "Negative retry not possible without time machine."

        self.url = f"{url.scheme}://{url.netloc}/{api_version}"
        self.verify_https: bool = f"{applications_superstaq.API_URL}/{self.api_version}" == self.url
        self.headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json",
            "X-Client-Name": self.client_name,
            "X-Client-Version": self.api_version,
        }

    def create_job(
        self,
        serialized_circuits: Dict[str, str],
        repetitions: Optional[int] = None,
        target: Optional[str] = None,
        name: Optional[str] = None,
        ibmq_token: Optional[str] = None,
        ibmq_pulse: Optional[bool] = None,
    ) -> dict:
        """Create a job.

        Args:
            serialized_circuits: The serialized representation of the circuit to run.
            repetitions: The number of times to repeat the circuit. For simulation the repeated
                sampling is not done on the server, but is passed as metadata to be recovered
                from the returned job.
            target: If supplied the target to run on. Supports one of `qpu` or `simulator`. If not
                set, uses `default_target`.
            name: An optional name of the job. Different than the `job_id` of the job.

        Returns:
            The json body of the response as a dict. This does not contain populated information
            about the job, but does contain the job id.

        Raises:
            An SuperstaQException if the request fails.
        """
        actual_target = self._target(target)
        json_dict: Dict[str, Any] = {
            **serialized_circuits,
            "backend": actual_target,
            "shots": repetitions,
        }
        if ibmq_token:
            json_dict["ibmq_token"] = ibmq_token

        if ibmq_pulse:
            json_dict["ibmq_pulse"] = ibmq_pulse

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/jobs",
                json=json_dict,
                headers=self.headers,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def get_job(self, job_id: str) -> dict:
        """Get the job from the SuperstaQ API.

        Args:
            job_id: The UUID of the job (returned when the job was created).

        Returns:
            The json body of the response as a dict.

        Raises:
            SuperstaQNotFoundException: If a job with the given job_id does not exist.
            SuperstaQException: For other API call failures.
        """

        def request() -> requests.Response:
            return requests.get(
                f"{self.url}/job/{job_id}",
                headers=self.headers,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def get_balance(self) -> dict:
        """Get the querying user's account balance in USD.

        Returns:
            The json body of the response as a dict.
        """

        def request() -> requests.Response:
            return requests.get(
                f"{self.url}/balance",
                headers=self.headers,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def get_backends(self) -> dict:
        """Makes a GET request to SuperstaQ API to get a list of available backends."""

        def request() -> requests.Response:
            return requests.get(
                f"{self.url}/backends",
                headers=self.headers,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def ibmq_set_token(self, ibmq_token: Dict[str, str]) -> dict:
        """Makes a POST request to SuperstaQ API to set IBMQ token field in database.

        Args:
            ibmq_token: dictionary with IBMQ token string entry.

        Returns:
            The json body of the response as a dict.
        """

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/ibmq_token",
                headers=self.headers,
                json=ibmq_token,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def aqt_compile(self, json_dict: Dict[str, Union[str, List[str]]]) -> dict:
        """Makes a POST request to SuperstaQ API to compile a list of circuits for Berkeley-AQT."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/aqt_compile",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def qscout_compile(self, json_dict: Dict[str, Union[str, List[str]]]) -> dict:
        """Makes a POST request to SuperstaQ API to compile a list of circuits for Berkeley-AQT."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/qscout_compile",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def ibmq_compile(self, json_dict: Dict[str, Union[str, List[str]]]) -> dict:
        """Makes a POST request to SuperstaQ API to compile a circuits for IBM devices."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/ibmq_compile",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def neutral_atom_compile(self, json_dict: Dict[str, Union[str, List[str]]]) -> dict:
        """Makes a POST request to SuperstaQ API to compile a circuits for neutral atom devices."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/neutral_atom_compile",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def submit_qubo(self, qubo: qv.QUBO, target: str, repetitions: int = 1000) -> dict:
        """Makes a POST request to SuperstaQ API to submit a QUBO problem to the given target."""
        json_dict = {
            "qubo": applications_superstaq.qubo.convert_qubo_to_model(qubo),
            "backend": target,
            "shots": repetitions,
        }

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/qubo",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def find_min_vol_portfolio(self, json_dict: dict) -> dict:
        """Makes a POST request to SuperstaQ API to find a minimum volatility portfolio
        that exceeds a certain specified return."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/minvol",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def find_max_pseudo_sharpe_ratio(self, json_dict: dict) -> dict:
        """Makes a POST request to SuperstaQ API to find a max Sharpe ratio portfolio."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/maxsharpe",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def tsp(self, json_dict: dict) -> dict:
        """Makes a POST request to SuperstaQ API to find a optimal TSP tour."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/tsp",
                headers=self.headers,
                json=json_dict,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def warehouse(self, json_dict: dict) -> dict:
        """Makes a POST request to SuperstaQ API to find optimal warehouse assignment."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/warehouse",
                headers=self.headers,
                json=json_dict,
            )

        return self._make_request(request).json()

    def aqt_upload_configs(self, aqt_configs: Dict[str, str]) -> dict:
        """Makes a POST request to SuperstaQ API to upload configurations."""

        def request() -> requests.Response:
            return requests.post(
                f"{self.url}/aqt_configs",
                headers=self.headers,
                json=aqt_configs,
                verify=self.verify_https,
            )

        return self._make_request(request).json()

    def _target(self, target: Optional[str]) -> str:
        """Returns the target if not None or the default target.

        Raises:
            AssertionError: if both `target` and `default_target` are not set.
        """
        assert target is not None or self.default_target is not None, (
            "One must specify a target on this call, or a default_target on the service/client, "
            "but neither were set."
        )
        return cast(str, target or self.default_target)

    def _handle_status_codes(self, response: requests.Response) -> None:
        if response.status_code == requests.codes.unauthorized:
            raise applications_superstaq.SuperstaQException(
                '"Not authorized" returned by SuperstaQ API.  '
                "Check to ensure you have supplied the correct API key.",
                response.status_code,
            )
        if response.status_code == requests.codes.not_found:
            raise applications_superstaq.SuperstaQNotFoundException(
                "SuperstaQ could not find requested resource."
            )

        if response.status_code not in self.RETRIABLE_STATUS_CODES:
            message = response.reason
            if response.status_code == 400:
                message = str(response.text)
            raise applications_superstaq.SuperstaQException(
                "Non-retriable error making request to SuperstaQ API. "
                f"Status: {response.status_code} "
                f"Error : {message}",
                response.status_code,
            )

    def _make_request(self, request: Callable[[], requests.Response]) -> requests.Response:
        """Make a request to the API, retrying if necessary.

        Args:
            request: A function that returns a `requests.Response`.

        Raises:
            SuperstaQException: If there was a not-retriable error from the API.
            TimeoutError: If the requests retried for more than `max_retry_seconds`.

        Returns:
            The request.Response from the final successful request call.
        """
        # Initial backoff of 100ms.
        delay_seconds = 0.1
        while True:
            try:
                response = request()
                if response.ok:
                    return response

                self._handle_status_codes(response)
                message = response.reason

            # Fallthrough should retry.
            except requests.RequestException as e:
                # Connection error, timeout at server, or too many redirects.
                # Retry these.
                message = f"RequestException of type {type(e)}."
            if delay_seconds > self.max_retry_seconds:
                raise TimeoutError(f"Reached maximum number of retries. Last error: {message}")
            if self.verbose:
                print(message, file=sys.stderr)
                print(f"Waiting {delay_seconds} seconds before retrying.")
            time.sleep(delay_seconds)
            delay_seconds *= 2

    def __str__(self) -> str:
        return f"Client with host={self.url} and name={self.client_name}"

    def __repr__(self) -> str:
        return textwrap.dedent(
            f"""\
            applications_superstaq.superstaq_client._SuperstaQClient(
                remote_host={self.url!r},
                api_key={self.api_key!r},
                client_name={self.client_name!r},
                default_target={self.default_target!r},
                api_version={self.api_version!r},
                max_retry_seconds={self.max_retry_seconds!r},
                verbose={self.verbose!r},
            )"""
        )
