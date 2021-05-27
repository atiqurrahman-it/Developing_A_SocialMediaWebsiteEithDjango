"""Social_site_project URL Configuration
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from App_post import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('userApp.urls')),
    path('post/',include('App_post.urls')),
    path('',views.Homepage,name='homepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

