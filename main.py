from pprint import pprint

from db.models import *

products = Products.objects.filter(publisher__title='Nintendo').values('title','price').all()
pprint(products)