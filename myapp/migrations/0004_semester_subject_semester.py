# Generated by Django 4.2.8 on 2023-12-04 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_subject_course_subject_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.ManyToManyField(to='myapp.semester'),
        ),
    ]
