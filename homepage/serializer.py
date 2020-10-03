from rest_framework import serializers
from homepage.models import boast, roast

class BoastSerializer(serializers.ModelSerializer):
    class Meta:
        model =  boast
        fields = [
            'content',
            'upvotes',
            'downvotes',
            'posted_at',
        ]


class RoastSerializer(serializers.ModelSerializer):
    class Meta:
        model =  roast
        fields = [
            'content',
            'upvotes',
            'downvotes',
            'posted_at',
        ]