from django.db import models

class Department(models.Model):
    DeptID = models.AutoField(primary_key=True)
    DeptName = models.CharField(max_length=50)

    def __str__(self):
        return self.DeptName

class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=50)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.ProjectName

class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Projects = models.ManyToManyField(Project)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"