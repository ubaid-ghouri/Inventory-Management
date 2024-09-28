# inventory/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cache_key = f"item_{item_id}"
        item = cache.get(cache_key)

        if not item:
            try:
                item = self.get_queryset().get(pk=item_id)
                cache.set(cache_key, item, timeout=60)  # Cache for 60 seconds
            except Item.DoesNotExist:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(item)
        return Response(serializer.data)

class ItemUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# inventory/views.py
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    # Optionally customize the token claims
    pass
