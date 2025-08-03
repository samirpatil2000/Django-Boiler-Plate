from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from account.models import Account
from account.serializers.register_serializer import AccountSerializer


class RegistrationAPIView(APIView):

    def get_object(self, user):
        try:
            return Account.objects.get(email=user)
        except Account.DoesNotExist:
            raise Http404

    def post(self, request):
        """
        Register a new user account
        Expected request body:
        {
            "email": "user@example.com",
            "password": "securepassword123",
            "password2": "securepassword123"
        }
        """
        try:
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                result = {
                    'status': status.HTTP_201_CREATED,
                    "message": "User registered successfully",
                    "data": {
                        "email": account.email,
                        "date_joined": account.date_joined
                    }
                }
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                result = {
                    'status': status.HTTP_400_BAD_REQUEST,
                    "message": "Registration failed",
                    "data": serializer.errors
                }
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
        except serializers.ValidationError as e:
            result = {
                'status': status.HTTP_400_BAD_REQUEST,
                "message": "Validation error",
                "data": e.detail if hasattr(e, 'detail') else str(e)
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            result = {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": str(e),
                "data": {}
            }
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            if not request.user.is_authenticated:
                result = {'status': status.HTTP_403_FORBIDDEN, "message": "Not Authenticated!", "data": {}}
                return Response(result)
            account = self.get_object(request.user)
            account_serializers = AccountSerializer(account)
            result = {'status': status.HTTP_200_OK, "message": "successfully register", "data": account_serializers.data}
        except Exception as e:
            result = {'status': status.HTTP_400_BAD_REQUEST, "message": str(e), "data":{}}
        return Response(result)

    def is_exists(self, email=None):

        if email and Account.objects.filter(email=email).exists():
            message = "Email already exists"
            return True, message

        return False, None