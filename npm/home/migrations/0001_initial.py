# Generated by Django 3.2.6 on 2021-09-14 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('screenshot', models.ImageField(default='https://via.placeholder.com/500x500.png?text=Default', upload_to='contact\\images')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
