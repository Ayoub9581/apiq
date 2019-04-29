from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Comment
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .api.serializers import CommentSerializer

class CommentListView(ListView):
    model = Comment
    template_name = 'commentaire/commentaire_list.html'


class CommentDetailView(DetailView):
	model = Comment
	template_name = 'commentaire/commentaire_detail.html'