from  django.urls import path
#   .   代表在当前文件夹
from . import views

urlpatterns = [
    path('',views.index),#   空字符代表主页面
    path('new',views.new),
    path('info',views.info)

]