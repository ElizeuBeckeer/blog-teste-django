from blog import views
from django.urls import path

app_name = 'blog'


#blog/ sendo incluso pela url do projeto
urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]

