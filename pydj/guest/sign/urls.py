from django.conf.urls import url
from sign import views_if
app_name='[sign]'
urlpatterns = [
# guest system interface:
# ex : /api/add_event/
url(r'^add_event/', views_if.add_event, name='add_event'),
url(r'^add_guest/', views_if.add_guest, name='add_guest'),
url(r'^get_event_list/', views_if.get_event_list, name='get_event_list'),
url(r'^get_guest_list/', views_if.get_guest_list, name='get_guest_list'),

        ]