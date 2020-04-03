from rest_framework.views import APIView

from .serializer import UserSerializer


class SigninView(APIView):
    def post(self, request):
        is_valid