from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    birth_date = models.DateField(max_length=30)
    password = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    place = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    date = models.DateField()
    managers = models.CharField(max_length=30)
    invite_number = models.IntegerField()
    event_budget = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.name
