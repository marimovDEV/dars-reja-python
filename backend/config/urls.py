from django.contrib import admin
from django.urls import path
from lessons_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints matching frontend routes
    path('api/lessons', views.lessons_list),
    path('api/lessons/<str:lesson_id>', views.lesson_detail),
    path('api/lessons/<str:lesson_id>/status', views.update_status),

    # Group API endpoints
    path('api/groups', views.groups_list),
    path('api/groups/<str:group_id>', views.group_detail),
    path('api/groups/<str:group_id>/lessons', views.group_lessons),
    path('api/groups/<str:group_id>/lessons/<str:lesson_id>', views.update_group_lesson_progress),
    
    path('api/notion/status', views.notion_status),
    path('api/scrape', views.scrape_notion),
    path('api/notion/disconnect', views.notion_disconnect),
]
