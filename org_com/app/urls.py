from django.urls import path
from .views import Index, ProductView, IssueView, MetricView, PIMRelationView

urlpatterns = [
    path('', Index.as_view(), name="Index"),
    path('products/', ProductView.as_view(), name="Product"),
    path('products/<int:pk>', ProductView.as_view()),
    path('issues/', IssueView.as_view(), name="Issue"),
    path('issues/<int:pk>', IssueView.as_view()),
    path('metrics/', MetricView.as_view(), name="Metric"),
    path('metrics/<int:pk>', MetricView.as_view()),
    path('product_issues/', PIMRelationView.as_view({'get': 'get_product_issue'})),
    path('set_product_issues/', PIMRelationView.as_view({'post': 'set_product_issue'})),
    path('product_metrics/', PIMRelationView.as_view({'get': 'get_product_metric'})),
    path('set_product_metrics/', PIMRelationView.as_view({'post': 'set_product_metric'})),
    path('metric_issues/', PIMRelationView.as_view({'get': 'get_metric_issue'})),
    path('set_metric_issues/', PIMRelationView.as_view({'post': 'set_metric_issue'})),
    path('pim_relation/<int:pk>', PIMRelationView.as_view({'delete':'delete_pim'})),
    path('get_issue_by_product/<int:pk>', PIMRelationView.as_view({'get':'get_issue_by_product'})),
    path('get_metric_by_product/<int:pk>', PIMRelationView.as_view({'get':'get_metric_by_product'})),
    path('get_issue_by_metric/<int:pk>', PIMRelationView.as_view({'get':'get_issue_by_metric'}))
]