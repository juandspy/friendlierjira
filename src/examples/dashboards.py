"""Sample dashboards."""
import plotly.express as px

from src.dashboard import Dashboard

SAMPLE_DASHBOARDS = [
    Dashboard(
        name="Backlog status",
        query="""
SELECT
    status,
    DATE_TRUNC('month', created) AS month,
    COUNT(*) AS issue_count
FROM jira_issue
WHERE project_key = 'CCXDEV'
    AND LOWER(labels::TEXT)::jsonb ? 'ccx-processing'
    AND EXTRACT(YEAR FROM DATE_TRUNC('month', created)) > 2000
GROUP BY month, status;
""",
        x="month",
        y="issue_count",
        group_by="status"),

    Dashboard(
        name="Tasks created per user",
        query="""
SELECT
    creator_display_name,
    DATE_TRUNC('month', created) AS month,
    COUNT(*) AS issue_count
FROM jira_issue
WHERE project_key = 'CCXDEV'
    AND status = 'Closed'
    AND LOWER(labels::TEXT)::jsonb ? 'ccx-processing'
GROUP BY creator_display_name, month
HAVING EXTRACT(YEAR FROM DATE_TRUNC('month', created)) > 2020;
""",
        x="month",
        y="issue_count",
        group_by="creator_display_name",
        plot_fun=px.line),

    Dashboard(
        name="User speed (issue count)",
        query="""
SELECT
    assignee_display_name,
    DATE_TRUNC('month', resolution_date) AS month,
    COUNT(*) AS issue_count
FROM jira_issue
WHERE project_key = 'CCXDEV'
AND assignee_display_name = 'Juan Diaz Suarez'
    AND status = 'Closed'
    AND LOWER(labels::TEXT)::jsonb ? 'ccx-processing'
GROUP BY assignee_display_name, month;
""",
        x="month",
        y="issue_count",
        group_by="assignee_display_name",
        add_trend=True),

    Dashboard(
        name="User speed (story points)",
        query="""
SELECT
    assignee_display_name,
    DATE_TRUNC('month', resolution_date) AS month,
    SUM(
        CAST(fields['Unknowns'] ->> 'customfield_12310243' AS DECIMAL)
        ) AS total_story_points
FROM jira_issue
WHERE project_key = 'CCXDEV'
    AND assignee_display_name = 'Juan Diaz Suarez'
    AND status = 'Closed'
    AND LOWER(labels::TEXT)::jsonb ? 'ccx-processing'
GROUP BY assignee_display_name, month;
""",
        x="month",
        y="total_story_points",
        group_by="assignee_display_name",
        add_trend=True),

    Dashboard(
        name="Project speed (issue count, all users)",
        query="""
SELECT
    assignee_display_name,
    DATE_TRUNC('month', resolution_date) AS month,
    COUNT(*) AS issue_count
FROM jira_issue
WHERE project_key = 'CCXDEV'
    AND status = 'Closed'
    AND LOWER(labels::TEXT)::jsonb ? 'ccx-processing'
GROUP BY assignee_display_name, month
HAVING EXTRACT(YEAR FROM DATE_TRUNC('month', resolution_date)) > 2000;
""",
        x="month",
        y="issue_count",
        group_by="assignee_display_name",
        plot_fun=px.line),

    Dashboard(
        name="Project speed (story points, all users)",
        query="""
SELECT
    assignee_display_name,
    DATE_TRUNC('month', resolution_date) AS month,
    SUM(
        CAST(fields['Unknowns'] ->> 'customfield_12310243' AS DECIMAL)
        ) AS total_story_points
FROM jira_issue
WHERE project_key = 'CCXDEV'
    AND status = 'Closed'
    AND LOWER(labels::TEXT)::jsonb ? 'ccx-processing'
GROUP BY assignee_display_name, month
HAVING EXTRACT(YEAR FROM DATE_TRUNC('month', resolution_date)) > 2000;
""",
        x="month",
        y="total_story_points",
        group_by="assignee_display_name",
        plot_fun=px.line),
]
