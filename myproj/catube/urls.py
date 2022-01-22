from django.urls import path
from .views import VideoListView, VideoDetailView, VideoCreateView, VideoUpdateView, VideoDeleteView, CommentCreateView, CommentDeleteView

app_name = "catube"

urlpatterns = [
    path("", VideoListView.as_view(), name="video_list"),
    path("create/", VideoCreateView.as_view(), name="video_create"),
    path("<int:pk>/", VideoDetailView.as_view(), name="video_detail"),
    path("<int:pk>/update/", VideoUpdateView.as_view(), name="video_update"),
    path("<int:pk>/delete/", VideoDeleteView.as_view(), name="video_delete"),

    path('<int:video_pk>/comments/create/',
         CommentCreateView.as_view(), name='comment_create'),
    path('<int:video_pk>/comments/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment_delete'),
]
