from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework import status
from lists.models import Movie


class ListView(APIView):

    def post(self, request):
        movie_serializer = MovieSerializer(data=request.data)

        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_200_CREATED)
        else:
            return Response(movie_serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def get(self, request,  **kwargs):
        if kwargs.get('movie_id') is None:
            movie_queryset = Movie.objects.all()
            movie_queryset_serializer = MovieSerializer(
                movie_queryset, many=True)
            return Response(movie_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            movie_id = kwargs.get('movie_id')
            movie_serializer = MovieSerializer(
                Movie.objects.get(id=movie_id))
            return Response(movie_serializer.data, status=status.HTTP_200_OK)
