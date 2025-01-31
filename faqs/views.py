from django.core.cache import cache
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')

        cache_key = f'faqs_{lang}'

        cached_faqs = cache.get(cache_key)

        if cached_faqs is not None:
            print("Cached FAQs:", cached_faqs)
            return cached_faqs

        faqs = FAQ.objects.all()

        cache.set(cache_key, faqs, timeout=60 * 15)  

        return faqs

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context