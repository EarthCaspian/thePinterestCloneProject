# Generated by Django 4.2 on 2023-08-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestmain', '0006_alter_group_group_boards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pins', to='pinterestmain.board'),
        ),
    ]
