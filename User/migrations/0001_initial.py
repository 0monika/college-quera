# Generated by Django 3.1.1 on 2021-06-04 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50, unique=True)),
                ('branch_slug', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100, unique=True)),
                ('user_password', models.CharField(max_length=20)),
                ('user_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('user_type', models.CharField(max_length=20)),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('verifyStatus', models.BooleanField(default=False)),
                ('user_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.branch')),
            ],
        ),
    ]
