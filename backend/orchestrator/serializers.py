from rest_framework import serializers

class ValuationRequestSerializer(serializers.Serializer):
    revenue = serializers.FloatField()
    expenses = serializers.FloatField()
    growth_rate = serializers.FloatField()
    industry = serializers.CharField()