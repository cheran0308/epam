from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import Product, Issue, Metric, PIMRelation
from .serializers import (ProductSerializer, IssueSerializer, 
						  MetricSerializer, PIRelationSerializer,
						  MIRelationSerializer, PMRelationSerializer,
						  PISerializer, PMSerializer, MISerializer)


class Index(APIView):
	'''
		This class is return Hello World on navigating to /
		Methods : get
	'''
	
	def get(self, request):
		content = {'message': 'Hello, World!'}
		return Response(content)


class ProductView(APIView):
	'''
		This class is used to run CRUD operation on product
	'''
	def get(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response({"products": serializer.data})

	def post(self, request):
		product = request.data.get('product')
		serializer = ProductSerializer(data=product)
		if serializer.is_valid(raise_exception=True):
			product_saved = serializer.save()
		return Response({"success": "Product '{}' created successfully".format(product_saved.title)})

	def put(self, request, pk):
		saved_product = get_object_or_404(Product.objects.all(), pk=pk)
		data = request.data.get('product')
		serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			product_saved = serializer.save()
		return Response({"success": "Product '{}' updated successfully".format(product_saved.title)})

	def delete(self, request, pk):
		product = get_object_or_404(Product.objects.all(), pk=pk)
		product.delete()
		return Response({"message": "Product with id `{}` has been deleted.".format(pk)},status=204)


class IssueView(APIView):
	'''
		This class is used to run CRUD operation on Issue
	'''
	def get(self, request):
		issues = Issue.objects.all()
		serializer = IssueSerializer(issues, many=True)
		return Response({"issues": serializer.data})

	def post(self, request):
		issue = request.data.get('issue')
		serializer = IssueSerializer(data=issue)
		if serializer.is_valid(raise_exception=True):
			issue_saved = serializer.save()
		return Response({"success": "Issue '{}' created successfully".format(issue_saved.title)})

	def put(self, request, pk):
		saved_issue = get_object_or_404(Issue.objects.all(), pk=pk)
		data = request.data.get('issue')
		serializer = IssueSerializer(instance=saved_issue, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			issue_saved = serializer.save()
		return Response({"success": "issue '{}' updated successfully".format(issue_saved.title)})

	def delete(self, request, pk):
		issue = get_object_or_404(Issue.objects.all(), pk=pk)
		issue.delete()
		return Response({"message": "Issue with id `{}` has been deleted.".format(pk)},status=204)


class MetricView(APIView):
	'''
		This class is used to run CRUD operation on Metric
	'''
	def get(self, request):
		metrics = Metric.objects.all()
		serializer = MetricSerializer(metrics, many=True)
		return Response({"metrics": serializer.data})

	def post(self, request):
		metric = request.data.get('metric')
		serializer = MetricSerializer(data=metric)
		if serializer.is_valid(raise_exception=True):
			metric_saved = serializer.save()
		return Response({"success": "Metric '{}' created successfully".format(metric_saved.title)})

	def put(self, request, pk):
		saved_metric = get_object_or_404(Metric.objects.all(), pk=pk)
		data = request.data.get('metric')
		serializer = MetricSerializer(instance=saved_metric, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			metric_saved = serializer.save()
		return Response({"success": "Metric '{}' updated successfully".format(metric_saved.title)})

	def delete(self, request, pk):
		metric = get_object_or_404(Metric.objects.all(), pk=pk)
		metric.delete()
		return Response({"message": "Metric with id `{}` has been deleted.".format(pk)},status=204)


class PIMRelationView(viewsets.GenericViewSet):
	'''
		This class is used to for mapping product, issue and metric
	'''
	@action(detail=True, methods=['get'])
	def get_product_issue(self, request):
		product_issues = PIMRelation.objects.filter(product__isnull=False, issue__isnull=False)
		serializer = PIRelationSerializer(product_issues, many=True)
		return Response({"products_issues" : serializer.data})

	@action(detail=True, methods=['get'])
	def get_metric_issue(self, request):
		metric_issues = PIMRelation.objects.filter(metric__isnull=False, issue__isnull=False)
		serializer = MIRelationSerializer(metric_issues, many=True)
		return Response({"products_issues" : serializer.data})

	@action(detail=True, methods=['get'])
	def get_product_metric(self, request):
		product_metrics = PIMRelation.objects.filter(product__isnull=False, metric__isnull=False)
		serializer = PMRelationSerializer(product_metrics, many=True)
		return Response({"products_issues" : serializer.data})

	@action(detail=True, method=['post'])
	def set_product_issue(self, request):
		product_issue = request.data.get('product_issue')
		serializer = PIRelationSerializer(data=product_issue)
		if serializer.is_valid(raise_exception=True):
			product_issue_saved = serializer.save()
		return Response({"success": "Product and Issue Maped successfully"})

	@action(detail=True, method=['post'])
	def set_product_metric(self, request):
		product_metric = request.data.get('product_metric')
		serializer = PMRelationSerializer(data=product_metric)
		if serializer.is_valid(raise_exception=True):
			product_metric_saved = serializer.save()
		return Response({"success": "Product and Metric Maped successfully"})

	@action(detail=True, method=['post'])
	def set_metric_issue(self, request):
		metric_issue = request.data.get('metric_issue')
		serializer = MIRelationSerializer(data=metric_issue)
		if serializer.is_valid(raise_exception=True):
			metric_issue_saved = serializer.save()
		return Response({"success": "Metric and Issue Maped successfully"})

	@action(detail=True, method=['delete'])
	def delete_pim(self, request, pk):
		pim_relation = get_object_or_404(PIMRelation.objects.all(), pk=pk)
		pim_relation.delete()
		return Response({"message": "id `{}` has been deleted.".format(pk)},status=204)

	@action(detail=True, methods=['get'])
	def get_issue_by_product(self, request, pk):
		product_issues = PIMRelation.objects.filter(product=pk, issue__isnull=False)
		serializer = PISerializer(product_issues, many=True)
		return Response({"product_id":pk,"issues" : serializer.data})

	@action(detail=True, methods=['get'])
	def get_metric_by_product(self, request, pk):
		product_metrics = PIMRelation.objects.filter(product=pk, metric__isnull=False)
		serializer = PMSerializer(product_metrics, many=True)
		return Response({"product_id":pk,"metrics" : serializer.data})

	@action(detail=True, methods=['get'])
	def get_issue_by_metric(self, request, pk):
		metric_issues = PIMRelation.objects.filter(metric=pk, issue__isnull=False)
		serializer = MISerializer(metric_issues, many=True)
		return Response({"metric_id":pk,"issues" : serializer.data})