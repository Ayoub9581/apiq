from rest_framework import serializers
from commentaire.models import Comment


class  CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model  = Comment
		fields = ['full_name','email','comment', 'timestamp']