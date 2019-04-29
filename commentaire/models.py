from django.db import models



class Comment(models.Model):
	full_name = models.CharField(max_length=30,null=True,blank=True)
	email	  = models.EmailField()
	comment   = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

