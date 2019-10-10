from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory

from app import views


class TestIndex(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.Index.as_view()
        self.uri = '/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestProductViewGet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.ProductView.as_view()
        self.uri = '/products/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestIssueViewGet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.IssueView.as_view()
        self.uri = '/issues/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestMetricViewGet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MetricView.as_view()
        self.uri = '/metrics/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestProductIssuesGet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PIMRelationView.as_view({'get': 'get_product_issue'})
        self.uri = '/product_issues/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestMetricIssuesGet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PIMRelationView.as_view({'get': 'get_metric_issue'})
        self.uri = '/metric_issues/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestProductMetricGet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PIMRelationView.as_view({'get': 'get_product_metric'})
        self.uri = '/product_metrics/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestProductViewPost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.ProductView.as_view()
        self.uri = '/products/'

    def test_create(self):
        params = {
            "product" : {
                "title" : "test1",
                "description" : "test desc 1"
            }
        }
        request = self.factory.post(self.uri, params, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestIssueViewPost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.IssueView.as_view()
        self.uri = '/issues/'

    def test_create(self):
        params = {
            "issue" : {
                "title" : "test1",
                "category" : "test cat 1"
            }
        }
        request = self.factory.post(self.uri, params, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestMetricViewPost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MetricView.as_view()
        self.uri = '/metrics/'

    def test_create(self):
        params = {
            "metric" : {
                "title" : "test1",
                "description" : "test desc 1"
            }
        }
        request = self.factory.post(self.uri, params, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestProductIssuePost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PIMRelationView.as_view({'post': 'set_product_issue'})
        self.uri = '/set_product_issues/'

    def test_create(self):
        params = {
            "product_issue" : {
                "product" : 1,
                "issue" : 1
            }
        }
        request = self.factory.post(self.uri, params, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestProductMetricPost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PIMRelationView.as_view({'post': 'set_product_metric'})
        self.uri = '/set_product_metrics/'

    def test_create(self):
        params = {
            "product_metric" : {
                "product" : 1,
                "metric" : 1
            }
        }
        request = self.factory.post(self.uri, params, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


class TestMetricIssuePost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PIMRelationView.as_view({'post': 'set_metric_issue'})
        self.uri = '/set_metric_issues/'

    def test_create(self):
        params = {
            "metric_issue" : {
                "metric" : 1,
                "issue" : 1
            }
        }
        request = self.factory.post(self.uri, params, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
