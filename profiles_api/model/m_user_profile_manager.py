from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email), # normalize el email a lowercase
            name=name,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)  # standard procedure

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""

        # Create a new user with the function we created above.
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)  # standard procedure

        return user

