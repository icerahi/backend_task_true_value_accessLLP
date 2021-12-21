from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework import filters 

class CustomPagination(PageNumberPagination):
    page_size_query_param='limit'
    
class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends=[filters.OrderingFilter]
    ordering_fields="__all__"
    
    def get_queryset(self):
        queryset = User.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset=queryset.filter(
                Q(first_name__icontains=name)|
                Q(last_name__icontains=name))
        return queryset        
    
    def update(self, request, *args, **kwargs):
        partial = True # Here I change partial to True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)