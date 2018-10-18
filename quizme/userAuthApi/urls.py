from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^users/register', 'userAuthAPI.views.create_auth'),
]