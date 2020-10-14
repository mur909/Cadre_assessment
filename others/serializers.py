from rest_framework import serializers
from others.models import User
import hashlib


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        # fields = ['username', 'password', 'is_super']

    def create(self, validated_data):
        username = validated_data['username']
        pwd = validated_data['password']
        # is_super = validated_data['is_super']
        hash_pwd = hashlib.md5(pwd.encode()).hexdigest()
        # user_obj = User.objects.create(username=username, password=hash_pwd, is_super=is_super)
        user_obj = User.objects.create(username=username, password=hash_pwd)
        return user_obj