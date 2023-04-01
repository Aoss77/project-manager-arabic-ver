from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProjectStatus(models.IntegerChoices):
    Pending = 1, gettext('pending')
    Completed = 2, gettext('completed')
    Postponed = 3, gettext('postponed')
    Canceled = 4, gettext(' canceled')


class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(
        choices=ProjectStatus.choices,
        default=ProjectStatus.Pending,
    )
    created_Date = models.DateTimeField(auto_now_add=True)
    updated_Date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # one-to-many relation
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
