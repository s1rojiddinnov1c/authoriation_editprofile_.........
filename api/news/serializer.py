from rest_framework import serializers
from .models import News, Category, Tag

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
     class Meta:
        model = Tag
        fields = '__all__'




