from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('tag/some_tag/', views.tag, name='tag'),
    path('hot/', views.hot, name='hot'),
    path('question/1/', views.question, name='question'),
    path('ask/', views.ask, name='ask')
]
