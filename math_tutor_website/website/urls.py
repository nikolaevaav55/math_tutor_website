from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', WebsiteHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('program/<slug:program_slug>/', ShowProgram.as_view(), name='program'),
    path('nice_page/', nice_page, name='nice_page'),
    path('home/', home, name='home2'),
    path('category/<slug:cat_slug>/',  WebsiteCategory.as_view(extra_context={'title': "Список по категориям"}), name='category'),
]

