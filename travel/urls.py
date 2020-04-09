from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from register import views as v
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$', views.wt_home),

url('wt_home',views.wt_home),
url('home',views.home),
url('base',views.base),
url('add_place',v.add_place),
url(r'^register/', v.register,name = "register"),
path('', include("django.contrib.auth.urls")),
path('search/',views.search_titles,name = "search"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)