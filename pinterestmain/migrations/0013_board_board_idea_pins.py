# Generated by Django 4.2 on 2023-08-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestmain', '0012_comment_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_idea_pins',
            field=models.ManyToManyField(related_name='boards', to='pinterestmain.ideapin'),
        ),
    ]
