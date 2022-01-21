from rest_framework import serializers


class PredictionSerializer(serializers.Serializer):
    result = serializers.IntegerField()
    #date = serializers.IntegerField()

class PredictionListSerializer(serializers.ListSerializer):
    child = PredictionSerializer()

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        # instance is the queryset, validated_data a list of dicts
