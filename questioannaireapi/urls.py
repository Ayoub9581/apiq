
from django.contrib import admin
from django.urls import path,include
from .router import router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('commentaire/', include('commentaire.urls', namespace='commentaire')),
    path('api/', include(router.urls), name='api')
]
