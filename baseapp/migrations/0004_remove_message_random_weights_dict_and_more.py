# Generated by Django 4.0.5 on 2022-09-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0003_alter_message_random_weights_dict'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='random_weights_dict',
        ),
        migrations.AddField(
            model_name='message',
            name='random_weights_text',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
