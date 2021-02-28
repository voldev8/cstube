# Generated by Django 3.1.6 on 2021-02-28 17:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20210226_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='videos',
            name='link',
            field=models.URLField(max_length=100),
        ),
    ]