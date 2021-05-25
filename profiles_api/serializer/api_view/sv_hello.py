from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serializes a name file for testing our APIView
        is a feature from the django rest framework that allows you to easily convert
        data inputs into python and vice versa"""
    name = serializers.CharField(max_length=10)  # valid la len is max 10
