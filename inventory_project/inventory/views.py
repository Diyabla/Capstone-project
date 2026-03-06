from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryItem, InventoryChangeLog
from .serializers import InventoryItemSerializer, InventoryChangeLogSerializer, UserSerializer
from .permissions import IsOwner
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from .forms import UserRegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
# Create your views here.

# def index(request):
#     return HttpResponse('This is the homepage')

def signup(request):

    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
        else:
            form = UserRegistrationForm()
        
    return render(request, 'signup.html', {'form':form})

   

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        
        if form.is_valid():
            username = form.get('username')
            password = form.get('password')

            user = authenticate(request, username = username, password = password),

            if user is not None:
                login(request,user)
                return redirect('profile')

    return render(request, 'login.html', {'form':form})


def profile_view(request):
    return render(request, 'profile.html')


def logout(request):
    logout(request)
    return redirect('login')




class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
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