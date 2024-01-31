from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema


class OperatorTokenAPIView(APIView):
    @swagger_auto_schema(request_body=CustomOperatorSerializer)
    def post(self, request):
        operator = CustomUser.objects.filter(
            username=request.data.get("username"),
            password=request.data.get("password"),
            role="operator"
        ).first()
        if operator is None:
            return Response({
                "xabar": "Operator topilmadi!"
            })
        refresh = RefreshToken.for_user(operator)
        resp = {
            "username": request.data.get("username"),
            "access": str(refresh.access_token),
            "refresh": str(refresh)

        }
        return Response(resp)


class DriverTokenAPIView(APIView):
    @swagger_auto_schema(request_body=CustomDriverSerializer)
    def post(self, request):
        driver = CustomUser.objects.filter(
            username=request.data.get("username"),
            role="driver"
        ).first()
        if driver is None:
            return Response({
                "xabar": "Haydovchi topilmadi!"
            })
        refresh = RefreshToken.for_user(driver)
        resp = {
            "username": request.data.get("username"),
            "access": str(refresh.access_token),
            "refresh": str(refresh)

        }
        return Response(resp)
