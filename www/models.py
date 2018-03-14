from django.db import models
from datetime import date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    displayOrder = models.IntegerField(blank=True, null=False, default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering =['displayOrder','name']
        verbose_name_plural = 'categories'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField("Product Description",default="",blank=True)
    image = models.CharField("Full-size Image Path",null=True,default='/images/products/sample.jpg',blank=True,max_length=100)
    displayOrder = models.IntegerField(blank=True, null=False, default=0)
    def __str__(self):
        return self.name

    class Meta:
        ordering =['displayOrder','name']

class Model(models.Model):
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    model = models.CharField("Model Num.",max_length=200, unique=True)
    desc = models.TextField("Model Description",default="",blank=True)
    size = models.CharField(max_length=200,default="",blank=True)
    bikeCnt = models.IntegerField("Bikes",default=0,null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00, help_text="Enter 0 to display 'Call for Price' message instead of actual price.")
    price_change_date = models.DateField(default=date.today().strftime('%m/%d/%y'))


    class Meta:
        ordering =['product__category__displayOrder','model']

    def __str__(self):
        return self.model

def productSelect(prod_id=0):
    """ Return a dictionary with the Model records for a single Product or all Products """

    model_list = Model.objects.select_related().filter(active=True)
    if prod_id > 0 :
        model_list = model_list.filter(product__id=prod_id)
    else:
        # just return all active products for the Price List page
        pass

    return model_list

def navSetup():
    """Return a dictionary of Product lists and other details needed by the navigation template
        and the price list
    """
    from django.conf import settings
    mediaURL = settings.MEDIA_URL
    model_list = Product.objects.select_related()
    display_list = model_list.filter(category__name__istartswith="Display")
    parking_list = model_list.filter(category__name__istartswith="Parking")
    model_list = Model.objects.select_related().filter(active=True)
    effectiveDate = model_list.latest(field_name='price_change_date')
    effectiveDate = effectiveDate.price_change_date

    d = {'mediaURL': mediaURL, 'display_list':display_list, 
        'parking_list': parking_list, 'effectiveDate':effectiveDate}
    return  d
