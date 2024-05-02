from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user_control.models import User


class LoginView(APIView):
    @staticmethod
    def post(request):
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            user = User.objects.filter(email=email).first()
            if user:
                if user.check_password(password):
                    # Return whatever response you want for successful signin
                    return Response({'message': 'Signin successful'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
