# Calendly MCP Server

An MCP Server for the Calendly API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Calendly API.


| Tool | Description |
|------|-------------|
| `list_event_invitees` | Retrieves a paginated list of invitees for a specific scheduled event with optional filtering by status, email, and sorting parameters. |
| `get_event` | Retrieves details about a scheduled event identified by the provided UUID using the GET method. |
| `get_event_invitee` | Retrieves detailed information about a specific invitee for a scheduled event using their unique identifiers. |
| `list_events` | Retrieves a list of scheduled events filtered by user, organization, invitee, status, time range, and other parameters, supporting pagination and sorting. |
| `get_event_type` | Retrieves the details of a specific event type identified by its UUID using the path "/event_types/{uuid}" and the GET method. |
| `list_user_sevent_types` | Retrieves a list of event types based on active status, organization, user, availability schedule, sorting, and pagination. |
| `get_user` | Retrieves a user's details by their unique identifier (UUID) and returns the user data. |
| `get_current_user` | Retrieves information about the current user using the API. |
| `list_organization_invitations` | Retrieves a list of invitations for an organization identified by its UUID, allowing filtering by count, page token, sort order, email, and invitation status. |
| `invite_user_to_organization` | Creates an invitation for a user to join an organization, identified by the provided UUID, and sends it to the specified recipient. |
| `get_organization_invitation` | Retrieves information about an organization invitation identified by its UUID, returning details about the invitation using the specified organization UUID and invitation UUID. |
| `revoke_user_sorganization_invitation` | Deletes one or more organization invitations and returns success or error codes indicating invalid tokens, missing invitations, or authorization issues. |
| `get_organization_membership` | Retrieves details of a specific organization membership using its unique identifier. |
| `remove_user_from_organization` | Removes a user from an organization using the specified UUID and returns a success status if the operation is completed without errors. |
| `list_organization_memberships` | Retrieves and lists organization memberships for specified users or organizations, supporting filtering by user, organization, and other criteria, using the "GET" method at the "/organization_memberships" path. |
| `get_webhook_subscription` | Retrieves the details of a webhook subscription identified by the specified `webhook_uuid`, returning relevant subscription information in response. |
| `delete_webhook_subscription` | Deletes a webhook subscription identified by its unique UUID and returns a success response upon completion. |
| `list_webhook_subscriptions` | Retrieves a paginated list of webhook subscriptions filtered by organization, user, and scope, with options for sorting and count. |
| `create_webhook_subscription` | Creates a new webhook subscription to receive notifications for specified events from a Squarespace website. |
| `create_single_use_scheduling_link` | Creates a new scheduling link using the "POST" method at the "/scheduling_links" path, allowing users to generate customized links for scheduling events. |
| `delete_invitee_data` | Initiates data deletion requests for invitees in compliance with data privacy regulations. |
| `delete_scheduled_event_data` | Submits data deletion requests for compliance events and returns asynchronous processing confirmation. |
| `get_invitee_no_show` | Retrieves information about an invitee who did not show up, identified by a specific UUID, using the GET method via the API endpoint "/invitee_no_shows/{uuid}". |
| `delete_invitee_no_show` | Removes an invitee's "no-show" status using their unique identifier (uuid) and returns an empty response upon successful deletion. |
| `create_invitee_no_show` | Triggers an action related to invitee no-shows using the POST method at the "/invitee_no_shows" endpoint, returning a status message based on the response codes provided. |
| `get_group` | Retrieves information about a group specified by its UUID from the API. |
| `list_groups` | Retrieves a list of groups for a specified organization using the GitHub API, with optional pagination controls. |
| `get_group_relationship` | Retrieves information about group relationships identified by the specified UUID using the GET method. |
| `list_group_relationships` | Retrieves a list of group relationships filtered by organization, owner, or group, using pagination parameters for controlled results. |
| `get_routing_form` | Retrieves a routing form by its unique identifier (UUID) using the GET method via the "/routing_forms/{uuid}" path. |
| `list_routing_forms` | Retrieves a list of routing forms for a specified organization with pagination, sorting, and count parameters. |
| `get_routing_form_submission` | Retrieves a specific routing form submission by its unique identifier (UUID) using the Calendly API. |
| `list_routing_form_submissions` | Retrieves routing form submissions using the GET method at "/routing_form_submissions", allowing filtering by form, count, page token, and sort order. |
| `list_event_type_available_times` | Retrieves a list of available times for a specified event type within a given date range, using the event type, start time, and end time as query parameters. |
| `list_activity_log_entries` | Retrieves filtered activity log entries based on parameters like organization, actor, timestamps, and action, supporting sorting and pagination. |
| `create_share` | Creates a new share resource and returns a status message. |
| `list_user_busy_times` | Retrieves an ascending list of a user's internal and external scheduled events within a specified date range using the "/user_busy_times" endpoint, allowing for efficient management of busy times. |
| `get_user_availability_schedule` | Retrieves the availability schedule of a user based on the provided UUID using the GET method. |
| `list_user_availability_schedules` | Retrieves the availability schedule for a specified user, including time intervals when booking is permitted. |
| `list_event_type_hosts` | Retrieves paginated event type memberships filtered by event type, count, and page token. |
| `create_one_off_event_type` | Creates a one-off event type using the "POST" method, allowing for the setup of a single, unique event configuration. |
| `get_sample_webhook_data` | Retrieves sample webhook data filtered by event type, organization, user, and scope parameters. |
