# Generated by Django 3.2.4 on 2021-10-27 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
        ('genie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebookrunlogs',
            name='workspace',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='workspace.workspace'),
        ),
    ]
