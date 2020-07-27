from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin

from users.serializer import AuthSerializer


class AuthCreateView(CreateModelMixin, GenericAPIView):
    serializer_class = AuthSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        return self.create(request)

