from django.urls import path
from . import views
from .views import AboutView, comment_like

app_name = 'home'

urlpatterns = [
    path('', AboutView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('work/', views.WorksView.as_view(), name='work'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('single-post/<int:pk>/', views.SinglePostView.as_view(), name='single-post'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<int:comment_id>/like/', comment_like, name='comment-like'),
]
