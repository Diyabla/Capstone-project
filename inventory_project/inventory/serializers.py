from rest_framework import serializers
from .models import InventoryItem, InventoryChangeLog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ['user','date_added','last_updated']


    def create(self,validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data)
    

class InventoryChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryChangeLog
        fields = "__all__"