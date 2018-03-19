from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    'serializers a name fields from testing out APIView'
    name = serializers.CharField(max_length=10)
    
