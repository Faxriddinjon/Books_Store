from django.urls import path
from . import views


urlpatterns=[
    path('',views.firstPage, name="firstPage"),
    path('logup/', views.logup,name="logup"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('login/', views.logout, name="logout"),
    path('add-author/',views.AddAuthor, name="addAuthor"),
    path('add-book/',views.AddBook, name="addBook"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('purchases/', views.purchases, name="purchases"),
    path('author-books/<int:pk>', views.authorBooks, name="authorBooks")

]