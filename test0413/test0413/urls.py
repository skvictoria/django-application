from django.conf.urls import include, url
from django.contrib import admin
from test0413 import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'test0413.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', views.test),
]
