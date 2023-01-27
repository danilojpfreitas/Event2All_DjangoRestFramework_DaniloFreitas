from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
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


class Quotation(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    contact = models.CharField(max_length=30)
    provider = models.CharField(max_length=30)
    expected_expense = models.IntegerField()
    actual_expense = models.IntegerField()
    amount_already_paid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)


class Guest(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    invite = models.BooleanField(default=False)
    isConfirmed = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)


class ToDoList(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    contact = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)