
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='приятность привычки')),
                ('frequency', models.PositiveIntegerField(default=1, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=250, null=True, verbose_name='вознаграждение')),
                ('eta', models.PositiveIntegerField(verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичность привычки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habit.habit', verbose_name='связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('action',),
            },
        ),
    ]