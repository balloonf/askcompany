from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.post_list, name="list"),
    path("post/<uuid:pk>/renew/", views.renew_post,
         name="renew-post"),
]
