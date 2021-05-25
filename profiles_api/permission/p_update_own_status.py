from rest_framework import permissions


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users update their own states"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
