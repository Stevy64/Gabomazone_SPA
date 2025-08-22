# store/views_auth.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers_auth import RegisterCustomerSerializer, RegisterVendorSerializer

class RegisterCustomerView(APIView):
    """POST /api/auth/register/customer/ — Création compte client"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        ser = RegisterCustomerSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        return Response({"id": user.id, "username": user.username}, status=status.HTTP_201_CREATED)


class RegisterVendorView(APIView):
    """POST /api/auth/register/vendor/ — Création compte vendeur (+ Seller)"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        ser = RegisterVendorSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        return Response({"id": user.id, "username": user.username, "seller": True}, status=status.HTTP_201_CREATED)
