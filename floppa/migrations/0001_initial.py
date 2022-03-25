# Generated by Django 3.1 on 2022-03-25 11:19

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
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('postcode', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Necklace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('colour', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=4)),
                ('stock', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('image1', models.ImageField(blank=True, max_length=255, null=True, upload_to='necklacePictures/')),
                ('image2', models.ImageField(blank=True, max_length=255, null=True, upload_to='necklacePictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed', models.BooleanField(default=False)),
                ('userID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='floppa.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Necklace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('necklaceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floppa.necklace')),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floppa.order')),
            ],
        ),
    ]
