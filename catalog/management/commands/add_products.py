import json

from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test Products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('categories_fixture.json', 'r', encoding='utf-8') as file:
            categories_data = json.load(file)

        for cat_data in categories_data:
            category_fields = cat_data['fields']
            category, created = Category.objects.get_or_create(
                pk=cat_data['pk'],
                defaults=category_fields
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added category: {category_fields["name"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category already exists: {category_fields["name"]}'))

        with open('products_fixture.json', 'r', encoding='utf-8') as file:
            products_data = json.load(file)

        for product_data in products_data:
            product_fields = product_data['fields']

            category = Category.objects.get(pk=product_fields['category'])

            product_defaults = {
                'name': product_fields['name'],
                'description': product_fields['description'],
                'image': product_fields['image'],
                'price': product_fields['price'],
                'created_at': product_fields['created_at'],
                'updated_at': product_fields['updated_at'],
                'category': category
            }

            product, created = Product.objects.get_or_create(
                pk=product_data['pk'],
                defaults=product_defaults
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product_fields["name"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product_fields["name"]}'))