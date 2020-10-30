from django.contrib.sitemaps.views import sitemap
from django.urls import path

from core import views
from core.sitemaps import PostSitemap

from .feeds import LatestPostsFeed

app_name = 'core'

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('search/', views.post_search, name='post_search'),
    path('feed/', LatestPostsFeed(), name='post_feed')
]
