from django.conf.urls import url, include
from .views import CustomerCreate,CustomerList,CustomerSingle,CustomerUpdate,ProductInsert,CategoryInsert,ProductUpdate,MultiTabProCustInsert,MultiDataFetch, StateGetData, StateSaveData, StateSingleData


urlpatterns = [
    url('customer/create/', CustomerCreate.as_view(), name='create-customer'),
    url('list/', CustomerList.as_view()),
    # url('list/<int:pk>/', CustomerSingle.as_view(), name='retrieve-customer'),
    url(r'^list/(?P<pk>[0-9]+)/$', CustomerSingle.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', CustomerUpdate.as_view(), name='update-customer'),
    # path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
    url('category/insert/',CategoryInsert.as_view(),name='category-insert'),
    
    url('product/create/',ProductInsert.as_view(),name='create-product'),
    url(r'^product/update/(?P<pk>[0-9]+)/$',ProductUpdate.as_view(),name='update-product'),
    url('pro-cust/insert/',MultiTabProCustInsert.as_view(),name='product-customer-data-insert'),
    url('pro-cust/multiple_get_data/',MultiDataFetch.as_view(),name='multiple-data-details'),
    url('state/data-insert/',StateSaveData.as_view(),name='new-state-details-insert'),
    url('get/state-detaisl/',StateGetData.as_view(),name="get-state-details"),
    url(r'^state-single/(?P<pk>[0-9]+)/$',StateSingleData.as_view(),name="get-single-details-state")
    

]