from django.contrib import admin
from profiles_api.model import m_user_profile
from profiles_api.model import m_profile_feed_item

# activate user interface
admin.site.register(m_user_profile.UserProfile)
admin.site.register(m_profile_feed_item.ProfileFeedItem)
