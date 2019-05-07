from django_elasticsearch_dsl import DocType, Index, fields
from ecomapp.models import Product, Category


product = Index('products')


@product.doc_type
class ProductDocument(DocType):

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
        ]
