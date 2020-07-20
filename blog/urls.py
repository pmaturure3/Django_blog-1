from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('blog', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('contact', views.contact, name='contact'),

    path('about', views.about, name='about'),
] 
