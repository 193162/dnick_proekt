# Generated by Django 4.0.4 on 2022-09-04 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_type_of_package_alter_profile_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='videos',
        ),
    ]
