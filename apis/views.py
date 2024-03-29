from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt import views as jwt_views
from .serializers import TokenObtainPairSerializer, UserInfoSerializer

# Create your views here.


class HelloView(APIView):

    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class TokenObtainPairView(jwt_views.TokenViewBase):
    serializer_class = TokenObtainPairSerializer


class UserInfoData(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = UserInfoSerializer
