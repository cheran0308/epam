from django.db import models

class Product(models.Model):

    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Issue(models.Model):

    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Metric(models.Model):

	title = models.CharField(max_length=50, unique=True)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class PIMRelation(models.Model):

	product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
	issue = models.ForeignKey(Issue, null=True, on_delete=models.CASCADE)
	metric = models.ForeignKey(Metric, null=True, on_delete=models.CASCADE)
