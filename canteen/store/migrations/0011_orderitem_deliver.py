# Generated by Django 3.1 on 2020-09-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20200925_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='deliver',
            field=models.BooleanField(default=False),
        ),
    ]
