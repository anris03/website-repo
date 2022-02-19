from django.urls import path
from blog import views


urlpatterns=[
    path('add',views.blog_view,name='add'),
    path('categories',views.post_cat,name='categories'),
    path('draft',views.draft_posts,name='draft'),
    path('categories/<int:pk>',views.post_details, name='details'),
    path('myposts',views.doc_posts,name='myposts')
]