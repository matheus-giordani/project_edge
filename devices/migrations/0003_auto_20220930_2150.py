# Generated by Django 3.2.9 on 2022-10-01 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20220930_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='peaple',
        ),
        migrations.CreateModel(
            name='DevicesControl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.devices')),
                ('peaple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.peaple')),
            ],
        ),
    ]
