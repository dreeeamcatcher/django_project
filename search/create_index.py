# from django_elasticsearch_dsl import DocType, Index
# from django.core.management.base import BaseCommand, CommandError
# from ecomapp.models import Product, Category
# from elasticsearch import Elasticsearch
# from elasticsearch_dsl.connections import connections
#
# product = Index('products')
#
#
# @product.doc_type
# class ProductDocument(DocType):
#
#     class Meta:
#         model = Product
#         fields = [
#             'title',
#             'category',
#             'brand',
#             'price'
#         ]
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **kwargs):
#         es = Elasticsearch()
#         for p in Product.objects.all():
#             if p.category:
#                 slug = p.category.slug
#             else:
#                 continue
#             if p.title:
#                 title = p.title
#             else:
#                 title = ''
#             doc = {
#                 'title': title,
#                 'category': p.category,
#                 'brand': p.brand,
#                 'price': p.price
#              }
#             res = es.index(index=slug, doc_type='prod', id=p.slug, body=doc)
#             print('*********************')
#             print(res)
#             print('*********************')
