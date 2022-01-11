from .models import State
from rest_framework import serializers

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [
            'name',
            'code',
            'populations'
            ]

states = [
            'Malaysia',
            'Johor',
            'Kedah',
            'Kelantan',
            'Melaka',
            'Negeri Sembilan',
            'Pahang',
            'Pulau Pinang',
            'Perak',
            'Perlis',
            'Selangor',
            'Terengganu',
            'Sabah',
            'Sarawak',
            'W.P. Kuala Lumpur',
            'W.P. Labuan',
            'W.P. Putrajaya',
        ]
