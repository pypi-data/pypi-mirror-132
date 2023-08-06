from .jwt import jwt_decode_user_key

from django.apps import apps
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

import jwt
import logging

logger = logging.getLogger(__file__)


class JWTAuthentication(BaseAuthentication):
    """
        class to obtain token from header if it is provided
        and verify if this is correct/valid token
    """

    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        payload = None
        if authorization_header.lower().startswith('bearer '):
            bearer, access_token, *extra_words = authorization_header.split(' ')
            if len(extra_words) > 0:
                raise exceptions.AuthenticationFailed("Improper structure of token")
            try:
                payload = jwt_decode_user_key(token=access_token)
            except jwt.DecodeError:
                raise exceptions.AuthenticationFailed('Error on decoding token')
            except jwt.ExpiredSignatureError:
                raise exceptions.AuthenticationFailed('Access_token expired')
            except IndexError:
                raise exceptions.AuthenticationFailed('Token prefix missing')
            user = None
            if payload:
                user_class = apps.get_model("core", "User")
                user = user_class.objects \
                    .filter(username=payload.get("username")) \
                    .only("i_user__private_key") \
                    .first()
            if user is None:
                raise exceptions.AuthenticationFailed('User inactive or deleted/not existed.')
            if not user.is_active:
                raise exceptions.AuthenticationFailed('User is inactive')
        else:
            raise exceptions.AuthenticationFailed("Missing 'Bearer' prefix")

        self.enforce_csrf(request)

        return user, None

    def enforce_csrf(self, request):
        return  # To not perform the csrf during checking auth header

