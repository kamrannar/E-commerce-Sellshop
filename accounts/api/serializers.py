from rest_framework import serializers
from accounts.models import Newsletter,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class SubscriberEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('email',)