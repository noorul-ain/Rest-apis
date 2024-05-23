
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.UserList.as_view()),
    # path('', views.UserCreate.as_view()),
    # path('user/<int:pk>', views.UserRetrieve.as_view()),
    # path('user/<int:pk>', views.UserUpdate.as_view()),
    # path('user/<int:pk>', views.UserDelete.as_view()),
    # # combination 🔥
    # path('', views.UserListCreate.as_view()),
    # path('user/<int:pk>', views.UserRetriveUpdate.as_view()),
    # path('user/<int:pk>', views.UserRetriveDestroy.as_view()),
    path('user/<int:pk>', views.UserRetriveUpdateDestroy.as_view()),






]
