from commentaire.models import Comment
from myapp.models import Temoignages
from .serializers import CommentSerializer,TemoignageSerializer
from rest_framework import routers, serializers, viewsets



class CommentViewset(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class TemoignagesViewset(viewsets.ModelViewSet):
	queryset = Temoignages.objects.all()
	serializer_class = TemoignageSerializer