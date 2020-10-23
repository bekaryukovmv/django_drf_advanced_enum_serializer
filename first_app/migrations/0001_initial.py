# Generated by Django 2.2 on 2020-10-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Undefined')], default='U', max_length=1)),
                ('age', models.IntegerField(default=0)),
                ('loyality', models.CharField(choices=[('PLATINUM', 'PLATINUM CARD'), ('GOLD', 'GOLDEN CARD'), ('SILVER', 'SILVER CARD')], default='SILVER', max_length=8)),
            ],
        ),
    ]
