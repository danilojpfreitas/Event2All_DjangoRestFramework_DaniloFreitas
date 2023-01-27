from rest_framework import serializers
from event2all.models import User, Event
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'birth_date', 'password', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validate_data):
            validate_data['password'] = make_password(validate_data['password'])

            return super(UserSerializer, self).create(validate_data)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'place', 'name', 'date', 'managers', 'invite_number', 'event_budget', 'created_at',
                  'updated_at', 'user_id']


class ListEventsByUserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
