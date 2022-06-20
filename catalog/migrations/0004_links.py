# Generated by Django 4.0.5 on 2022-06-19 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_videos_admin_permission_alter_videos_type_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField(max_length=300)),
                ('type_video', models.CharField(blank=True, choices=[('Smoke', 'smoke'), ('Molly', 'molly'), ('Flash', 'flash'), ('Nade', 'grenade')], max_length=6)),
                ('site', models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('mid', 'Middle')], default='a', max_length=3)),
                ('map_belong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.maps')),
            ],
            options={
                'verbose_name': 'Link',
            },
        ),
    ]
