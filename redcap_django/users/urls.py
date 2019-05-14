from django.urls import path

from redcap_django.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    UserDetailAPIView)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:id>/", view=user_detail_view, name="detail"),
    path("detail/", view=UserDetailAPIView.as_view(), name="detail_api"),
]
