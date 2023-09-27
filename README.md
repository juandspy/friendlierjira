
## Steampipe + Jira plugin as a container

Build the Steampipe + Jira plugin image:
```
podman build -f steampipe-jira.Dockerfile -t steampipe-jira .
```

Run it as a service:
```
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
```
podman logs --follow steampipe-jira
```

You can then use any CLI tool to connect to the PostgreSQL database:
```
pgcli "postgres://steampipe:$STEAMPIPE_DATABASE_PASSWORD@localhost:9193/steampipe?sslmode=require"
```
