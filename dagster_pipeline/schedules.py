# dagster_pipeline/schedules.py

from dagster import ScheduleDefinition
from .jobs import full_pipeline

daily_pipeline = ScheduleDefinition(
    job=full_pipeline,
    cron_schedule="0 1 * * *",  # every day at 1:00 AM
    name="daily_etl_job"
)
