
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('addpost/',addpost,name='addpost'),
    path('editpost/<int:id>/',editpost,name='editpost'),
    path('deletepost/<int:id>/',deletepost,name='deletepost'),
    path('addcategory/',addcategory,name='addcategory'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logoutfun,name='logout'),
    path('category/<int:id>/',filterPost,name='category'),
    path('singlepost/<int:id>/',singlepost,name='singlepost'),
    path('search/',searchpost,name='search'),
    path('mypost/',mypost,name='mypost'),
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
