from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class AllOperatorAPIView(APIView):
    def get(self, request):
        operator = Operator.objects.all()
        serializer = OperatorSerializer(operator, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = OperatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)


class OperatorAPIView(APIView):
    def get(self, request, pk):
        operator = Operator.objects.get(id=pk)
        serializer = OperatorSerializer(operator)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = OperatorSerializer(Operator.objects.get(id=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    def delete(self, request, pk):
        serializer = OperatorSerializer(Operator.objects.get(id=pk))
        Operator.objects.filter(id=pk).delete()
        return Response({
            "Deleted data": serializer.data,
            "success": "OK"
        })

    def patch(self, request, pk):
        old = Operator.objects.get(id=pk)
        old_serializer = OperatorSerializer(old)
        serializer = OperatorSerializer(Operator.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Old": old_serializer.data,
                "New": serializer.data,
                "Status": status.HTTP_202_ACCEPTED
            })
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class AllClientAPIView(APIView):
    def get(self, request):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)


class ClientAPIView(APIView):
    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = ClientSerializer(Client.objects.get(id=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    def delete(self, request, pk):
        serializer = ClientSerializer(Client.objects.get(id=pk))
        Client.objects.get(id=pk).delete()
        return Response({
            "Deleted data": serializer.data,
            "success": "OK"
        })

    def patch(self, request, pk):
        old = Client.objects.get(id=pk)
        old_serializer = ClientSerializer(old)
        serializer = ClientSerializer(Client.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Old": old_serializer.data,
                "New": serializer.data,
                "Status": status.HTTP_202_ACCEPTED
            })
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class AllOrderAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     order = Order.objects.all()
    #     serializer = OrderSerializer(order, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(status="active")
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "order_group",
                {
                    "type": "add_new_order",
                },
            )
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class OrderAPIView(APIView):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = OrderSerializer(Order.objects.get(id=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    def delete(self, request, pk):
        serializer = OrderSerializer(Order.objects.get(id=pk))
        Order.objects.filter(id=pk).delete()
        return Response({
            "Deleted data": serializer.data,
            "success": "OK"
        })

    def patch(self, request, pk):
        old = Order.objects.get(id=pk)
        old_serializer = OrderSerializer(old)
        serializer = OrderSerializer(Order.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Old": old_serializer.data,
                "New": serializer.data,
                "Status": status.HTTP_202_ACCEPTED
            })
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
