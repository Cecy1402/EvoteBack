from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('Evote.urls')),
    path('api/v1.0/', include('Users.urls')),


]