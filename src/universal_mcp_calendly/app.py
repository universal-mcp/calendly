from typing import Any

from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration


class CalendlyApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        """
        Initializes a new instance of the Calendly API application with the specified integration and additional configuration options.

        Args:
            integration: An optional Integration object to associate with the Calendly API application. Defaults to None.
            **kwargs: Arbitrary keyword arguments that are passed to the superclass initializer for additional configuration.

        Returns:
            None
        """
        super().__init__(name="calendly", integration=integration, **kwargs)
        self.base_url = "https://api.calendly.com"

    def list_event_invitees(
        self, uuid, status=None, sort=None, email=None, page_token=None, count=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of invitees for a specific scheduled event with optional filtering and pagination support.
        
        Args:
            uuid: str. The unique identifier of the scheduled event (required).
            status: Optional[str]. Filter invitees by invitation status (e.g., 'accepted', 'declined', 'pending').
            sort: Optional[str]. Sorting order for results (e.g., 'name_asc', 'date_desc').
            email: Optional[str]. Filter invitees by email address.
            page_token: Optional[str]. Pagination token for retrieving specific results page.
            count: Optional[int]. Maximum number of invitees to return per page.
        
        Returns:
            dict[str, Any]. Contains list of invitees and pagination details, structured as {'invitees': [...], 'pagination': {...}}.
        
        Raises:
            ValueError: Raised when 'uuid' parameter is not provided.
            HTTPError: Raised for failed API requests (4XX/5XX status codes).
        
        Tags:
            fetch, list, pagination, filtering, invitee-management, api-client, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/scheduled_events/{uuid}/invitees"
        query_params = {
            k: v
            for k, v in [
                ("status", status),
                ("sort", sort),
                ("email", email),
                ("page_token", page_token),
                ("count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details of a scheduled event using its unique identifier.
        
        Args:
            uuid: str. The unique identifier of the scheduled event to retrieve.
        
        Returns:
            dict[str, Any]: A dictionary containing the scheduled event details, including all fields returned by the API.
        
        Raises:
            ValueError: Raised if the 'uuid' parameter is None.
            HTTPError: Raised if the API request fails (e.g., invalid UUID, network error, or server issue).
        
        Tags:
            scheduled-events, retrieve, api, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/scheduled_events/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_invitee(self, event_uuid, invitee_uuid) -> dict[str, Any]:
        """
        Retrieves details about a specific invitee for a given scheduled event.
        
        Args:
            event_uuid: The unique identifier of the scheduled event.
            invitee_uuid: The unique identifier of the invitee to retrieve.
        
        Returns:
            A dictionary containing invitee details as returned by the API.
        
        Raises:
            ValueError: Raised when either 'event_uuid' or 'invitee_uuid' is missing.
        
        Tags:
            fetch, event-management, invitee, important
        """
        if event_uuid is None:
            raise ValueError("Missing required parameter 'event_uuid'")
        if invitee_uuid is None:
            raise ValueError("Missing required parameter 'invitee_uuid'")
        url = f"{self.base_url}/scheduled_events/{event_uuid}/invitees/{invitee_uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_events(
        self,
        user=None,
        organization=None,
        invitee_email=None,
        status=None,
        sort=None,
        min_start_time=None,
        max_start_time=None,
        page_token=None,
        count=None,
        group=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of scheduled events based on specified filters such as user, organization, invitee email, status, date range, sorting, and pagination criteria.
        
        Args:
            user: Optional user identifier to filter events by a specific user.
            organization: Optional organization identifier to filter events by a specific organization.
            invitee_email: Optional email address of the invitee to filter events.
            status: Optional status to filter events (e.g., 'scheduled', 'cancelled').
            sort: Optional sorting criteria for the events (e.g., by start time).
            min_start_time: Minimum start time (ISO 8601 format) to filter events.
            max_start_time: Maximum start time (ISO 8601 format) to filter events.
            page_token: Token for fetching the next page of results.
            count: Optional maximum number of events to return.
            group: Optional group identifier to filter events by group.
        
        Returns:
            A dictionary containing the list of scheduled events and associated metadata.
        
        Raises:
            HTTPError: When the server returns a status code indicating an HTTP error (e.g., 404, 500).
        
        Tags:
            list, filter, events, pagination, important
        """
        url = f"{self.base_url}/scheduled_events"
        query_params = {
            k: v
            for k, v in [
                ("user", user),
                ("organization", organization),
                ("invitee_email", invitee_email),
                ("status", status),
                ("sort", sort),
                ("min_start_time", min_start_time),
                ("max_start_time", max_start_time),
                ("page_token", page_token),
                ("count", count),
                ("group", group),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_type(self, uuid) -> dict[str, Any]:
        """
        Retrieves the event type details for the specified UUID from the API.
        
        Args:
            uuid: The unique identifier of the event type to retrieve.
        
        Returns:
            A dictionary containing the event type details as returned by the API.
        
        Raises:
            ValueError: Raised when the 'uuid' parameter is missing or None.
            requests.exceptions.HTTPError: Raised if the HTTP request encounters an error status.
        
        Tags:
            retrieve, event-type, api-call, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/event_types/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_sevent_types(
        self,
        active=None,
        organization=None,
        user=None,
        user_availability_schedule=None,
        sort=None,
        admin_managed=None,
        page_token=None,
        count=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of user event types with optional filtering, sorting, and pagination parameters.
        
        Args:
            active: Optional; filters event types by active status (bool or compatible)
            organization: Optional; filters by organization identifier (string)
            user: Optional; filters by user identifier (string)
            user_availability_schedule: Optional; filters by availability schedule ID (string)
            sort: Optional; comma-separated string or list for sorting results (string or list)
            admin_managed: Optional; filters admin-managed event types (bool or compatible)
            page_token: Optional; pagination token for subsequent pages (string)
            count: Optional; maximum number of results to return (integer)
        
        Returns:
            Dictionary containing the event types list and pagination metadata (dict[str, Any])
        
        Raises:
            HTTPStatusError: Raised when the API request fails (4xx/5xx status codes)
        
        Tags:
            list, filter, pagination, user-events, api, important
        """
        url = f"{self.base_url}/event_types"
        query_params = {
            k: v
            for k, v in [
                ("active", active),
                ("organization", organization),
                ("user", user),
                ("user_availability_schedule", user_availability_schedule),
                ("sort", sort),
                ("admin_managed", admin_managed),
                ("page_token", page_token),
                ("count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user(self, uuid) -> dict[str, Any]:
        """
        Retrieves detailed user information for a specified UUID from a remote API.
        
        Args:
            uuid: The unique identifier (UUID) of the user to retrieve, in string format.
        
        Returns:
            Dictionary containing the user's details (e.g., name, email, permissions) as returned by the API.
        
        Raises:
            ValueError: Raised when the required 'uuid' parameter is None.
            requests.exceptions.HTTPError: Raised if the API request fails (e.g., 404 for missing user or 500 server errors).
        
        Tags:
            user-management, api-client, fetch, data-retrieval, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/users/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_current_user(
        self,
    ) -> dict[str, Any]:
        """
        Retrieves information about the currently authenticated user from the API.
        
        Returns:
            Dictionary containing the current user's information (user metadata, credentials, or permissions) as returned by the API.
        
        Raises:
            requests.HTTPError: Raised when the API request fails (e.g., authentication failure, network issues, or server errors).
        
        Tags:
            fetch, user-info, authentication, api, important
        """
        url = f"{self.base_url}/users/me"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_invitations(
        self, uuid, count=None, page_token=None, sort=None, email=None, status=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of invitations for a specified organization with optional filtering, sorting, and pagination.
        
        Args:
            uuid: Unique identifier of the organization whose invitations are to be listed (required).
            count: Optional[int]: Maximum number of invitations to return per page.
            page_token: Optional[str]: Token indicating the page of results to retrieve.
            sort: Optional[str]: Sorting criteria for invitations (e.g., 'created_at:desc', 'status:asc').
            email: Optional[str]: Filter invitations sent to a specific email address.
            status: Optional[str]: Filter invitations by status (e.g., 'pending', 'accepted', 'expired').
        
        Returns:
            dict[str, Any]: A dictionary containing 'invitations' (list of invitation objects) and pagination metadata (e.g., 'next_page_token').
        
        Raises:
            ValueError: Raised if 'uuid' parameter is None or invalid.
            HTTPError: Raised for HTTP request failures from the API endpoint.
        
        Tags:
            list, organizations, invitations, pagination, filter, api, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organizations/{uuid}/invitations"
        query_params = {
            k: v
            for k, v in [
                ("count", count),
                ("page_token", page_token),
                ("sort", sort),
                ("email", email),
                ("status", status),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def invite_user_to_organization(self, uuid, email=None) -> dict[str, Any]:
        """
        Sends an invitation to a specified email address to join an organization identified by its UUID.
        
        Args:
            uuid: The unique identifier of the organization to which the user is being invited.
            email: Optional email address of the user to invite. If None, the invite is created without an email.
        
        Returns:
            A dictionary containing the JSON response from the API after sending the invitation.
        
        Raises:
            ValueError: Raised when the required parameter 'uuid' is missing.
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            invite, organization, management, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizations/{uuid}/invitations"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_invitation(self, org_uuid, uuid) -> dict[str, Any]:
        """
        Retrieves a specific invitation for an organization using its unique identifiers.
        
        Args:
            org_uuid: The unique identifier of the organization whose invitation is to be retrieved.
            uuid: The unique identifier of the invitation to fetch.
        
        Returns:
            A dictionary containing the invitation details as returned by the API.
        
        Raises:
            ValueError: Raised if either 'org_uuid' or 'uuid' is missing.
        
        Tags:
            retrieve, organizational, invitation, important
        """
        if org_uuid is None:
            raise ValueError("Missing required parameter 'org_uuid'")
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organizations/{org_uuid}/invitations/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def revoke_user_sorganization_invitation(self, org_uuid, uuid) -> Any:
        """
        Revokes a user's invitation to an organization by deleting the specified invitation resource.
        
        Args:
            org_uuid: The unique identifier of the organization from which the user's invitation will be revoked.
            uuid: The unique identifier of the invitation to be revoked.
        
        Returns:
            The JSON response from the API after successfully revoking the invitation.
        
        Raises:
            ValueError: Raised if either 'org_uuid' or 'uuid' parameter is missing.
            requests.RequestException: Occurs if the API request fails (e.g., network issues, server errors).
        
        Tags:
            revoke, organization, invitation, important
        """
        if org_uuid is None:
            raise ValueError("Missing required parameter 'org_uuid'")
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organizations/{org_uuid}/invitations/{uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_membership(self, uuid) -> dict[str, Any]:
        """
        Retrieves the membership information for a specified organization membership UUID.
        
        Args:
            uuid: str. The unique identifier of the organization membership to retrieve.
        
        Returns:
            dict. A dictionary containing the organization membership details as returned by the API.
        
        Raises:
            ValueError: Raised when the required 'uuid' parameter is missing.
        
        Tags:
            get, membership, organization, api_call, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organization_memberships/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_user_from_organization(self, uuid) -> Any:
        """
        Removes a user from the organization by deleting their membership using the specified UUID
        
        Args:
            uuid: The unique identifier of the organization membership to remove
        
        Returns:
            The response data from the organization membership removal request
        
        Raises:
            ValueError: Raised when the required parameter 'uuid' is missing
        
        Tags:
            remove, organization, management, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organization_memberships/{uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_memberships(
        self, page_token=None, count=None, email=None, organization=None, user=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of organization memberships with optional filtering by pagination, email, organization, or user parameters.
        
        Args:
            page_token: Optional; A string token to specify the page of results to retrieve for pagination.
            count: Optional; An integer specifying the maximum number of memberships to return.
            email: Optional; A string to filter memberships by user email address.
            organization: Optional; A string to filter memberships by organization identifier.
            user: Optional; A string to filter memberships by user identifier.
        
        Returns:
            A dictionary containing the organization membership data returned by the API.
        
        Raises:
            HTTPError: Raised if the HTTP request does not return a successful status code.
        
        Tags:
            list, organization, membership, api, important
        """
        url = f"{self.base_url}/organization_memberships"
        query_params = {
            k: v
            for k, v in [
                ("page_token", page_token),
                ("count", count),
                ("email", email),
                ("organization", organization),
                ("user", user),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_subscription(self, webhook_uuid) -> dict[str, Any]:
        """
        Retrieves the details of a webhook subscription identified by its UUID.
        
        Args:
            webhook_uuid: The unique identifier (UUID) of the webhook subscription to retrieve.
        
        Returns:
            A dictionary containing the webhook subscription details as returned by the API.
        
        Raises:
            ValueError: Raised when the 'webhook_uuid' parameter is missing.
        
        Tags:
            fetch, webhook, management, important
        """
        if webhook_uuid is None:
            raise ValueError("Missing required parameter 'webhook_uuid'")
        url = f"{self.base_url}/webhook_subscriptions/{webhook_uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook_subscription(self, webhook_uuid) -> Any:
        """
        Deletes a webhook subscription identified by its UUID from the server using the provided UUID.
        
        Args:
            webhook_uuid: The unique identifier (UUID) of the webhook subscription to delete.
        
        Returns:
            JSON-decoded response from the server after successful deletion.
        
        Raises:
            ValueError: Raised when the 'webhook_uuid' parameter is None.
            HTTPError: Raised when the server response contains an unsuccessful status code (4XX/5XX).
        
        Tags:
            delete, webhook, subscription, async, http, management, important
        """
        if webhook_uuid is None:
            raise ValueError("Missing required parameter 'webhook_uuid'")
        url = f"{self.base_url}/webhook_subscriptions/{webhook_uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_webhook_subscriptions(
        self,
        organization=None,
        user=None,
        page_token=None,
        count=None,
        sort=None,
        scope=None,
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of webhook subscriptions with optional filtering parameters.
        
        Args:
            organization: Optional organization identifier to filter subscriptions by organization (str or None).
            user: Optional user identifier to filter subscriptions created by a specific user (str or None).
            page_token: Optional pagination token to retrieve a specific page of results (str or None).
            count: Optional maximum number of subscriptions to return per response (int or None).
            sort: Optional sorting order for returned subscriptions (str or None).
            scope: Optional scope identifier to filter webhook subscriptions (str or None).
        
        Returns:
            Dictionary containing webhook subscription entries and associated metadata (e.g., paging information).
        
        Raises:
            HTTPError: When the API request fails, typically due to invalid parameters or server-side errors.
        
        Tags:
            list, webhooks, pagination, filter, management, important
        """
        url = f"{self.base_url}/webhook_subscriptions"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("user", user),
                ("page_token", page_token),
                ("count", count),
                ("sort", sort),
                ("scope", scope),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook_subscription(
        self,
        events=None,
        group=None,
        organization=None,
        scope=None,
        signing_key=None,
        url=None,
        user=None,
    ) -> dict[str, Any]:
        """
        Creates a new webhook subscription with customizable parameters and returns its configuration details.
        
        Args:
            events: List of event names that trigger the webhook notification.
            group: Group identifier for webhook scope.
            organization: Organization identifier associated with the subscription.
            scope: Authorization scope for webhook activation.
            signing_key: Cryptographic key for payload verification.
            url: Endpoint URL for webhook event delivery.
            user: User identifier linked to the subscription.
        
        Returns:
            Dictionary containing full webhook subscription details including generated IDs and timestamps.
        
        Raises:
            HTTPError: When the API request fails due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            webhook, subscription, create, async-job, api, important
        """
        request_body = {
            "events": events,
            "group": group,
            "organization": organization,
            "scope": scope,
            "signing_key": signing_key,
            "url": url,
            "user": user,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhook_subscriptions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_single_use_scheduling_link(
        self, max_event_count=None, owner=None, owner_type=None
    ) -> dict[str, Any]:
        """
        Creates a single-use scheduling link by sending a POST request with optional restrictions.
        
        Args:
            max_event_count: Optional; int or None. The maximum number of events that can be scheduled using the link.
            owner: Optional; str or None. The identifier for the owner of the scheduling link.
            owner_type: Optional; str or None. The type of the owner (e.g., 'user', 'team').
        
        Returns:
            dict[str, Any]: The response data from the scheduling link creation API as a dictionary.
        
        Raises:
            requests.RequestException: Raised when there's a network problem (e.g., DNS resolution, refused connection).
        
        Tags:
            create, scheduling, important
        """
        request_body = {
            "max_event_count": max_event_count,
            "owner": owner,
            "owner_type": owner_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/scheduling_links"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_invitee_data(self, emails=None) -> dict[str, Any]:
        """
        Deletes invitee data for specified email addresses by sending a POST request to the data compliance API.
        
        Args:
            emails: Optional list of email addresses (list[str] or None) to identify the invitees whose data should be deleted. If None, no emails are included in the request.
        
        Returns:
            A dictionary containing the JSON response from the API indicating the result of the deletion request.
        
        Raises:
            requests.exceptions.HTTPError: Raised if an HTTP request returns an unsuccessful status code, indicating a problem with the request or server response.
        
        Tags:
            delete, compliance, api-call, important
        """
        request_body = {
            "emails": emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/data_compliance/deletion/invitees"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_event_data(
        self, end_time=None, start_time=None
    ) -> dict[str, Any]:
        """
        Deletes scheduled event data within the specified time range by sending a deletion request to the data compliance service.
        
        Args:
            end_time: Optional; The end of the time interval for which scheduled event data should be deleted. If None, no upper bound is set.
            start_time: Optional; The start of the time interval for which scheduled event data should be deleted. If None, no lower bound is set.
        
        Returns:
            A dictionary containing the response from the data compliance deletion endpoint.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request encounters an error, such as a 4xx or 5xx status code.
        
        Tags:
            delete, data_compliance, important, management
        """
        request_body = {
            "end_time": end_time,
            "start_time": start_time,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/data_compliance/deletion/events"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_invitee_no_show(self, uuid) -> dict[str, Any]:
        """
        Retrieves details about an invitee who did not show up for a scheduled event, identified by a unique UUID.
        
        Args:
            uuid: The unique identifier (UUID) of the invitee no-show to retrieve.
        
        Returns:
            A dictionary containing details of the invitee no-show record, including invitee information and event metadata.
        
        Raises:
            ValueError: Raised when the 'uuid' parameter is None, indicating a missing required identifier.
            HTTPError: Raised when the API request fails, typically due to invalid UUID formats, non-existent records, or server errors.
        
        Tags:
            retrieve, no-show, invitee, scheduling, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/invitee_no_shows/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_invitee_no_show(self, uuid) -> Any:
        """
        Deletes an invitee no-show record identified by the given UUID.
        
        Args:
            uuid: The unique identifier (UUID) of the invitee no-show to delete. Must not be None.
        
        Returns:
            The response data as a JSON object after successfully deleting the invitee no-show record.
        
        Raises:
            ValueError: Raised when the required parameter 'uuid' is missing (i.e., None).
            requests.HTTPError: Raised by the response.raise_for_status() call if the HTTP request was unsuccessful.
        
        Tags:
            delete, management, important, uuid-based
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/invitee_no_shows/{uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_invitee_no_show(self, invitee=None) -> dict[str, Any]:
        """
        Creates an invitee no-show record via POST request to the invitee_no_shows endpoint.
        
        Args:
            invitee: Optional; information about the invitee included in the request body. Omitted if None.
        
        Returns:
            Dictionary containing the server's JSON response data from the creation request.
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP request failures (e.g., 4XX/5XX status codes).
            requests.exceptions.RequestException: Raised for connection errors or timeout issues.
        
        Tags:
            create, post-request, no-show, management, important
        """
        request_body = {
            "invitee": invitee,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/invitee_no_shows"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_group(self, uuid) -> dict[str, Any]:
        """
        Retrieves a group's details from the server by its UUID.
        
        Args:
            uuid: The unique identifier (UUID) of the group to retrieve.
        
        Returns:
            A dictionary containing the group's details as returned by the server.
        
        Raises:
            ValueError: Raised when the 'uuid' parameter is None.
            requests.HTTPError: Raised when the server response contains an HTTP error status code.
        
        Tags:
            retrieve, group, server, http, management, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/groups/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_groups(
        self, organization=None, page_token=None, count=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of groups from the API, optionally filtered by organization.
        
        Args:
            organization: Optional organization filter (string) to narrow results
            page_token: Optional pagination token (string) for requesting specific results pages
            count: Optional maximum number of groups (integer) to return per page
        
        Returns:
            Dictionary containing API response with groups list and pagination details
        
        Raises:
            HTTPError: On unsuccessful API request status codes (4xx/5xx)
        
        Tags:
            list, paginated, api-client, management, important
        """
        url = f"{self.base_url}/groups"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("page_token", page_token),
                ("count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_group_relationship(self, uuid) -> dict[str, Any]:
        """
        Retrieves the relationship information for a group by UUID from the API.
        
        Args:
            uuid: The unique identifier (UUID) of the group whose relationship data is to be retrieved.
        
        Returns:
            A dictionary containing the group relationship information as returned by the API.
        
        Raises:
            ValueError: Raised when the required parameter 'uuid' is not provided.
            requests.exceptions.HTTPError: Raised when the API request fails (non-2xx status code).
        
        Tags:
            retrieve, group, api, relationship, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/group_relationships/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_group_relationships(
        self, count=None, page_token=None, organization=None, owner=None, group=None
    ) -> dict[str, Any]:
        """
        Retrieves paginated group relationships from the server with optional filtering parameters.
        
        Args:
            count: Maximum number of records to retrieve (used for pagination).
            page_token: Token indicating the page of results to retrieve.
            organization: Filter relationships by a specific organization identifier.
            owner: Filter relationships by an owner identifier.
            group: Filter relationships by a group identifier.
        
        Returns:
            Dictionary containing the server's JSON response, including metadata and group relationship records.
        
        Raises:
            requests.HTTPError: Raised when the server returns a non-200 status code during the API request.
        
        Tags:
            list, retrieve, pagination, filter, api, important
        """
        url = f"{self.base_url}/group_relationships"
        query_params = {
            k: v
            for k, v in [
                ("count", count),
                ("page_token", page_token),
                ("organization", organization),
                ("owner", owner),
                ("group", group),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_routing_form(self, uuid) -> dict[str, Any]:
        """
        Retrieves a specific routing form by its unique identifier from the server.
        
        Args:
            uuid: The unique identifier (UUID) of the routing form to fetch.
        
        Returns:
            A dictionary containing the full routing form data structure as returned by the server.
        
        Raises:
            ValueError: If the 'uuid' parameter is None or empty.
            HTTPError: If the server request fails due to network issues, invalid authentication, or a non-existent UUID.
        
        Tags:
            fetch, routing-form, management, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/routing_forms/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_routing_forms(
        self, organization=None, count=None, page_token=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a paginated list of routing forms from the API with optional filtering, sorting, and pagination.
        
        Args:
            organization: Optional[str]. Organization identifier to filter routing forms. None disables organization filtering.
            count: Optional[int]. Maximum number of routing forms to return. None uses default API pagination size.
            page_token: Optional[str]. Pagination token for specific result pages. None retrieves the first page.
            sort: Optional[str]. Sorting criteria for results. None uses API default sorting.
        
        Returns:
            dict[str, Any]: API response dictionary containing routing form list and pagination metadata.
        
        Raises:
            HTTPError: If the API request fails due to network issues, authentication errors, or invalid parameters.
        
        Tags:
            list, api, pagination, routing-forms, management, important
        """
        url = f"{self.base_url}/routing_forms"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("count", count),
                ("page_token", page_token),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_routing_form_submission(self, uuid) -> dict[str, Any]:
        """
        Retrieves a routing form submission by its unique identifier (UUID) from the configured API endpoint.
        
        Args:
            uuid: The unique identifier of the routing form submission to retrieve. Must not be None.
        
        Returns:
            A dictionary containing the routing form submission data retrieved from the API.
        
        Raises:
            ValueError: Raised when the 'uuid' parameter is missing or None.
        
        Tags:
            retrieve, api, routing, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/routing_form_submissions/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_routing_form_submissions(
        self, form=None, count=None, page_token=None, sort=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of routing form submissions with optional filtering and pagination.
        
        Args:
            form: Optional; the identifier of the form to filter submissions by.
            count: Optional; the maximum number of submissions to return.
            page_token: Optional; token for pagination to retrieve the next set of results.
            sort: Optional; sorting preference for the submissions.
        
        Returns:
            A dictionary containing the retrieved routing form submissions and related metadata.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            list, retrieve, important, management
        """
        url = f"{self.base_url}/routing_form_submissions"
        query_params = {
            k: v
            for k, v in [
                ("form", form),
                ("count", count),
                ("page_token", page_token),
                ("sort", sort),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_type_available_times(
        self, event_type=None, start_time=None, end_time=None
    ) -> dict[str, Any]:
        """
        Retrieves available scheduling times for specified event types within an optional datetime range.
        
        Args:
            event_type: Optional event type filter (returns times for all types if None)
            start_time: Earliest inclusive datetime (string/datetime format) for results
            end_time: Latest inclusive datetime (string/datetime format) for results
        
        Returns:
            Dictionary containing API response data with available time slots
        
        Raises:
            HTTPError: If the API request returns a 4XX/5XX status code (via response.raise_for_status())
        
        Tags:
            list, query, times, scheduling, api, important
        """
        url = f"{self.base_url}/event_type_available_times"
        query_params = {
            k: v
            for k, v in [
                ("event_type", event_type),
                ("start_time", start_time),
                ("end_time", end_time),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_activity_log_entries(
        self,
        organization=None,
        search_term=None,
        actor=None,
        sort=None,
        min_occurred_at=None,
        max_occurred_at=None,
        page_token=None,
        count=None,
        namespace=None,
        action=None,
    ) -> dict[str, Any]:
        """
        Retrieves a list of activity log entries with optional filtering, sorting, and pagination.
        
        Args:
            organization: Optional; organization identifier to filter log entries by a specific organization.
            search_term: Optional; term to search for in the activity log entries.
            actor: Optional; filter results by the user or entity that performed the action.
            sort: Optional; sorting order for the results (e.g., ascending or descending by a field).
            min_occurred_at: Optional; ISO 8601 timestamp to filter entries that occurred after this date and time.
            max_occurred_at: Optional; ISO 8601 timestamp to filter entries that occurred before this date and time.
            page_token: Optional; token for paginating through large result sets.
            count: Optional; maximum number of entries to return.
            namespace: Optional; filter results by a specific namespace.
            action: Optional; filter results by a specific action performed.
        
        Returns:
            A dictionary containing a list of activity log entries and any associated pagination metadata.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an unexpected status code or connection issue.
        
        Tags:
            list, activity-log, async-job, important
        """
        url = f"{self.base_url}/activity_log_entries"
        query_params = {
            k: v
            for k, v in [
                ("organization", organization),
                ("search_term", search_term),
                ("actor", actor),
                ("sort", sort),
                ("min_occurred_at", min_occurred_at),
                ("max_occurred_at", max_occurred_at),
                ("page_token", page_token),
                ("count", count),
                ("namespace", namespace),
                ("action", action),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_share(
        self,
        availability_rule=None,
        duration=None,
        end_date=None,
        event_type=None,
        hide_location=None,
        location_configurations=None,
        max_booking_time=None,
        name=None,
        period_type=None,
        start_date=None,
    ) -> dict[str, Any]:
        """
        Creates a new share with specified configuration by sending a POST request to the shares API endpoint.
        
        Args:
            availability_rule: Optional; rule defining the availability schedule for the share
            duration: Optional; duration of the share in minutes
            end_date: Optional; end date for the share's availability period
            event_type: Optional; type of event associated with the share
            hide_location: Optional; whether to hide location details in the share
            location_configurations: Optional; configuration details for associated physical/virtual locations
            max_booking_time: Optional; maximum allowed booking time in minutes
            name: Optional; display name for the share
            period_type: Optional; temporal pattern type (e.g., recurring, single occurrence)
            start_date: Optional; start date for the share's availability period
        
        Returns:
            Dictionary containing created share details from API response, including IDs and configuration parameters
        
        Raises:
            requests.exceptions.HTTPError: Raised for unsuccessful API responses (4XX/5XX status codes)
        
        Tags:
            create, api-client, post-request, configuration-management, important
        """
        request_body = {
            "availability_rule": availability_rule,
            "duration": duration,
            "end_date": end_date,
            "event_type": event_type,
            "hide_location": hide_location,
            "location_configurations": location_configurations,
            "max_booking_time": max_booking_time,
            "name": name,
            "period_type": period_type,
            "start_date": start_date,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/shares"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_busy_times(
        self, user=None, start_time=None, end_time=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of busy time intervals for specified users within an optional date range.
        
        Args:
            user: Optional user identifier (None returns busy times for all users).
            start_time: Optional ISO 8601 timestamp for filtering busy times starting on/after this time (None disables lower bound).
            end_time: Optional ISO 8601 timestamp for filtering busy times ending before/on this time (None disables upper bound).
        
        Returns:
            Dictionary containing busy time intervals and metadata from the API response.
        
        Raises:
            HTTPError: If the API request fails due to network issues, invalid parameters, or server errors.
        
        Tags:
            busy-times, retrieve, time-management, api-integration, important
        """
        url = f"{self.base_url}/user_busy_times"
        query_params = {
            k: v
            for k, v in [
                ("user", user),
                ("start_time", start_time),
                ("end_time", end_time),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user_availability_schedule(self, uuid) -> dict[str, Any]:
        """
        Retrieves the availability schedule for a user identified by the given UUID.
        
        Args:
            uuid: The UUID of the user whose availability schedule is to be retrieved.
        
        Returns:
            A dictionary containing the user's availability schedule as returned by the API.
        
        Raises:
            ValueError: Raised when the required 'uuid' parameter is missing.
        
        Tags:
            search, management, important
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/user_availability_schedules/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_availability_schedules(self, user=None) -> dict[str, Any]:
        """
        Retrieves user availability schedules from the API, optionally filtered by a specific user identifier.
        
        Args:
            user: Optional string representing the user identifier to filter schedules. If None, returns schedules for all users.
        
        Returns:
            Dictionary containing availability schedules data returned by the API.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (e.g., 4XX/5XX status codes).
        
        Tags:
            retrieve, list, user, availability, async-job, important
        """
        url = f"{self.base_url}/user_availability_schedules"
        query_params = {k: v for k, v in [("user", user)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_type_hosts(
        self, event_type=None, count=None, page_token=None
    ) -> dict[str, Any]:
        """
        Retrieves a list of event type hosts based on provided filter, count, and pagination parameters.
        
        Args:
            event_type: Optional; a string specifying the event type to filter hosts by.
            count: Optional; an integer indicating the maximum number of hosts to return.
            page_token: Optional; a string token to retrieve the next page of results for pagination.
        
        Returns:
            A dictionary containing the JSON response with event type hosts data, which may include host details and pagination information.
        
        Raises:
            HTTPError: Raised when the HTTP request fails, typically due to bad status code.
        
        Tags:
            list, event-type, pagination, hosts-management, important
        """
        url = f"{self.base_url}/event_type_memberships"
        query_params = {
            k: v
            for k, v in [
                ("event_type", event_type),
                ("count", count),
                ("page_token", page_token),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_one_off_event_type(
        self,
        co_hosts=None,
        date_setting=None,
        duration=None,
        host=None,
        location=None,
        name=None,
        timezone=None,
    ) -> dict[str, Any]:
        """
        Creates a one-off event type with configurable parameters and returns details of the created event.
        
        Args:
            co_hosts: Optional; list or identifiers representing additional hosts for the event.
            date_setting: Optional; date configuration (e.g., specific date, range, or recurrence settings).
            duration: Optional; event length in minutes.
            host: Optional; main host/organizer identifier.
            location: Optional; physical address or virtual meeting link.
            name: Optional; title/name of the event.
            timezone: Optional; timezone where the event occurs.
        
        Returns:
            Dictionary containing created event details from the API.
        
        Raises:
            HTTPError: Raised for unsuccessful API responses (4XX/5XX status codes).
        
        Tags:
            create, one-off, event, management, api, important
        """
        request_body = {
            "co_hosts": co_hosts,
            "date_setting": date_setting,
            "duration": duration,
            "host": host,
            "location": location,
            "name": name,
            "timezone": timezone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/one_off_event_types"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sample_webhook_data(
        self, event=None, organization=None, user=None, scope=None
    ) -> dict[str, Any]:
        """
        Retrieves sample webhook data from the API using optional query parameters for event, organization, user, and scope filtering.
        
        Args:
            event: Optional string specifying the event type to filter webhook data.
            organization: Optional string representing the organization identifier for filtering.
            user: Optional string identifying the user for filtering.
            scope: Optional string indicating the scope for filtering.
        
        Returns:
            Dictionary containing JSON-formatted sample webhook data from the API.
        
        Raises:
            HTTPError: Raised when the API request fails (e.g., 4xx/5xx status codes).
        
        Tags:
            webhook, data-retrieval, api-integration, important
        """
        url = f"{self.base_url}/sample_webhook_data"
        query_params = {
            k: v
            for k, v in [
                ("event", event),
                ("organization", organization),
                ("user", user),
                ("scope", scope),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        """
        Returns a list of method references for various event, user, group, organization, and webhook operations supported by this instance.

        Args:
            None: This method does not accept any parameters.

        Returns:
            List of callable method references available on this instance for performing event, user, group, organization, and webhook operations.
        """
        return [
            self.list_event_invitees,
            self.get_event,
            self.get_event_invitee,
            self.list_events,
            self.get_event_type,
            self.list_user_sevent_types,
            self.get_user,
            self.get_current_user,
            self.list_organization_invitations,
            self.invite_user_to_organization,
            self.get_organization_invitation,
            self.revoke_user_sorganization_invitation,
            self.get_organization_membership,
            self.remove_user_from_organization,
            self.list_organization_memberships,
            self.get_webhook_subscription,
            self.delete_webhook_subscription,
            self.list_webhook_subscriptions,
            self.create_webhook_subscription,
            self.create_single_use_scheduling_link,
            self.delete_invitee_data,
            self.delete_scheduled_event_data,
            self.get_invitee_no_show,
            self.delete_invitee_no_show,
            self.create_invitee_no_show,
            self.get_group,
            self.list_groups,
            self.get_group_relationship,
            self.list_group_relationships,
            self.get_routing_form,
            self.list_routing_forms,
            self.get_routing_form_submission,
            self.list_routing_form_submissions,
            self.list_event_type_available_times,
            self.list_activity_log_entries,
            self.create_share,
            self.list_user_busy_times,
            self.get_user_availability_schedule,
            self.list_user_availability_schedules,
            self.list_event_type_hosts,
            self.create_one_off_event_type,
            self.get_sample_webhook_data,
        ]
