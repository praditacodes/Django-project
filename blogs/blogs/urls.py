from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('blog/', views.hello_blog),
    path('blogs/', include('app1.urls')), 
    # path('tourist/', include('tourist.urls')), # Include app1's urls
    # path('author/',include('author.py')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
