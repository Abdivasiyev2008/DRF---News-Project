from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostEditView

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('<int:pk>/edit/', PostEditView.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view()),
    path('create/', PostCreateView.as_view()),
]