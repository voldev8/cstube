# Generated by Django 3.1.6 on 2021-02-18 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210217_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='site',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('mid', 'Middle')], default='a', help_text='Site availability', max_length=3),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
