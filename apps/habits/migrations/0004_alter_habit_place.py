# Generated by Django 4.2.5 on 2023-09-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0003_alter_habit_eta_alter_habit_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.CharField(help_text='отвечает на вопрос где', max_length=50, verbose_name='место'),
        ),
    ]