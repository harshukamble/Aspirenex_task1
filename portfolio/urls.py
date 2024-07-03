from django.urls import path
from portfolio import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.handleblog,name='handleblog'),
    path('internshipdetails',views.internshipdetails,name='internshipdetails'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('skill/', views.skills_page, name='skills_page'),
    path('achievements/', views.achievements_page, name='achievements_page'),
    path('internship/', views.internship, name='internship'),
    path('certificates/', views.certificates, name='certificates'),
]
