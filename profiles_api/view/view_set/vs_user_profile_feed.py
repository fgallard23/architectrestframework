from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # IsAuthenticatedOrReadOnly

from profiles_api.permission import p_update_own_status
from profiles_api.serializer.view_set import ss_profile_feed_item
from profiles_api.model import m_profile_feed_item


# replace GET / PUT / PATCH / PATCH / FILTER / create
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""

    # get all data class
    serializer_class = ss_profile_feed_item.ProfileFeedItemSerializer
    queryset = m_profile_feed_item.ProfileFeedItem.objects.all()
    # auth
    authentication_classes = (TokenAuthentication,)
    permission_classes = (p_update_own_status.UpdateOwnStatus, IsAuthenticated)

    # get master ID for child sequence for table
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        print(self.request.user)
        serializer.save(user_profile=self.request.user)
