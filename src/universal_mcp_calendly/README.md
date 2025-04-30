
# Calendly MCP Server

An MCP Server for the Calendly API.

## Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## Tools

This is automatically generated from OpenAPI schema for the Calendly API.

## Supported Integrations

This tool can be integrated with any service that supports HTTP requests.

## Tool List

| Tool | Description |
|------|-------------|
| `list_event_invitees` | Retrieves a list of invitees for a specific scheduled event with optional filtering and pagination support. |
| `get_event` | Retrieves the details of a scheduled event using its unique identifier. |
| `get_event_invitee` | Retrieves details about a specific invitee for a given scheduled event. |
| `list_events` | Retrieves a list of scheduled events based on specified filters such as user, organization, invitee email, status, date range, sorting, and pagination criteria. |
| `get_event_type` | Retrieves the event type details for the specified UUID from the API. |
| `list_user_sevent_types` | Retrieves a paginated list of user event types with optional filtering, sorting, and pagination parameters. |
| `get_user` | Retrieves detailed user information for a specified UUID from a remote API. |
| `get_current_user` | Retrieves information about the currently authenticated user from the API. |
| `list_organization_invitations` | Retrieves a paginated list of invitations for a specified organization with optional filtering, sorting, and pagination. |
| `invite_user_to_organization` | Sends an invitation to a specified email address to join an organization identified by its UUID. |
| `get_organization_invitation` | Retrieves a specific invitation for an organization using its unique identifiers. |
| `revoke_user_sorganization_invitation` | Revokes a user's invitation to an organization by deleting the specified invitation resource. |
| `get_organization_membership` | Retrieves the membership information for a specified organization membership UUID. |
| `remove_user_from_organization` | Removes a user from the organization by deleting their membership using the specified UUID |
| `list_organization_memberships` | Retrieves a list of organization memberships with optional filtering by pagination, email, organization, or user parameters. |
| `get_webhook_subscription` | Retrieves the details of a webhook subscription identified by its UUID. |
| `delete_webhook_subscription` | Deletes a webhook subscription identified by its UUID from the server using the provided UUID. |
| `list_webhook_subscriptions` | Retrieves a paginated list of webhook subscriptions with optional filtering parameters. |
| `create_webhook_subscription` | Creates a new webhook subscription with customizable parameters and returns its configuration details. |
| `create_single_use_scheduling_link` | Creates a single-use scheduling link by sending a POST request with optional restrictions. |
| `delete_invitee_data` | Deletes invitee data for specified email addresses by sending a POST request to the data compliance API. |
| `delete_scheduled_event_data` | Deletes scheduled event data within the specified time range by sending a deletion request to the data compliance service. |
| `get_invitee_no_show` | Retrieves details about an invitee who did not show up for a scheduled event, identified by a unique UUID. |
| `delete_invitee_no_show` | Deletes an invitee no-show record identified by the given UUID. |
| `create_invitee_no_show` | Creates an invitee no-show record via POST request to the invitee_no_shows endpoint. |
| `get_group` | Retrieves a group's details from the server by its UUID. |
| `list_groups` | Retrieves a paginated list of groups from the API, optionally filtered by organization. |
| `get_group_relationship` | Retrieves the relationship information for a group by UUID from the API. |
| `list_group_relationships` | Retrieves paginated group relationships from the server with optional filtering parameters. |
| `get_routing_form` | Retrieves a specific routing form by its unique identifier from the server. |
| `list_routing_forms` | Retrieves a paginated list of routing forms from the API with optional filtering, sorting, and pagination. |
| `get_routing_form_submission` | Retrieves a routing form submission by its unique identifier (UUID) from the configured API endpoint. |
| `list_routing_form_submissions` | Retrieves a list of routing form submissions with optional filtering and pagination. |
| `list_event_type_available_times` | Retrieves available scheduling times for specified event types within an optional datetime range. |
| `list_activity_log_entries` | Retrieves a list of activity log entries with optional filtering, sorting, and pagination. |
| `create_share` | Creates a new share with specified configuration by sending a POST request to the shares API endpoint. |
| `list_user_busy_times` | Retrieves a list of busy time intervals for specified users within an optional date range. |
| `get_user_availability_schedule` | Retrieves the availability schedule for a user identified by the given UUID. |
| `list_user_availability_schedules` | Retrieves user availability schedules from the API, optionally filtered by a specific user identifier. |
| `list_event_type_hosts` | Retrieves a list of event type hosts based on provided filter, count, and pagination parameters. |
| `create_one_off_event_type` | Creates a one-off event type with configurable parameters and returns details of the created event. |
| `get_sample_webhook_data` | Retrieves sample webhook data from the API using optional query parameters for event, organization, user, and scope filtering. |
| `list_tools` | Returns a list of method references for various event, user, group, organization, and webhook operations supported by this instance. |

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Calendly app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server
