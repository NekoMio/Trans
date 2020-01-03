# Generated by Django 3.0 on 2020-01-03 07:20

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolFellow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('sex', models.CharField(max_length=1, verbose_name='性别')),
                ('tell', models.CharField(max_length=11, null=True, verbose_name='移动电话')),
                ('fixed_tell', models.CharField(max_length=12, null=True, verbose_name='固定电话')),
                ('email', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('department', models.CharField(max_length=100, verbose_name='院系')),
                ('school_class', models.CharField(max_length=30, null=True, verbose_name='班级')),
                ('education', models.CharField(max_length=50, verbose_name='学历')),
                ('year_system', models.CharField(max_length=30, null=True, verbose_name='学制')),
                ('year_enroll', models.IntegerField(verbose_name='入学年份')),
                ('year_graduate', models.IntegerField(verbose_name='毕业年份')),
                ('teacher', models.CharField(max_length=40, null=True, verbose_name='印象最深刻的辅导员老师')),
                ('mentor', models.CharField(max_length=40, null=True, verbose_name='印象最深刻的导师')),
                ('current_work_unit', models.CharField(max_length=100, verbose_name='现工作单位')),
                ('address_work_unit', models.CharField(max_length=200, null=True, verbose_name='现工作单位地址')),
                ('industry_category', models.CharField(max_length=20, null=True, verbose_name='行业类别')),
                ('unit_property', models.CharField(max_length=30, null=True, verbose_name='单位性质')),
                ('current_job_title', models.CharField(max_length=100, null=True, verbose_name='现职务职称')),
                ('honour', models.TextField(null=True, verbose_name='所获荣誉')),
                ('remark', models.TextField(null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '校友',
                'verbose_name_plural': '校友们',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True,
                                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                              verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('information', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  to='home.SchoolFellow', verbose_name='所关联的详细个人信息')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
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
