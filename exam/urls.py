from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.exam, name='exam'),
    path('data/', views.data, name='data'),
    path('upload/', views.upload, name='upload'),
    path('upload_topic', views.upload_topic, name='upload_topic'),
    path('upload_topic_success', views.upload_topic_success, name='upload_topic_success'),
    path('upload_topic_failed', views.upload_topic_failed, name='upload_topic_failed'),
    path('upload_topic_func', views.upload_topic_func, name='upload_topic_func'),
    path('upload_question', views.upload_question, name='upload_question'),
]