from rest_framework import serializers
from .models import LINKS

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = LINKS
        fields = ('_id', 'tag_name', 'tag_link', 'page_num')
