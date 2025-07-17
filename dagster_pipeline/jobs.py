# dagster_pipeline/jobs.py

from dagster import job
from .ops import scrape_telegram_data, load_raw_to_postgres, run_dbt_transformations, run_yolo_enrichment

@job
def full_pipeline():
    data = scrape_telegram_data()
    raw_loaded = load_raw_to_postgres(start_after=data)
    transformed = run_dbt_transformations(start_after=raw_loaded)
    run_yolo_enrichment(start_after=transformed)
