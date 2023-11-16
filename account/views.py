from rest_framework import status
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.response import Response
from .serializers import UserSignupSerializer,UserSigninSerializer
class UserSignupView(CreateAPIView):

    def post(self, request):
        data = request.data
        serializer = UserSignupSerializer(data=data)

        try:

            if not serializer.is_valid():
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    'success': False,
                    'status code': status_code,
                    'message': serializer.errors
                }
            else:
                user = serializer.save()
                status_code = status.HTTP_201_CREATED
                response = {
                    'success': True,
                    'status code': status_code,
                    'message': 'User registered  successfully',
                    'user_profile': {
                        "user_id": user.user_id,
                        "name": serializer.data['name'],
                        "email": serializer.data['email']
                    }
                }

        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = {
                'success': False,
                'status code': status_code,
                'message': 'Something went wrong, Please try again.',
                'error': str(error),
            }
        return Response(response, status=status_code)


class UserSigninView(RetrieveAPIView):
    def post(self, request):
        print(request.data)
        serializer = UserSigninSerializer(data=request.data)
        response = Response()

        try:

            if not serializer.is_valid():
                status_code = status.HTTP_400_BAD_REQUEST
                response.status_code = status_code
                response.data = {
                    'success': False,
                    'status code': status_code,
                    'message': 'Your entered credentials are not correct, please try again',
                }
            else:

                status_code = status.HTTP_200_OK
                response.data = {
                    'success': True,
                    'status code': status_code,
                    'message': 'User logged in  successfully',
                    'user_profile': serializer.data,
                }
                response.status_code = status_code
        except Exception as e:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response.data = {
                'success': False,
                'status code': status_code,
                'message': "Something went wrong, please try again.",
                "details": str(e),
            }
            response.status_code = status_code

        return response