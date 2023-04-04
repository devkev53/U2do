# Generated by Django 3.2 on 2023-04-04 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0008_alter_todo_asigned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='styleworkspace',
            name='workspace',
        ),
        migrations.AddField(
            model_name='historicalworkspace',
            name='style',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workspaces.styleworkspace'),
        ),
        migrations.AddField(
            model_name='workspace',
            name='style',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='workspaces.styleworkspace'),
            preserve_default=False,
        ),
    ]
