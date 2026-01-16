from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'mahasiswa'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about'),  # ← BARU
    path('gallery/', views.gallery, name='gallery'),  # ← BARU
    path('login/', auth_views.LoginView.as_view(
        template_name='mahasiswa/registration/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='mahasiswa:home'
    ), name='logout'),
    path('register/', views.register, name='register'),
    path('mahasiswa/', views.mahasiswa_list, name='list'),
    path('mahasiswa/create/', views.mahasiswa_create, name='create'),
    path('mahasiswa/<int:pk>/', views.mahasiswa_detail, name='detail'),
    path('mahasiswa/<int:pk>/update/', views.mahasiswa_update, name='update'),
    path('mahasiswa/<int:pk>/delete/', views.mahasiswa_delete, name='delete'),
]