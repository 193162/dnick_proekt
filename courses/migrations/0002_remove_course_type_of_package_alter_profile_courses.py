# Generated by Django 4.0.4 on 2022-09-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='type_of_package',
        ),
        migrations.AlterField(
            model_name='profile',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='courses.course'),
        ),
    ]