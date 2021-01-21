from django.urls import path
from . import views
urlpatterns = [
    path('jobs/<int:jobs_id>',views.jobs_view_detail),
    path('jobs',views.jobs_list_view),
    path('alljobs',views.home_view),
    path('',views.dashboard_view),
]