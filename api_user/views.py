
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from api_user.models import Student, Hobi
from api_user.serializers import StudentSerializer, HobiSerializer
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):

    throttle_classes = (UserRateThrottle,)

    def list(self, request):
        queryset = Student.objects.select_related()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=0):
        queryset = Student.objects.filter(id=pk)
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=0):
        user = Student.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        queryset = Student.objects.get(id=pk)
        serializer = StudentSerializer(queryset, data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HobiViewSet(viewsets.ViewSet):

    throttle_classes = (UserRateThrottle,)

    def list(self, request):
        queryset = Hobi.objects.all()
        serializer = HobiSerializer(queryset, many=True)
        return Response(serializer.data)