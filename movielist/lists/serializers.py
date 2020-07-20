from rest_framework import serializers
from .models import Movie

# serializer 작성 (추후 업데이트 필요)
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'