# Generated by Django 2.0.2 on 2018-03-04 08:44

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
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=10000)),
                ('completion_deadline', models.DateField(blank=True, null=True)),
                ('are_members_needed', models.BooleanField(default=True)),
                ('designer_needed', models.BooleanField(default=True)),
                ('developer_needed', models.BooleanField(default=True)),
                ('beginners_welcome', models.BooleanField(default=True)),
                ('complexity', models.CharField(max_length=200)),
                ('estimated_duration', models.IntegerField(max_length=200)),
                ('github_link', models.CharField(blank=True, max_length=200, null=True)),
                ('domains', models.ManyToManyField(to='app.Domain')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_owned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('is_developer_speciality', models.BooleanField(default=False)),
                ('is_designer_speciality', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('word', models.CharField(max_length=35)),
                ('slug', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_developer', models.BooleanField(default=False)),
                ('is_designer', models.BooleanField(default=False)),
                ('age', models.IntegerField(max_length=200)),
                ('interested_in_domains', models.ManyToManyField(null=True, to='app.Domain')),
                ('languages', models.ManyToManyField(blank=True, null=True, to='app.Language')),
                ('specialties', models.ManyToManyField(to='app.Speciality')),
                ('tools', models.ManyToManyField(blank=True, null=True, to='app.Tool')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='specialities_needed',
            field=models.ManyToManyField(to='app.Speciality'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='app.Tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(related_name='projects_involved_in', to=settings.AUTH_USER_MODEL),
        ),
    ]