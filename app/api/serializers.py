from django.db import models
from django.db.models import fields
from app.models import Blog
from rest_framework import serializers

class BlogSerializer (serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'