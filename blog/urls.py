from django.urls import path, include

from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.all_blogs, name='all_blogs'),
    # looks for an int after blog. call it blog_id
    path('<int:blog_id>', views.detail, name='detail')

]
