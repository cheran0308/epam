from rest_framework import serializers

from .models import Product, Issue, Metric, PIMRelation

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)

        instance.save()
        return instance


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

    def create(self, validated_data):
        return Metric.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

class PIRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PIMRelation
        fields = ('id', 'product', 'issue')

    def create(self, validated_data):
        return PIMRelation.objects.create(**validated_data)

class MIRelationSerializer(serializers.ModelSerializer):
    metric = serializers.StringRelatedField(read_only=True)
    issue = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PIMRelation
        fields = ('id', 'metric', 'issue')

    def create(self, validated_data):
        return PIMRelation.objects.create(**validated_data)

class PMRelationSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    metric = serializers.StringRelatedField()

    class Meta:
        model = PIMRelation
        fields = ('id', 'product', 'metric')

    def create(self, validated_data):
        return PIMRelation.objects.create(**validated_data)

class PISerializer(serializers.ModelSerializer):
    issue = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PIMRelation
        fields = ('id', 'issue')

class PMSerializer(serializers.ModelSerializer):
    metric = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PIMRelation
        fields = ('id', 'metric')

class MISerializer(serializers.ModelSerializer):
    issue = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PIMRelation
        fields = ('id', 'issue')
