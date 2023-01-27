from rest_framework import serializers
from event2all.models import User, Event, Quotation, Guest, ToDoList
from django.contrib.auth.hashers import make_password


# User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'birth_date', 'password', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validate_data):
            validate_data['password'] = make_password(validate_data['password'])

            return super(UserSerializer, self).create(validate_data)


# Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'place', 'name', 'date', 'managers', 'invite_number', 'event_budget', 'created_at',
                  'updated_at', 'user_id']


class ListEventsByUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


# Quotation

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'


# Guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


# ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'
