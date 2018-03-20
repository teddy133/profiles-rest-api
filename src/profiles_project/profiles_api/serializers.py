from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    'serializers a name fields from testing out APIView'
    name = serializers.CharField(max_length=10)

class userProfileSerializer(serializers.ModelSerializer):
    ''' a serializer to '''
    class Meta():
        fields = ('id', 'email','name','password')
        model = models.UserProfile
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        '''create and return a new user'''
        user = models.UserProfile(email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()

        return user
