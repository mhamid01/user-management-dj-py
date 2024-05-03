from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user_control.serializers import CustomUserSerializer


class RegistrationView(APIView):
    @staticmethod
    def post(request):
        if request.method == 'POST':
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                # refresh_token = str(refresh)
                return Response({'token': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
