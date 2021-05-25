from django.db import models


class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)  # class name
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
