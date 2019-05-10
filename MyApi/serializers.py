from MyApi.models import FineFoods

from rest_framework import serializers


class FineFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FineFoods
        fields = ['pk', 'productId', 'userId', 'profileName', 'helpfulness', 'review', 'review_time', 'review_summary', 'review_text']
