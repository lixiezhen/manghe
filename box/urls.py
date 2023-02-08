from django.urls import path
from . import views
app_name = 'box'
urlpatterns = [
    path('', views.head),
    path('search/', views.search,name='search'),
    path('woman/',views.woman_box,name='woman'),
    path('man/',views.man_box,name='man'),
    path('collect/', views.collect,name='collect'),
    path('comment_control/',views.comment_control),
    path('put-list/', views.put,name='put_list'),
    path('random-list/', views.random_list,name='random_list'),
    path('edit-box/',views.edit_box,name='edit_box'),
    path('delete-box/',views.delete_box,name='delete_box'),
    path('delete/<int:box_id>/',views.delete_cltbox,name='delete_cltbox'),
    path('woman/<int:box_id>/',views.woman_intro,name='woman_intro'),
    path('woman-image/',views.woman_image,name='woman_image'),
    path('woman-random',views.woman_random,name='woman_random'),
    path('woman-put/',views.woman_put,name='woman_put'),
    path('woman-collection/',views.woman_collection,name='woman_collection'),
    path('woman/<int:box_id>/<int:pk>/',views.collect_woman_box,name='collect_woman_box'),
    path('man/<int:box_id>/',views.man_intro,name='man_intro'),
    path('man-image/',views.man_image,name='man_image'),
    path('man-random',views.man_random,name='man_random'),
    path('man-put/',views.man_put,name='man_put'),
    path('man-collection/',views.man_collection,name='man_collection'),
    path('man/<int:box_id>/<int:pk>/',views.collect_man_box,name='collect_man_box'),

]
