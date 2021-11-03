from . import views
from django.urls import path

urlpatterns = [
    path("", views.blogs, name="blogs"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", views.UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),

    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]