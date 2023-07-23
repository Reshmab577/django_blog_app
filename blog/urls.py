from django.urls import path
from .import views
urlpatterns = [
    #path('' ,views.home,name='blog'),
    path('' ,views.BlogListView.as_view(),name='blog'),
    path('about/',views.about,name='blog_about'),
    #  path('base/',views.base,name='basepage'),

]