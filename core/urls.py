from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .feeds import LatestPostsFeed

from core.sitemaps import PostSitemap
from core import views


app_name = 'core'

sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'), 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
    path('fedd/', LatestPostsFeed(), name='post_feed')
] 
