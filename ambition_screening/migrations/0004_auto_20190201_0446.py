# Generated by Django 2.1.5 on 2019-02-01 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("ambition_screening", "0003_auto_20181108_0353")]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.Site",
            ),
        )
    ]
