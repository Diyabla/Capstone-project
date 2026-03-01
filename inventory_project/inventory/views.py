from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryItem, InventoryChangeLog
from .serializers import InventoryItemSerializer, InventoryChangeLogSerializer, UserSerializer
from .permissions import IsOwner
# Create your views here.


class UserViewSet(ModelViewSet):
    query_set = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class InventoryViewSet(ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated , IsOwner]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name','quality','price','date_added']


    def get_queryset(self):
        queryset = InventoryItem.objects.filter(user=self.request.user)

        category = self.request.query_params.get('category')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        low_stock = self.request.query_params.get('low_stock')

        if category:
            queryset = queryset.filter(category=category)

        if min_price and max_price:
            queryset = queryset.filter(price_range = [min_price, max_price])

        if low_stock:
            queryset = queryset.filter(quantity__lt = low_stock)

        return queryset
    

    def perform_update(self, serializer):
        instance = self.get_object()
        old_quantity = instance.quantity
        updated_instance = serializer.save()


        if old_quantity != updated_instance.quantity:
            InventoryChangeLog.objects.create(
                item = updated_instance,
                changed_by = self.request.user,
                previous_quantity = old_quantity,
                new_quantity = updated_instance.quantity
            )



class ChangeLogViewSet(ReadOnlyModelViewSet):
    serializer_class = InventoryChangeLogSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return InventoryChangeLog.objects.filter(
            item__user = self.request.user
        )