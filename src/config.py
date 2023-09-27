"""Configuration variables."""
import os


QUERY_TIMEOUT_SECONDS = int(os.getenv("QUERY_TIMEOUT_SECONDS", "60"))
DB_NAME = os.getenv("DB_NAME", "steampipe")
DB_PASSWORD = os.getenv("STEAMPIPE_DATABASE_PASSWORD", "")
DB_USER = os.getenv("DB_USER", "steampipe")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "9193")
