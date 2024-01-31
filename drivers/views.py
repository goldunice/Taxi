from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response


class AllCarCategoryAPIView(APIView):
    def get(self, request):
        car_category = CarCategory.objects.all()
        serializer = CarCategorySerializer(car_category, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CarCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)


class CarCategoryAPIView(APIView):
    def get(self, request, pk):
        car_category = CarCategory.objects.get(id=pk)
        serializer = CarCategorySerializer(car_category)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = CarCategorySerializer(CarCategory.objects.get(id=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    def patch(self, request, pk):
        old = CarCategory.objects.get(id=pk)
        old_serializer = CarCategorySerializer(old)
        serializer = CarCategorySerializer(CarCategory.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Old": old_serializer.data,
                "New": serializer.data,
                "Status": status.HTTP_202_ACCEPTED
            })
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        serializer = CarCategorySerializer(CarCategory.objects.get(id=pk))
        CarCategory.objects.filter(id=pk).delete()
        return Response({
            "Deleted data": serializer.data,
            "success": "OK"
        })


class AllDriverAPIView(APIView):
    def get(self, request):
        driver = Driver.objects.all()
        serializer = DriverSerializer(driver, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors)


class DriverAPIView(APIView):
    def get(self, request, pk):
        car_category = Driver.objects.get(id=pk)
        serializer = DriverSerializer(car_category)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = DriverSerializer(Driver.objects.get(id=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    def delete(self, request, pk):
        serializer = DriverSerializer(Driver.objects.get(id=pk))
        Driver.objects.filter(id=pk).delete()
        return Response({
            "Deleted data": serializer.data,
            "success": "OK"
        })

    def patch(self, request, pk):
        old = Driver.objects.get(id=pk)
        old_serializer = DriverSerializer(old)
        serializer = DriverSerializer(Driver.objects.get(id=pk), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Old": old_serializer.data,
                "New": serializer.data,
                "Status": status.HTTP_202_ACCEPTED
            })
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
