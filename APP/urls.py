from django.urls import path

from .views import (AddPostCategory, AddPostView, ArticleDetailView,
                    AuthorView, CategoryListView, CategoryView, DeletePostView,
                    HomeView, UpdatePostView)

# from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>',
         ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='article_update'),  # noqa: E501
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='article_delete'),  # noqa: E501
    path('category/', AddPostCategory.as_view(), name='category'),  # noqa: E501
    path('category/<str:cats>/', CategoryView, name='category'),  # noqa: E501
    path('category-list/', CategoryListView, name='category-list'),  # noqa: E501
    path('authors/<str:aut>/', AuthorView, name='authors'),  # noqa: E501


]
