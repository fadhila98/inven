# Generated by Django 3.2.7 on 2021-09-25 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0003_delete_productmovement'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('qty', models.IntegerField()),
                ('from_location', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='location-from+', to='locations.location')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('to_location', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='location-to+', to='locations.location')),
            ],
        ),
    ]
