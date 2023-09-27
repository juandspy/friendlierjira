# Friendlier Jira

The goal of this tool is to provide a friendly UI to run SQL queries and
build dashboards.

The project is built on top of: 
- [Steampipe](https://github.com/turbot/steampipe)
- [Streamlit](https://github.com/streamlit/streamlit)

> **DISCLAIMER**: due to a [bug in the Steampipe Jira plugin](https://github.com/turbot/steampipe-plugin-jira/pull/86/commits/6121a8a5faa17c186c58d78c2086a1a3de25da3c), most of the tables are currently unusable with self hosted Jira instances. Also, some queries may need a couple of minutes to complete.

## Screenshots

<details>
<summary>Run custom queries</summary>
<br>

![Custom queries](docs/static/custom_queries.png)

</details>

<details>
<summary>Create custom dashboards</summary>
<br>

![Custom dashboards](docs/static/custom_dashboards.png)

</details>

<details>
<summary>Use the prebuilt dashboards</summary>
<br>

![Prebuilt dashboards](docs/static/prebuilt_dashboards.png)

</details>

## Run it as a container

Create a `.env` file containing:

```sh
STEAMPIPE_CACHE_MAX_TTL=3600          # DB max TTL
STEAMPIPE_CACHE_TTL=3600              # DB TTL
STEAMPIPE_DATABASE_PASSWORD=ABCDEFGH  # Password to connect to the Steampipe DB
QUERY_TIMEOUT_SECONDS=60              # Use -1 to disable it

JIRA_URL=YOUR_JIRA_URL
JIRA_PERSONAL_ACCESS_TOKEN=YOUR_JIRA_PERSONAL_ACCESS_TOKEN
JIRA_USER=YOUR_JIRA_USER
```

You can just use `make run` or do it manually:

Build the Steampipe + Jira plugin image:
```sh
podman build -f steampipe-jira.Dockerfile -t steampipe-jira .
```

Run it as a service:
```sh
source .env
podman run \
    -p 9193:9193 \
    -d \
    -e STEAMPIPE_DATABASE_PASSWORD="$STEAMPIPE_DATABASE_PASSWORD" \
    -e JIRA_URL="$JIRA_URL" \
    -e JIRA_PERSONAL_ACCESS_TOKEN="$JIRA_PERSONAL_ACCESS_TOKEN" \
    -e JIRA_USER="$JIRA_USER" \
    --name steampipe-jira \
    --rm \
    steampipe-jira service start --foreground
```

You can see the container logs using:
```sh
podman logs --follow steampipe-jira
```

You can then use any CLI tool to connect to the PostgreSQL database:
```sh
pgcli "postgres://steampipe:$STEAMPIPE_DATABASE_PASSWORD@localhost:9193/steampipe?sslmode=require"
```
