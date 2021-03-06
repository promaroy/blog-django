from django.urls import path
from . import views
urlpatterns = [
    path('', views.postview,name='postview'),
    path('post/<int:post_id>',views.PostDetail,name='postdetail'),
    path('write',views.writepost,name='write'),
    path('login_view',views.login_view,name='login_view'),
    path('signup/',views.signup,name='signup/'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('blogs/search', views.blogbyauthor, name='blogbyauthor'),
]
