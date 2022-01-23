from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CommentCreateView, CommentDeleteView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),

    path('<int:blog_pk>/comments/create/',
         CommentCreateView.as_view(), name='comment_create'),
    path('<int:blog_pk>/comments/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment_delete'),
]
