# Generated by Django 4.1.2 on 2022-12-10 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('verification', '0002_user_mobile_recived_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mobile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
