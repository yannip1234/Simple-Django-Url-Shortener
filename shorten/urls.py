from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:url_id>/", views.url_go, name='url_go')
    # path("result/", views.result, name="result")
]
