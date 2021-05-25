from rest_framework import serializers
from profiles_api.model import m_user_profile


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object
        is a feature from the django rest framework that allows you to easily convert
        data inputs into python and vice versa """

    class Meta:
        model = m_user_profile.UserProfile
        fields = ('id', 'email', 'name', 'last_login', 'password')  # fields validate
        extra_kwargs = {
            # special validate for hash password
            'last_login': {'read_only': True},
            'password': {'write_only': True}
        }

    # inheritance for ModelSerializer get data with POST
    def create(self, validated_data):
        """Create an return new user"""
        user = m_user_profile.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
