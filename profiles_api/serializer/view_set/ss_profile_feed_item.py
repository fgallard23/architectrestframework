from rest_framework import serializers
from profiles_api.model import m_profile_feed_item


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = m_profile_feed_item.ProfileFeedItem
        # always id first parameter
        # define model class ProfileFeedItem all fields need validated
        fields = ('id','user_profile','status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only':True}}
