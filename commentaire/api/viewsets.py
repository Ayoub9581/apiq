from commentaire.models import Comment
from .serializers import CommentSerializer
from rest_framework import routers, serializers, viewsets



class CommentViewset(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer