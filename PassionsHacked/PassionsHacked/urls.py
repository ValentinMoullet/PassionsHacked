"""PassionsHacked URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Assemblage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^echo', views.echo, name='echo'),
    url(r'^$', views.index, name='index'),

    url(r'^register$', views.register, name='register'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^signtest$', views.signtest, name='signtest'),

    url(r'^getcountries$', views.get_countries, name='get_countries'),
    url(r'^create_group$', views.create_group, name='create_group'),
    url(r'^add_user_to_group$', views.add_user_to_group, name='add_user_to_group'),
    url(r'^get_users_from_group$', views.get_users_from_group, name='get_users_from_group'),
    url(r'^add_block_to_group$', views.add_block_to_group, name='add_block_to_group'),
    url(r'^get_blocks_from_group$', views.get_blocks_from_group, name='get_blocks_from_group')
]
