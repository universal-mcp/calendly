from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class CalendlyApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='calendly', integration=integration, **kwargs)
        self.base_url = "https://api.calendly.com"

    def list_event_invitees(self, uuid, status=None, sort=None, email=None, page_token=None, count=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of invitees for a specific scheduled event with optional filtering by status, email, and sorting parameters.

        Args:
            uuid (string): uuid
            status (string): Indicates if the invitee "canceled" or still "active" Example: 'active'.
            sort (string): Order results by the **created_at** field and direction specified: ascending ("asc") or descending ("desc") Example: 'created_at:asc'.
            email (string): Indicates if the results should be filtered by email address Example: '<email>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events, {uuid}, invitees
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/scheduled_events/{uuid}/invitees"
        query_params = {k: v for k, v in [('status', status), ('sort', sort), ('email', email), ('page_token', page_token), ('count', count)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event(self, uuid) -> dict[str, Any]:
        """
        Retrieves details about a scheduled event identified by the provided UUID using the GET method.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events, {uuid}
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
        Retrieves detailed information about a specific invitee for a scheduled event using their unique identifiers.

        Args:
            event_uuid (string): event_uuid
            invitee_uuid (string): invitee_uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events, {event_uuid}, invitees1, {invitee_uuid}
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

    def list_events(self, user=None, organization=None, invitee_email=None, status=None, sort=None, min_start_time=None, max_start_time=None, page_token=None, count=None, group=None) -> dict[str, Any]:
        """
        Retrieves a list of scheduled events filtered by user, organization, invitee, status, time range, and other parameters, supporting pagination and sorting.

        Args:
            user (string): Return events that are scheduled with the user associated with this URI Example: '<uri>'.
            organization (string): Return events that are scheduled with the organization associated with this URI Example: '<uri>'.
            invitee_email (string): Return events that are scheduled with the invitee associated with this email address Example: '<email>'.
            status (string): Whether the scheduled event is `active` or `canceled` Example: 'active'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values.
        Supported fields are: start_time.
        Sort direction is specified as: asc, desc. Example: '<string>'.
            min_start_time (string): Include events with start times after this time (sample time format: "2020-01-02T03:04:05.678123Z"). This time should use the UTC timezone. Example: '<string>'.
            max_start_time (string): Include events with start times prior to this time (sample time format: "2020-01-02T03:04:05.678123Z"). This time should use the UTC timezone. Example: '<string>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            group (string): Return events that are scheduled with the group associated with this URI Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            scheduled_events
        """
        url = f"{self.base_url}/scheduled_events"
        query_params = {k: v for k, v in [('user', user), ('organization', organization), ('invitee_email', invitee_email), ('status', status), ('sort', sort), ('min_start_time', min_start_time), ('max_start_time', max_start_time), ('page_token', page_token), ('count', count), ('group', group)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_event_type(self, uuid) -> dict[str, Any]:
        """
        Retrieves the details of a specific event type identified by its UUID using the path "/event_types/{uuid}" and the GET method.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            event_types, {uuid}1
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/event_types/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_sevent_types(self, active=None, organization=None, user=None, user_availability_schedule=None, sort=None, admin_managed=None, page_token=None, count=None) -> dict[str, Any]:
        """
        Retrieves a list of event types based on active status, organization, user, availability schedule, sorting, and pagination.

        Args:
            active (string): Return only active event types if true, only inactive if false, or all event types if this parameter is omitted. Example: '<boolean>'.
            organization (string): View available personal, team, and organization event types associated with the organization's URI. Example: '<uri>'.
            user (string): View available personal, team, and organization event types associated with the user's URI. Example: '<uri>'.
            user_availability_schedule (string): Used in conjunction with `user` parameter, returns a filtered list of Event Types that use the given primary availability schedule. Example: '<uri>'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values.Supported fields are: name, position, created_at, updated_at. Sort direction is specified as: asc, desc. Example: 'name:asc'.
            admin_managed (string): Return only admin managed event types if true, exclude admin managed event types if false, or include all event types if this parameter is omitted. Example: '<boolean>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.

        Returns:
            dict[str, Any]: OK

        Tags:
            event_types
        """
        url = f"{self.base_url}/event_types"
        query_params = {k: v for k, v in [('active', active), ('organization', organization), ('user', user), ('user_availability_schedule', user_availability_schedule), ('sort', sort), ('admin_managed', admin_managed), ('page_token', page_token), ('count', count)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user(self, uuid) -> dict[str, Any]:
        """
        Retrieves a user's details by their unique identifier (UUID) and returns the user data.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            users, {uuid}12
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/users/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_current_user(self) -> dict[str, Any]:
        """
        Retrieves information about the current user using the API.

        Returns:
            dict[str, Any]: OK

        Tags:
            users, me
        """
        url = f"{self.base_url}/users/me"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_invitations(self, uuid, count=None, page_token=None, sort=None, email=None, status=None) -> dict[str, Any]:
        """
        Retrieves a list of invitations for an organization identified by its UUID, allowing filtering by count, page token, sort order, email, and invitation status.

        Args:
            uuid (string): uuid
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            sort (string): Order results by the field name and direction specified (ascending or descending). Returns multiple sets of results in a comma-separated list. Example: 'created_at:asc'.
            email (string): Indicates if the results should be filtered by email address Example: '<email>'.
            status (string): Indicates if the results should be filtered by status ("pending", "accepted", or "declined") Example: 'accepted'.

        Returns:
            dict[str, Any]: OK

        Tags:
            organizations, {uuid}123, invitations
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organizations/{uuid}/invitations"
        query_params = {k: v for k, v in [('count', count), ('page_token', page_token), ('sort', sort), ('email', email), ('status', status)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def invite_user_to_organization(self, uuid, email=None) -> dict[str, Any]:
        """
        Creates an invitation for a user to join an organization, identified by the provided UUID, and sends it to the specified recipient.

        Args:
            uuid (string): uuid
            email (string): email
                Example:
                ```json
                {
                  "email": "<email>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            organizations, {uuid}123, invitations
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        request_body = {
            'email': email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/organizations/{uuid}/invitations"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_invitation(self, org_uuid, uuid) -> dict[str, Any]:
        """
        Retrieves information about an organization invitation identified by its UUID, returning details about the invitation using the specified organization UUID and invitation UUID.

        Args:
            org_uuid (string): org_uuid
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            organizations, {org_uuid}, invitations1, {uuid}1234
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
        Deletes one or more organization invitations and returns success or error codes indicating invalid tokens, missing invitations, or authorization issues.

        Args:
            org_uuid (string): org_uuid
            uuid (string): uuid

        Returns:
            Any: No Content

        Tags:
            organizations, {org_uuid}, invitations1, {uuid}1234
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
        Retrieves details of a specific organization membership using its unique identifier.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            organization_memberships, {uuid}12345
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
        Removes a user from an organization using the specified UUID and returns a success status if the operation is completed without errors.

        Args:
            uuid (string): uuid

        Returns:
            Any: No Content

        Tags:
            organization_memberships, {uuid}12345
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/organization_memberships/{uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_organization_memberships(self, page_token=None, count=None, email=None, organization=None, user=None) -> dict[str, Any]:
        """
        Retrieves and lists organization memberships for specified users or organizations, supporting filtering by user, organization, and other criteria, using the "GET" method at the "/organization_memberships" path.

        Args:
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            email (string): Indicates if the results should be filtered by email address Example: '<email>'.
            organization (string): Indicates if the results should be filtered by organization Example: '<uri>'.
            user (string): Indicates if the results should be filtered by user Example: '<uri>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            organization_memberships
        """
        url = f"{self.base_url}/organization_memberships"
        query_params = {k: v for k, v in [('page_token', page_token), ('count', count), ('email', email), ('organization', organization), ('user', user)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_subscription(self, webhook_uuid) -> dict[str, Any]:
        """
        Retrieves the details of a webhook subscription identified by the specified `webhook_uuid`, returning relevant subscription information in response.

        Args:
            webhook_uuid (string): webhook_uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            webhook_subscriptions, {webhook_uuid}
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
        Deletes a webhook subscription identified by its unique UUID and returns a success response upon completion.

        Args:
            webhook_uuid (string): webhook_uuid

        Returns:
            Any: No Content

        Tags:
            webhook_subscriptions, {webhook_uuid}
        """
        if webhook_uuid is None:
            raise ValueError("Missing required parameter 'webhook_uuid'")
        url = f"{self.base_url}/webhook_subscriptions/{webhook_uuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_webhook_subscriptions(self, organization=None, user=None, page_token=None, count=None, sort=None, scope=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of webhook subscriptions filtered by organization, user, and scope, with options for sorting and count.

        Args:
            organization (string): (Required) Indicates if the results should be filtered by organization Example: '<uri>'.
            user (string): Indicates if the results should be filtered by user. This parameter is only required if the `scope` parameter is set to `user`. Example: '<uri>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values.
        Supported fields are: created_at.
        Sort direction is specified as: asc, desc. Example: '<string>'.
            scope (string): (Required) Filter the list by organization or user Example: 'user'.

        Returns:
            dict[str, Any]: OK

        Tags:
            webhook_subscriptions
        """
        url = f"{self.base_url}/webhook_subscriptions"
        query_params = {k: v for k, v in [('organization', organization), ('user', user), ('page_token', page_token), ('count', count), ('sort', sort), ('scope', scope)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook_subscription(self, events=None, group=None, organization=None, scope=None, signing_key=None, url=None, user=None) -> dict[str, Any]:
        """
        Creates a new webhook subscription to receive notifications for specified events from a Squarespace website.

        Args:
            events (array): events Example: "['invitee.canceled', 'routing_form_submission.created']".
            group (string): group Example: '<uri>'.
            organization (string): organization Example: '<uri>'.
            scope (string): scope Example: 'organization'.
            signing_key (string): signing_key Example: '<string>'.
            url (string): url Example: '<uri>'.
            user (string): user
                Example:
                ```json
                {
                  "events": [
                    "invitee.canceled",
                    "routing_form_submission.created"
                  ],
                  "group": "<uri>",
                  "organization": "<uri>",
                  "scope": "organization",
                  "signing_key": "<string>",
                  "url": "<uri>",
                  "user": "<uri>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            webhook_subscriptions
        """
        request_body = {
            'events': events,
            'group': group,
            'organization': organization,
            'scope': scope,
            'signing_key': signing_key,
            'url': url,
            'user': user,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/webhook_subscriptions"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_single_use_scheduling_link(self, max_event_count=None, owner=None, owner_type=None) -> dict[str, Any]:
        """
        Creates a new scheduling link using the "POST" method at the "/scheduling_links" path, allowing users to generate customized links for scheduling events.

        Args:
            max_event_count (number): max_event_count Example: '1'.
            owner (string): owner Example: '<uri>'.
            owner_type (string): owner_type
                Example:
                ```json
                {
                  "max_event_count": 1,
                  "owner": "<uri>",
                  "owner_type": "EventType"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            scheduling_links
        """
        request_body = {
            'max_event_count': max_event_count,
            'owner': owner,
            'owner_type': owner_type,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/scheduling_links"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_invitee_data(self, emails=None) -> dict[str, Any]:
        """
        Initiates data deletion requests for invitees in compliance with data privacy regulations.

        Args:
            emails (array): emails
                Example:
                ```json
                {
                  "emails": [
                    "<email>",
                    "<email>"
                  ]
                }
                ```

        Returns:
            dict[str, Any]: Accepted

        Tags:
            data_compliance, deletion, invitees12
        """
        request_body = {
            'emails': emails,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/data_compliance/deletion/invitees"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_event_data(self, end_time=None, start_time=None) -> dict[str, Any]:
        """
        Submits data deletion requests for compliance events and returns asynchronous processing confirmation.

        Args:
            end_time (string): end_time Example: '<dateTime>'.
            start_time (string): start_time
                Example:
                ```json
                {
                  "end_time": "<dateTime>",
                  "start_time": "<dateTime>"
                }
                ```

        Returns:
            dict[str, Any]: Accepted

        Tags:
            data_compliance, deletion, events
        """
        request_body = {
            'end_time': end_time,
            'start_time': start_time,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/data_compliance/deletion/events"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_invitee_no_show(self, uuid) -> dict[str, Any]:
        """
        Retrieves information about an invitee who did not show up, identified by a specific UUID, using the GET method via the API endpoint "/invitee_no_shows/{uuid}".

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            invitee_no_shows, {uuid}123456
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
        Removes an invitee's "no-show" status using their unique identifier (uuid) and returns an empty response upon successful deletion.

        Args:
            uuid (string): uuid

        Returns:
            Any: No Content

        Tags:
            invitee_no_shows, {uuid}123456
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
        Triggers an action related to invitee no-shows using the POST method at the "/invitee_no_shows" endpoint, returning a status message based on the response codes provided.

        Args:
            invitee (string): invitee
                Example:
                ```json
                {
                  "invitee": "<uri>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            invitee_no_shows
        """
        request_body = {
            'invitee': invitee,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/invitee_no_shows"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_group(self, uuid) -> dict[str, Any]:
        """
        Retrieves information about a group specified by its UUID from the API.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            groups, {uuid}1234567
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/groups/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_groups(self, organization=None, page_token=None, count=None) -> dict[str, Any]:
        """
        Retrieves a list of groups for a specified organization using the GitHub API, with optional pagination controls.

        Args:
            organization (string): (Required) Return groups that are associated with the organization associated with this URI Example: '<string>'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.

        Returns:
            dict[str, Any]: OK

        Tags:
            groups
        """
        url = f"{self.base_url}/groups"
        query_params = {k: v for k, v in [('organization', organization), ('page_token', page_token), ('count', count)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_group_relationship(self, uuid) -> dict[str, Any]:
        """
        Retrieves information about group relationships identified by the specified UUID using the GET method.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            group_relationships, {uuid}12345678
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/group_relationships/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_group_relationships(self, count=None, page_token=None, organization=None, owner=None, group=None) -> dict[str, Any]:
        """
        Retrieves a list of group relationships filtered by organization, owner, or group, using pagination parameters for controlled results.

        Args:
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            organization (string): Indicates the results should be filtered by organization Example: '<uri>'.
            owner (string): Indicates the results should be filtered by owner <br>
        One Of: - Organization Membership URI - ` - Organization Invitation URI - ` Example: '<uri>'.
            group (string): Indicates the results should be filtered by group Example: '<uri>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            group_relationships
        """
        url = f"{self.base_url}/group_relationships"
        query_params = {k: v for k, v in [('count', count), ('page_token', page_token), ('organization', organization), ('owner', owner), ('group', group)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_routing_form(self, uuid) -> dict[str, Any]:
        """
        Retrieves a routing form by its unique identifier (UUID) using the GET method via the "/routing_forms/{uuid}" path.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_forms, {uuid}123456789
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/routing_forms/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_routing_forms(self, organization=None, count=None, page_token=None, sort=None) -> dict[str, Any]:
        """
        Retrieves a list of routing forms for a specified organization with pagination, sorting, and count parameters.

        Args:
            organization (string): (Required) View organization routing forms associated with the organization's URI. Example: '<uri>'.
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values. Supported fields are: created_at. Sort direction is specified as: asc, desc. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_forms
        """
        url = f"{self.base_url}/routing_forms"
        query_params = {k: v for k, v in [('organization', organization), ('count', count), ('page_token', page_token), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_routing_form_submission(self, uuid) -> dict[str, Any]:
        """
        Retrieves a specific routing form submission by its unique identifier (UUID) using the Calendly API.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_form_submissions, {uuid}12345678910
        """
        if uuid is None:
            raise ValueError("Missing required parameter 'uuid'")
        url = f"{self.base_url}/routing_form_submissions/{uuid}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_routing_form_submissions(self, form=None, count=None, page_token=None, sort=None) -> dict[str, Any]:
        """
        Retrieves routing form submissions using the GET method at "/routing_form_submissions", allowing filtering by form, count, page token, and sort order.

        Args:
            form (string): (Required) View routing form submissions associated with the routing form's URI. Example: '<uri>'.
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.
            sort (string): Order results by the specified field and direction. Accepts comma-separated list of {field}:{direction} values. Supported fields are: created_at. Sort direction is specified as: asc, desc. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            routing_form_submissions
        """
        url = f"{self.base_url}/routing_form_submissions"
        query_params = {k: v for k, v in [('form', form), ('count', count), ('page_token', page_token), ('sort', sort)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_type_available_times(self, event_type=None, start_time=None, end_time=None) -> dict[str, Any]:
        """
        Retrieves a list of available times for a specified event type within a given date range, using the event type, start time, and end time as query parameters.

        Args:
            event_type (string): (Required) The uri associated with the event type Example: '<uri>'.
            start_time (string): (Required) Start time of the requested availability range. Example: '<string>'.
            end_time (string): (Required) End time of the requested availability range. Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            event_type_available_times
        """
        url = f"{self.base_url}/event_type_available_times"
        query_params = {k: v for k, v in [('event_type', event_type), ('start_time', start_time), ('end_time', end_time)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_activity_log_entries(self, organization=None, search_term=None, actor=None, sort=None, min_occurred_at=None, max_occurred_at=None, page_token=None, count=None, namespace=None, action=None) -> dict[str, Any]:
        """
        Retrieves filtered activity log entries based on parameters like organization, actor, timestamps, and action, supporting sorting and pagination.

        Args:
            organization (string): (Required) Return activity log entries from the organization associated with this URI Example: '<uri>'.
            search_term (string): Filters entries based on the search term. Supported operators: - `|` - to allow filtering by one term or another. Example: `this | that` - `+` - to allow filtering by one term and another. Example: `this + that` - `"` - to allow filtering by an exact search term. Example: `"email@website.com"` - `-` - to omit specific terms from results. Example: `Added -User` - `()` - to allow specifying precedence during a search. Example: `(this + that) OR (person + place)` - `*` - to allow prefix searching. Example `*@other-website.com` Example: '<string>'.
            actor (string): Return entries from the user(s) associated with the provided URIs Example: '<uri>,<uri>'.
            sort (string): Order results by the specified field and direction. List of {field}:{direction} values. Example: 'occurred_at:desc'.
            min_occurred_at (string): Include entries that occurred after this time (sample time format: "2020-01-02T03:04:05.678Z"). This time should use the UTC timezone. Example: '<dateTime>'.
            max_occurred_at (string): Include entries that occurred prior to this time (sample time format: "2020-01-02T03:04:05.678Z"). This time should use the UTC timezone. Example: '<dateTime>'.
            page_token (string): The token to pass to get the next portion of the collection Example: '<string>'.
            count (string): The number of rows to return Example: '20'.
            namespace (string): The categories of the entries Example: '<string>,<string>'.
            action (string): The action(s) associated with the entries Example: '<string>,<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            activity_log_entries
        """
        url = f"{self.base_url}/activity_log_entries"
        query_params = {k: v for k, v in [('organization', organization), ('search_term', search_term), ('actor', actor), ('sort', sort), ('min_occurred_at', min_occurred_at), ('max_occurred_at', max_occurred_at), ('page_token', page_token), ('count', count), ('namespace', namespace), ('action', action)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_share(self, availability_rule=None, duration=None, end_date=None, event_type=None, hide_location=None, location_configurations=None, max_booking_time=None, name=None, period_type=None, start_date=None) -> dict[str, Any]:
        """
        Creates a new share resource and returns a status message.

        Args:
            availability_rule (object): availability_rule
            duration (string): duration Example: '<integer>'.
            end_date (string): end_date Example: '<date>'.
            event_type (string): event_type Example: '<uri>'.
            hide_location (string): hide_location Example: '<boolean>'.
            location_configurations (array): location_configurations Example: "[{'additional_info': '<string>', 'kind': 'ask_invitee', 'location': '<string>', 'phone_number': '<string>', 'position': '<integer>'}, {'additional_info': '<string>', 'kind': 'microsoft_teams_conference', 'location': '<string>', 'phone_number': '<string>', 'position': '<integer>'}]".
            max_booking_time (string): max_booking_time Example: '<integer>'.
            name (string): name Example: '<string>'.
            period_type (string): period_type Example: 'fixed'.
            start_date (string): start_date
                Example:
                ```json
                {
                  "availability_rule": {
                    "rules": [
                      {
                        "date": "<date>",
                        "intervals": [
                          {
                            "from": "87:41",
                            "to": "67:37"
                          },
                          {
                            "from": "37:88",
                            "to": "18:71"
                          }
                        ],
                        "type": "date",
                        "wday": "wednesday"
                      },
                      {
                        "date": "<date>",
                        "intervals": [
                          {
                            "from": "56:49",
                            "to": "38:81"
                          },
                          {
                            "from": "65:67",
                            "to": "87:67"
                          }
                        ],
                        "type": "wday",
                        "wday": "tuesday"
                      }
                    ],
                    "timezone": "<string>"
                  },
                  "duration": "<integer>",
                  "end_date": "<date>",
                  "event_type": "<uri>",
                  "hide_location": "<boolean>",
                  "location_configurations": [
                    {
                      "additional_info": "<string>",
                      "kind": "ask_invitee",
                      "location": "<string>",
                      "phone_number": "<string>",
                      "position": "<integer>"
                    },
                    {
                      "additional_info": "<string>",
                      "kind": "microsoft_teams_conference",
                      "location": "<string>",
                      "phone_number": "<string>",
                      "position": "<integer>"
                    }
                  ],
                  "max_booking_time": "<integer>",
                  "name": "<string>",
                  "period_type": "fixed",
                  "start_date": "<date>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            shares
        """
        request_body = {
            'availability_rule': availability_rule,
            'duration': duration,
            'end_date': end_date,
            'event_type': event_type,
            'hide_location': hide_location,
            'location_configurations': location_configurations,
            'max_booking_time': max_booking_time,
            'name': name,
            'period_type': period_type,
            'start_date': start_date,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/shares"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_busy_times(self, user=None, start_time=None, end_time=None) -> dict[str, Any]:
        """
        Retrieves an ascending list of a user's internal and external scheduled events within a specified date range using the "/user_busy_times" endpoint, allowing for efficient management of busy times.

        Args:
            user (string): (Required) The uri associated with the user Example: '<uri>'.
            start_time (string): (Required) Start time of the requested availability range Example: '<string>'.
            end_time (string): (Required) End time of the requested availability range Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            user_busy_times
        """
        url = f"{self.base_url}/user_busy_times"
        query_params = {k: v for k, v in [('user', user), ('start_time', start_time), ('end_time', end_time)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_user_availability_schedule(self, uuid) -> dict[str, Any]:
        """
        Retrieves the availability schedule of a user based on the provided UUID using the GET method.

        Args:
            uuid (string): uuid

        Returns:
            dict[str, Any]: OK

        Tags:
            user_availability_schedules, {uuid}1234567891011
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
        Retrieves the availability schedule for a specified user, including time intervals when booking is permitted.

        Args:
            user (string): (Required) A URI reference to a user Example: '<uri>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            user_availability_schedules
        """
        url = f"{self.base_url}/user_availability_schedules"
        query_params = {k: v for k, v in [('user', user)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_event_type_hosts(self, event_type=None, count=None, page_token=None) -> dict[str, Any]:
        """
        Retrieves paginated event type memberships filtered by event type, count, and page token.

        Args:
            event_type (string): (Required) The uri associated with the event type Example: '<uri>'.
            count (string): The number of rows to return Example: '20'.
            page_token (string): The token to pass to get the next or previous portion of the collection Example: '<string>'.

        Returns:
            dict[str, Any]: OK

        Tags:
            event_type_memberships
        """
        url = f"{self.base_url}/event_type_memberships"
        query_params = {k: v for k, v in [('event_type', event_type), ('count', count), ('page_token', page_token)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_one_off_event_type(self, co_hosts=None, date_setting=None, duration=None, host=None, location=None, name=None, timezone=None) -> dict[str, Any]:
        """
        Creates a one-off event type using the "POST" method, allowing for the setup of a single, unique event configuration.

        Args:
            co_hosts (array): co_hosts Example: "['<uri>', '<uri>']".
            date_setting (object): date_setting
            duration (string): duration Example: '<number>'.
            host (string): host Example: '<uri>'.
            location (object): location
            name (string): name Example: '<string>'.
            timezone (string): timezone
                Example:
                ```json
                {
                  "co_hosts": [
                    "<uri>",
                    "<uri>"
                  ],
                  "date_setting": {
                    "value": "reference ./models/date_setting/DateRange.yaml not found in the OpenAPI spec"
                  },
                  "duration": "<number>",
                  "host": "<uri>",
                  "location": {
                    "value": "reference ./models/adhoc-locations/CustomLocation.yaml not found in the OpenAPI spec"
                  },
                  "name": "<string>",
                  "timezone": "<string>"
                }
                ```

        Returns:
            dict[str, Any]: Created

        Tags:
            one_off_event_types
        """
        request_body = {
            'co_hosts': co_hosts,
            'date_setting': date_setting,
            'duration': duration,
            'host': host,
            'location': location,
            'name': name,
            'timezone': timezone,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/one_off_event_types"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sample_webhook_data(self, event=None, organization=None, user=None, scope=None) -> dict[str, Any]:
        """
        Retrieves sample webhook data filtered by event type, organization, user, and scope parameters.

        Args:
            event (string): (Required) Example: 'invitee.created'.
            organization (string): (Required) Example: '<uri>'.
            user (string): Specifies the user identifier or name for filtering or retrieving specific data in the response. Example: '<uri>'.
            scope (string): (Required) Example: 'user'.

        Returns:
            dict[str, Any]: OK

        Tags:
            sample_webhook_data
        """
        url = f"{self.base_url}/sample_webhook_data"
        query_params = {k: v for k, v in [('event', event), ('organization', organization), ('user', user), ('scope', scope)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
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
            self.get_sample_webhook_data
        ]
