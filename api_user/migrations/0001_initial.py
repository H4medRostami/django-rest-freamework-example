# Generated by Django 2.1 on 2018-08-19 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobi_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('hobies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_user.Hobi')),
                ('majors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_user.Major')),
            ],
        ),
    ]
