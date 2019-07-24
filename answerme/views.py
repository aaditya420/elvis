from rest_framework import viewsets
from .serializers import LinksSerializer
from .models import LINKS


class LinksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LINKS.objects.filter(page_num='4')
    serializer_class = LinksSerializer
