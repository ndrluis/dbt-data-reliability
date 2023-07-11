from datetime import datetime

import dbt_project
from data_generator import DATE_FORMAT, generate_dates
from data_seeder import DbtDataSeeder


def test_table_volume_anomalies():
    table_name = "volume_anomalies"
    dbt_runner = dbt_project.get_dbt_runner()
    data = [
        {"updated_at": date.strftime(DATE_FORMAT)}
        for date in generate_dates(base_date=datetime.now())
    ]
    with DbtDataSeeder().seed_data(data, table_name):
        dbt_runner.test(
            vars={
                "table_name": table_name,
                "test_name": "elementary.volume_anomalies",
                "test_args": {
                    "timestamp_column": "updated_at",
                },
            }
        )
