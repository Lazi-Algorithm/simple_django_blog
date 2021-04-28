from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, AddCommentView, PasswordsChangeView,password_success, UserRegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('article/<int:pk>', PostDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('password_change/', PasswordsChangeView.as_view(), name="password_change" ),
    path('password_success/', password_success, name='password_success'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    # path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]

