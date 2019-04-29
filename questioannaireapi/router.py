from commentaire.api.viewsets import CommentViewset,TemoignagesViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('commentaires', CommentViewset)
router.register('temoignages', TemoignagesViewset)