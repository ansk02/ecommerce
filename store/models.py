from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
class Product(models.Model):
	product_name = models.CharField('Nom du produit', max_length=100, unique = True)
	slug = models.SlugField('slug', max_length=100, unique = True)
	description = models.TextField(max_length=500, blank=True)
	price = models.FloatField('Prix', default=0)
	images = models.ImageField(upload_to='photos/products')
	stock = models.IntegerField()
	is_available = models.BooleanField('Disponible ? ',default=True)
	category = models.ForeignKey( Category, on_delete=models.CASCADE)
	created_date = models.DateTimeField('Date d\'ajout', auto_now_add=True)
	modified_date = models.DateTimeField('Dernière modification', auto_now=True)


	class Meta:
		verbose_name = "Produit"
		verbose_name_plural = "Produits"

	def get_url(self):
		return reverse('store:product_detail', args=[self.category.slug, self.slug])


	def __str__(self):
		return self.product_name