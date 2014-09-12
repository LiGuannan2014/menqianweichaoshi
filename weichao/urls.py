from django.conf.urls import patterns, include, url
from oscar.app import application
from weichao import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Examples:
    # url(r'^$', 'weichao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include(application.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^country/$',
        views.CountryList.as_view(),
        name='country-list'),
    url(r'^country/(?P<pk>[0-9]+)/$',
        views.CountryDetail.as_view(),
        name='country-detail'),

    url(r'^useraddress/$',
        views.UserAddressList.as_view(),
        name='useraddress-list'),
    url(r'^useraddress/(?P<pk>[0-9]+)/$',
        views.UserAddressDetail.as_view(),
        name='useraddress-detail'),

    url(r'^category/$',
        views.CategoryList.as_view(),
        name='category-list'),
    url(r'^category/(?P<pk>[0-9]+)/$',
        views.CategoryDetail.as_view(),
        name='category-detail'),

	url(r'^productclass/$',
        views.ProductClassList.as_view(),
        name='productclass-list'),
    url(r'^productclass/(?P<pk>[0-9]+)/$',
        views.ProductClassDetail.as_view(),
        name='productclass-detail'),

    url(r'^product/$',
        views.ProductList.as_view(),
        name='product-list'),
    url(r'^product/(?P<pk>[0-9]+)/$',
        views.ProductDetail.as_view(),
        name='product-detail')

)
