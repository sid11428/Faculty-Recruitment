# Generated by Django 4.1.2 on 2022-11-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_alter_application_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]