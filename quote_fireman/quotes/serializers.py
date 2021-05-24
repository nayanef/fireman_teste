from rest_framework import serializers
from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=700, allow_blank=False)
    author = serializers.CharField(max_length=100, allow_blank=False)
    class Meta:
        model = Quote
        fields = ['text','author']