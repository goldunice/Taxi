from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response


class AllPaymentAPIView(APIView):
    def get(self, request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)


class PaymentAPIView(APIView):
    def get(self, request, pk):
        payment = Payment.objects.get(id=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = PaymentSerializer(Payment.objects.get(id=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    def delete(self, request, pk):
        serializer = PaymentSerializer(Payment.objects.get(id=pk))
        Payment.objects.filter(id=pk).delete()
        return Response({
            "Deleted data": serializer.data,
            "success": "OK"
        })

    def patch(self, request, pk):
        old = Payment.objects.get(id=pk)
        old_serializer = PaymentSerializer(old)
        serializer = PaymentSerializer(Payment.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Old": old_serializer.data,
                "New": serializer.data,
                "Status": status.HTTP_202_ACCEPTED
            })
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
