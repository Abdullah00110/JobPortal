# Generated by Django 5.0.6 on 2024-07-13 15:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('SSC', 'SSC'), ('HSC', 'HSC'), ('Graduation', 'Graduation'), ('Post Graduation', 'Post Graduation')], default='Graduation', max_length=30)),
                ('specialization', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=200)),
                ('board_or_university', models.CharField(max_length=100)),
                ('passing_year', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
