# Generated by Django 3.1.2 on 2020-10-11 00:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('class_name', models.CharField(choices=[('1', (('1А', '1А'), ('1Б', '1Б'), ('1В', '1В'), ('1Г', '1Г'), ('1Д', '1Д'))), ('2', (('2А', '2А'), ('2Б', '2Б'), ('2В', '2В'), ('2Г', '2Г'), ('2Д', '2Д'))), ('3', (('3А', '3А'), ('3Б', '3Б'), ('3В', '3В'), ('3Г', '3Г'), ('3Д', '3Д'))), ('4', (('4А', '4А'), ('4Б', '4Б'), ('4В', '4В'), ('4Г', '4Г'), ('4Д', '4Д'))), ('5', (('5А', '5А'), ('5Б', '5Б'), ('5В', '5В'), ('5Г', '5Г'))), ('6', (('6А', '6А'), ('6Б', '6Б'), ('6В', '6В'), ('6Г', '6Г'))), ('7', (('7А', '7А'), ('7Б', '7Б'), ('7В', '7В'), ('7Г', '7Г'))), ('8', (('8А', '8А'), ('8Б', '8Б'), ('8В', '8В'), ('8Г', '8Г'))), ('9', (('9А', '9А'), ('9Б', '9Б'), ('9В', '9В'), ('9Г', '9Г'))), ('10', (('10.1', '10.1'), ('10.2', '10.2'), ('10.3', '10.3'))), ('11', (('11.1', '11.1'), ('11.2', '11.2'), ('11.3', '11.3')))], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('subject', models.CharField(choices=[('Математические', (('Алгебра', 'Алгебра'), ('Геометрия', 'Геометрия'), ('Математика', 'Математика'), ('Информатика', 'Информатика'))), ('Гуманитарные', (('История', 'История'), ('Обществознание', 'Обществознание'))), ('Естественно-научные', (('Физика', 'Физика'), ('Химия', 'Химия'), ('География', 'География'), ('Астрономия', 'Астрономия'), ('Биология', 'Биология'), ('ОБЖ', 'ОБЖ'), ('Экология', 'Экология'))), ('Филологические', (('Русский язык', 'Русский язык'), ('Литература', 'Литература'), ('Иностранный язык', 'Иностранный язык'))), ('Искусство', (('Музыка', 'Музыка'), ('ИЗО', 'ИЗО'))), ('Физкультура', 'Физкультура')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(choices=[('1', (('1А', '1А'), ('1Б', '1Б'), ('1В', '1В'), ('1Г', '1Г'), ('1Д', '1Д'))), ('2', (('2А', '2А'), ('2Б', '2Б'), ('2В', '2В'), ('2Г', '2Г'), ('2Д', '2Д'))), ('3', (('3А', '3А'), ('3Б', '3Б'), ('3В', '3В'), ('3Г', '3Г'), ('3Д', '3Д'))), ('4', (('4А', '4А'), ('4Б', '4Б'), ('4В', '4В'), ('4Г', '4Г'), ('4Д', '4Д'))), ('5', (('5А', '5А'), ('5Б', '5Б'), ('5В', '5В'), ('5Г', '5Г'))), ('6', (('6А', '6А'), ('6Б', '6Б'), ('6В', '6В'), ('6Г', '6Г'))), ('7', (('7А', '7А'), ('7Б', '7Б'), ('7В', '7В'), ('7Г', '7Г'))), ('8', (('8А', '8А'), ('8Б', '8Б'), ('8В', '8В'), ('8Г', '8Г'))), ('9', (('9А', '9А'), ('9Б', '9Б'), ('9В', '9В'), ('9Г', '9Г'))), ('10', (('10.1', '10.1'), ('10.2', '10.2'), ('10.3', '10.3'))), ('11', (('11.1', '11.1'), ('11.2', '11.2'), ('11.3', '11.3')))], max_length=10)),
                ('subject', models.CharField(choices=[('Математические', (('Алгебра', 'Алгебра'), ('Геометрия', 'Геометрия'), ('Математика', 'Математика'), ('Информатика', 'Информатика'))), ('Гуманитарные', (('История', 'История'), ('Обществознание', 'Обществознание'))), ('Естественно-научные', (('Физика', 'Физика'), ('Химия', 'Химия'), ('География', 'География'), ('Астрономия', 'Астрономия'), ('Биология', 'Биология'), ('ОБЖ', 'ОБЖ'), ('Экология', 'Экология'))), ('Филологические', (('Русский язык', 'Русский язык'), ('Литература', 'Литература'), ('Иностранный язык', 'Иностранный язык'))), ('Искусство', (('Музыка', 'Музыка'), ('ИЗО', 'ИЗО'))), ('Физкультура', 'Физкультура')], max_length=50)),
                ('date_of_publication', models.DateField()),
                ('deadline', models.DateField()),
                ('task_text', models.TextField(max_length=10000)),
                ('fines_info', models.TextField(max_length=1000)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hwdesk.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='LoadTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision', models.TextField(max_length=10000)),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hwdesk.pupil')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hwdesk.task')),
            ],
        ),
        migrations.CreateModel(
            name='CheckTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=2)),
                ('comment', models.TextField(max_length=100)),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hwdesk.pupil')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hwdesk.task')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('type', models.CharField(choices=[('teacher', 'учитель'), ('pupil', 'ученик')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
