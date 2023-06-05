"""django_st URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_st.views import ItemView, ElementsView, AddElementView, DeleteElementView, EditUserView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('delete_item', DeleteElementView.as_view()),
    path('writing_menu_db', AddElementView.as_view()),
    path('read_from_db', ItemView.as_view()),
    path('show_base_elements', ElementsView.as_view()),
    path('edit_user/<int:id>', EditUserView.as_view()),
    path('', ItemView.as_view())

]
