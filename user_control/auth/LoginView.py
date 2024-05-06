from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user_control.models import User


class LoginView(APIView):
    @staticmethod
    def post(request):
        try:
            if request.method == 'POST':
                email = request.data.get('email')
                password = request.data.get('password')
                user = User.objects.filter(email=email).first()
                if user:
                    if user.check_password(password):
                        # Generate JWT token
                        refresh = RefreshToken.for_user(user)
                        return Response({'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
                    else:
                        return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
