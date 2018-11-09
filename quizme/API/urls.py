from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.UserList.as_view()),
    #path('<int:pk>/', views.UserDetail.as_view()),
    path('', views.GameList.as_view()),
    path('<int:pk>/', views.GameDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('game/<int:pk>/', views.QuestionList.as_view()),

]
