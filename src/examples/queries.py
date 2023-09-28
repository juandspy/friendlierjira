"""Some sample queries."""

SAMPLE_QUERIES = {
    "Issues from a given project": """SELECT
    key,
    created,
    creator_display_name,
    status,
    summary
FROM jira_issue
WHERE project_key = 'CCXDEV'
LIMIT 10;""",

    # FIXME: Not all sprints are shown
    "List sprints": """
SELECT
  id,
  name,
  board_id,
  state,
  start_date,
  end_date,
  complete_date
FROM
  jira_sprint;
""",

    "Tasks from a user": """
SELECT
    key,
    created,
    creator_display_name,
    status,
    summary,
    fields['Unknowns']['customfield_12310243'] story_points
FROM jira_issue
WHERE project_key = 'CCXDEV' AND creator_display_name = 'Juan Diaz Suarez'
LIMIT 10;
""",

    "Epics in this quarter":
"""
SELECT
    key,
    summary
    created,
    EXTRACT(DAY FROM NOW() - created) as age,
    assignee_display_name,
    creator_display_name,
    status,
    resolution_date,
    updated
FROM jira_issue
WHERE project_key = 'CCXDEV'
    AND type = 'Epic'
    AND fields['fixVersions'][0]->>'name' = '2023Q4'
LIMIT 10;
"""
}
