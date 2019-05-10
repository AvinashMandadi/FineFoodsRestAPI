from django.conf.urls import url
from MyApi.views import RetrieveApiView, ListAndCreateApiView

urlpatterns = [
    url(r'^$', ListAndCreateApiView.as_view(), name='List-Api-View'),
    url(r'^(?P<pk>\d+)/$', RetrieveApiView.as_view(), name='Fine-Foods-View'),
]
