# Generated by Django 3.2.19 on 2023-06-06 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoyaltyTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('minimum_purchase', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('reward_points', models.PositiveIntegerField(default=0)),
                ('total_purchases', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loyalty_app.loyaltytier')),
            ],
        ),
    ]
