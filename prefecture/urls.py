from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("mypage/", views.mypage_view, name='mypage'),
    path("prefecture/<int:pk>/detail/", views.DetailPrefectureView.as_view(), name="prefecture-detail"),
    path("prefecture/register/", views.ResisterPrefectureView.as_view(), name="register-prefecture"),
    path("prefecture/<int:pk>/delete/", views.DeletePrefectureView.as_view(), name="delete-prefecture"),
    path("prefecture/<int:prefecture_id>/review/", views.CreateReviewView.as_view(), name="review"),
    path("review/<int:pk>/delete/", views.DeleteReviewView.as_view(), name="delete-review"),
    path("review/<int:pk>/update/", views.UpdateReviewView.as_view(), name="update-review"),
]
