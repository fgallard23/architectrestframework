from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from profiles_api.permission import p_update_own_profile
from profiles_api.serializer.view_set import ss_user_profile
from profiles_api.model import m_user_profile


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    # get all data class
    serializer_class = ss_user_profile.UserProfileSerializer  # serialize class
    queryset = m_user_profile.UserProfile.objects.all() # all data
    # auth
    authentication_classes = (TokenAuthentication,)
    permission_classes = (p_update_own_profile.UpdateOwnProfile,) # update profile data
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
