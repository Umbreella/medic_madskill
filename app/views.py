from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *


class NewModelViewSet(ModelViewSet):
    queryset = New.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = NewSerializer
    ordering = ('-id',)


class AnalysisModelViewSet(ModelViewSet):
    queryset = Analysis.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AnalysisSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('category',)
    search_fields = ('name',)
    ordering = ('-id',)


class PatientModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PatientSerializer
    ordering = ('last_name', 'first_name', 'middle_name',)

    def get_queryset(self):
        return Patient.objects.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        serializer = self.serializer_class(data=data, context={'user': user, })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        instance = self.get_object()
        serializer = self.serializer_class(instance, data=data,
                                           context={'user': user, })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class OrderModeViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    ordering = ('-id',)

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        serializer = self.serializer_class(data=data, context={'user': user, })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
