# Generated by Django 4.2.7 on 2023-11-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0002_tarefa_data_tarefa_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='hora',
            field=models.TimeField(blank=True, null=True),
        ),
    ]