from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Extracting the 'username' from the query parameters
        username = request.GET.get('username')
        
        # If no username is provided, return None to indicate no authentication
        if username is None:
            return None
        
        try:
            # Fetching the user from the database using the provided username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # If the user doesn't exist, raise an AuthenticationFailed exception
            raise AuthenticationFailed('No Such User')

        # Returning the user and None for authentication success
        return (user, None)
