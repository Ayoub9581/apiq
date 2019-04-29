from rest_framework import serializers
from commentaire.models import Comment
from myapp.models import Temoignages


class  CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model  = Comment
		fields = ['full_name','email','comment', 'timestamp']



class TemoignageSerializer(serializers.ModelSerializer):

	class Meta:
		model  = Temoignages
		fields = ('company_id','name',)