from django.urls import path
from rest_framework.documentation import include_docs_urls

from .apiview import RegisterUser, PostList, PostDetail
from rest_framework.authtoken import views


urlpatterns = [
    path("login/", views.obtain_auth_token, name="login"),
    path("posts/", PostList.as_view(), name="posts_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="posts_detail"),
    path("register/", RegisterUser.as_view(), name="register"),
    path(r'docs/', include_docs_urls(title='Posts API')),
]
# path("login/", views.obtain_auth_token, name="login"),
