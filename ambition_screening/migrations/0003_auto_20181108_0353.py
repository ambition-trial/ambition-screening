# Generated by Django 2.1.2 on 2018-11-08 01:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_screening', '0002_auto_20180706_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='history_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
