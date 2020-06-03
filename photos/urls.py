from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

# urlpatterns = [
#     url(r'^signup', views.signup, name='signup'),
#     url(r'', views.index, name='home'),
#     url(r'^login', LoginView.as_view(), name='login_url'),
#     url(r'^logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
#     url(r'^newpost/', views.new_post, name='new_post'),
#     url(r'^profile/', views.profile, name='profile'),
#     url(r'^updateprofile/', views.update_profile, name='update_profile'),
# ]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)