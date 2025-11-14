from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index' ),
    path('about', views.about, name = 'about' ),
    path('contact', views.contact, name = 'contact' ),
    path('single_blog_page/<int:id>',views.single_blog_page,name = 'single_blog_page'),
    path('post_blog',views.post_blog,name = 'post_blog'),

    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]


from django.conf import settings
from django.conf.urls.static import static

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)