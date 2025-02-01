# faqs/views.py
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faq_list_{lang}'
        
        # Try to get data from cache
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data
            
        # If not in cache, get from database and cache it
        queryset = super().get_queryset()
        cache.set(cache_key, queryset, timeout=60*15)
        return queryset