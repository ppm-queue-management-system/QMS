# Generated by Django 3.0.4 on 2020-05-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0003_bookticketmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelTicketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=10)),
            ],
        ),
    ]
