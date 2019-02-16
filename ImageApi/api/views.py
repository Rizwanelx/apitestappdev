from django.shortcuts import render
from ImageApi.api.serializers import MovieSerializer,  UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from ImageApi.api.models import Movie
from rest_framework.decorators import action
from django.contrib.auth.models import User


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(methods=['post'], detail=False)
    def upload_docs(request):
        try:
            file = request.data['file']
        except KeyError:
            response = {"message": "You need to pass all params"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
            product = Movie.objects.create(image=file)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer