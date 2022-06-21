from django.urls import path

from Gestion_usuarios.views import show_user_posts_view,post_detail_view,post_delete_view

urlpatterns = [    
    path('show-user-posts/',show_user_posts_view,name='show_user_posts'),
    #Se deben invocar desde la view con los mismos nombres. En este caso pk y user_loged
    path('post-detail/<int:pk>/<str:user_loged>',post_detail_view,name='post_detail_view'),
    path('post-delete-view/<int:pk>/<str:user_loged>',post_delete_view,name ='post_delete_view'),    
]