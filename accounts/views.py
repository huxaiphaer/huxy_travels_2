from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import exceptions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import UserSerializer
from accounts.utils import generate_access_token, generate_refresh_token


@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password = request.data.get('password')
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed(
            'username and password required')

    user = User.objects.filter(username=username).first()
    if user is None:
        raise exceptions.AuthenticationFailed('user not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('wrong password')

    serialized_user = UserSerializer(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': serialized_user,
    }

    return response


@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up_view(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password')
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
