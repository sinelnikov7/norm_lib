# Generated by Django 4.0.5 on 2022-06-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default=1, max_length=100, verbose_name='Пароль'),
            preserve_default=False,
        ),
    ]
