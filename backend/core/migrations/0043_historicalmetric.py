# Generated by Django 5.1.1 on 2024-11-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0042_asset_filtering_labels"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalMetric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(db_index=True, verbose_name="Date")),
                ("data", models.JSONField(verbose_name="Historical Data")),
                ("model", models.TextField(db_index=True, verbose_name="Model")),
                (
                    "object_id",
                    models.UUIDField(db_index=True, verbose_name="Object ID"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["model", "object_id", "date"],
                        name="core_histor_model_e05191_idx",
                    ),
                    models.Index(
                        fields=["date", "model"], name="core_histor_date_ddb7df_idx"
                    ),
                ],
                "unique_together": {("model", "object_id", "date")},
            },
        ),
    ]
