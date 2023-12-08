from django.contrib import admin
from django.urls import path

# imported views
from ai import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # configured the url
    path('',views.hello, name="hello"),
    path('home',views.home,name="home"),
    path('sentimentanalasis',views.sentimentanalasis,name="sentimentanalasis")
]
