from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import RatingSerializer

from .models import Rating

class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if(self.request.method=='GET'):
            return []

        return [IsAuthenticated()]