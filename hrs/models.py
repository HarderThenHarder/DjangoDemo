from django.db import models

# Create your models here.
class Dept(models.Model):
    no = models.IntegerField(primary_key=True, db_column='dno', verbose_name='Dept No.')
    name = models.CharField(max_length=20, db_column='dname', verbose_name='Dept Name.')
    location = models.CharField(max_length=10, db_column='dlocation', verbose_name='Dept Location.')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_dept'

class Emp(models.Model):
    no = models.IntegerField(primary_key=True, db_column='eno', verbose_name='Emp No.')
    name = models.CharField(max_length=20, db_column='ename', verbose_name='Emp Name.')
    job = models.CharField(max_length=10, db_column='ejob', verbose_name='Emp Job.')
    # 多对一外键关联(自参照)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Emp Manager.')
    sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Emp Salary.')
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Emp Subsidy')
    # 多对一外键关联(参照部门模型)
    dept = models.ForeignKey(Dept, db_column='dno', on_delete=models.PROTECT, verbose_name='Emp Dept')
   
    def __str__(self):
       return self.name

    class Meta:
        db_table = 'tb_emp'
