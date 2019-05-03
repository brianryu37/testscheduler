from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    student_id = models.CharField(max_length = 20)

    #String Representation of Student
    def __str__(self):
        return self.student_name + " - " + self.student_id

class Instructor(models.Model):
    i_name = models.CharField(max_length = 40)
    i_id = models.CharField(max_length = 20)
    i_tenure = models.CharField(max_length = 3)

    def __str__(self):
        return self.i_name

class Course(models.Model):
    class_name = models.CharField(max_length = 50)
    class_id= models.CharField(max_length=8)
    instructor = models.ForeignKey(Instructor, on_delete = models.SET_NULL, 
    default = None, blank = True, null = True)

    def __str__(self):
        return self.class_name + " - " + str(self.instructor)
    class Meta:
        ordering = ('class_name',)