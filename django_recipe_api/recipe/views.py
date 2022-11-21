from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import RecipeSerializer  # import the serializer we just created
from .models import Recipe


# Create your views here.
class recipe_view_set(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    # define queryset
    queryset = Recipe.objects.all()
    print("queryset", queryset)
    # serializer_class = RecipeSerializer

