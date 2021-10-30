# Generated by Django 3.2.4 on 2021-10-26 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=200, null=True)),
                ('label', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(default='text', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AccountSettingValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True)),
                ('accountSetting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.accountsetting')),
            ],
        ),
    ]
