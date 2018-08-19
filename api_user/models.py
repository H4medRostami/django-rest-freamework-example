from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s: %s' % (self.name, self.lname)


class Major(models.Model):
    majors = models.ForeignKey(Student, related_name='major', on_delete=models.CASCADE ,null=True)
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s:' % (self.name)

class Hobi(models.Model):
    hobies = models.ForeignKey(Student,related_name='hobies', on_delete=models.CASCADE, null=True)
    hobi_name = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s:' % (self.hobi_name)

    def __str__(self):
        return self.hobi_name



