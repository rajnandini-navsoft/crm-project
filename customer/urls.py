from django.conf.urls import url, include
from .views import CustomerCreate,CustomerList,CustomerSingle,CustomerUpdate,ProductInsert,CategoryInsert,ProductUpdate


urlpatterns = [
    url('customer/create/', CustomerCreate.as_view(), name='create-customer'),
    url('list/', CustomerList.as_view()),
    # url('list/<int:pk>/', CustomerSingle.as_view(), name='retrieve-customer'),
    url(r'^list/(?P<pk>[0-9]+)/$', CustomerSingle.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', CustomerUpdate.as_view(), name='update-customer'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
    url('category/insert/',CategoryInsert.as_view(),name='category-insert'),
    url('product/create/',ProductInsert.as_view(),name='create-product'),
    url(r'^product/update/(?P<pk>[0-9]+)/$',ProductUpdate.as_view(),name='update-product')
]