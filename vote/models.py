from django.db import models

# Create your models here.
class Subject(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='Subject No.')
    name = models.CharField(max_length=20, verbose_name='Subject Name')
    intro = models.CharField(max_length=511, default='', verbose_name='Introduction')
    create_date = models.DateField(null=True, verbose_name='Create Date')
    is_hot = models.BooleanField(default=False, verbose_name='Hot Subject')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_subject'
        verbose_name = 'Subject'
        verbose_name_plural = 'Subject'


class Teacher(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='Teacher No.')
    name = models.CharField(max_length=20, verbose_name='Teacher Name')
    detail = models.CharField(max_length=1023, default='', verbose_name='Details')
    photo = models.CharField(max_length=1023, default='', verbose_name='Photo')
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT, db_column='sno', verbose_name='Teaching Subject')

    class Meta:
        db_table = 'tb_teacher'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teacher'