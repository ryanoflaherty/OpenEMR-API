from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        utc_now = timezone.now()

        if token.created < utc_now - timezone.timedelta(days=2):
            raise exceptions.AuthenticationFailed('Token has expired')

        return token.user, token
