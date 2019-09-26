from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('login_system/', include('login_module.urls')),
  path('admin/', admin.site.urls),
]
