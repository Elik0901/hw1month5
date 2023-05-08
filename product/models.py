from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=200)
class Category(models.Model):
    name = models.CharField(max_length=35)

    @property
    def products_count(self):
        return self.product_set.count()

    def products_list(self):
        return [product.title for product in self.product_set.all()]

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    @property
    def category_name(self):
        try:
            return self.category.name
        except:
            return 'нет категорий'

    def rating(self):
        stars_list = [review.stars for review in self.reviews.all()]
        return round(sum(stars_list)/ len(stars_list), 2)

    def __str__(self):
        return self.title


class Review(models.Model):
    CHOICES = ((i, "*"* i) for i in range(1,6))
    text = models.TextField(max_length=300)
    stars = models.IntegerField(choices=CHOICES, default=0)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    @property
    def product_title(self):
        return self.product.title

    def __str__(self):
        return self.text
