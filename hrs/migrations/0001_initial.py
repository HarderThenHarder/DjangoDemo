# Generated by Django 2.2.6 on 2019-10-23 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('no', models.IntegerField(db_column='dno', primary_key=True, serialize=False, verbose_name='Dept No.')),
                ('name', models.CharField(db_column='dname', max_length=20, verbose_name='Dept Name.')),
                ('location', models.CharField(db_column='dlocation', max_length=10, verbose_name='Dept Location.')),
            ],
            options={
                'db_table': 'tb_dept',
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('no', models.IntegerField(db_column='eno', primary_key=True, serialize=False, verbose_name='Emp No.')),
                ('name', models.CharField(db_column='ename', max_length=20, verbose_name='Emp Name.')),
                ('job', models.CharField(db_column='ejob', max_length=10, verbose_name='Emp Job.')),
                ('sal', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Emp Salary.')),
                ('comm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Emp Subsidy')),
                ('dept', models.ForeignKey(db_column='dno', on_delete=django.db.models.deletion.PROTECT, to='hrs.Dept', verbose_name='Emp Dept')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrs.Emp', verbose_name='Emp Manager.')),
            ],
            options={
                'db_table': 'tb_emp',
            },
        ),
    ]