from django.urls import path
from django.views.generic import TemplateView

from web.views import HomePageView, PostDetailView, ApplicationCreateView


app_name = "web"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post"),
    path('apply/', ApplicationCreateView.as_view(), name='application_form'),
    path('status/', TemplateView.as_view(template_name='web/application_status.html'), name='application_status'),
]
