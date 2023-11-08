from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='teacherpics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class Department(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Course(models.Model):
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    name=models.CharField(max_length=240)
    def __str__(self):
        return self.name





# class SubCourse(models.Model):
#     name=models.CharField(max_length=250)
#     department=models.ForeignKey(Department,on_delete=models.SET_NULL, blank=True, null=True)
#     course=models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
#     def __str__(self):
#         return self.name
