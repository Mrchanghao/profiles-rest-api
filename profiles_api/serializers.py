from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''
        serializers class a name field for testing hello Api view
    '''
    name = serializers.CharField(max_length=10)
