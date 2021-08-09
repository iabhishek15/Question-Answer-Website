"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages.views import home_page_view, add_question_view, question_edit_view
from question_page.views import question_view, testing_view
from log_sign.views import sign_up_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name = "home"),
    path('login/', login_view),
    path('signup/', sign_up_view, name = "signup"),
    path('new-question/', add_question_view),
    path('<int:id>/', question_view, name = "question_view"),
    path('edit/<int:id>/', question_edit_view),
    path('testing/',testing_view),
    path('logout/',logout_view),
]
