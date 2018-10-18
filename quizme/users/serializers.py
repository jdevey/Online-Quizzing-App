from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', 'password', 'macAddress')


    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return users