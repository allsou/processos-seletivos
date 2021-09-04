from mongoengine import Document

from entities.customer import Customer
from entities.product import Product
from exceptions.general import NotFoundException
from settings import LOGGER

LIMIT_PER_PAGE = 10


class Database:
    def save(self, document: Document) -> Document:
        LOGGER.debug('Persisting document')
        document.save()
        return document

    def get_product_by_id(self, product_id: str) -> Product:
        LOGGER.debug(f'Getting product {product_id} in database')
        product = Product.objects(id=product_id).first()  # pylint: disable=no-member
        if not product:
            LOGGER.debug('None product found to product_id informed')
            raise NotFoundException
        return product

    def get_customer_by_id(self, customer_id: str) -> Customer:
        LOGGER.debug(f'Getting customer {customer_id} in database')
        customer = Customer.objects(id=customer_id).first()  # pylint: disable=no-member
        if not customer:
            LOGGER.debug('None customer found to customer_id informed')
            raise NotFoundException
        return customer

    def delete_product_by_id(self, product_id: str) -> None:
        LOGGER.debug(f'Deleting product {product_id} in database')
        product = Product.objects(id=product_id).delete()  # pylint: disable=no-member
        if not product:
            raise NotFoundException

    def delete_customer_by_id(self, customer_id: str) -> None:
        LOGGER.debug(f'Deleting customer {customer_id} in database')
        customer = Customer.objects(id=customer_id).delete()  # pylint: disable=no-member
        if not customer:
            raise NotFoundException

    def update_product_by_id(self, product_id: str, data: dict) -> Product:
        LOGGER.debug(f'Updating product {product_id} in database')
        product = Product.objects(id=product_id).first()  # pylint: disable=no-member
        if not product:
            raise NotFoundException
        product.update(**data)  # pylint: disable=no-member
        product = Product.objects(id=product_id).first()
        return product

    def update_customer_by_id(self, customer_id: str, data: dict) -> Customer:
        LOGGER.debug(f'Updating customer {customer_id} in database')
        customer = Customer.objects(id=customer_id).first()  # pylint: disable=no-member
        if not customer:
            raise NotFoundException
        customer.update(**data)  # pylint: disable=no-member
        customer = Customer.objects(id=customer_id).first()
        return customer

    def get_products(self, page: int) -> (list, int):
        LOGGER.debug(f'Getting products page {page}')
        products_total = Product.objects().count()
        if page == 1:
            products = Product.objects().limit(LIMIT_PER_PAGE)
        else:
            products = Product.objects.skip((page - 1) * LIMIT_PER_PAGE).limit(page * LIMIT_PER_PAGE)
        return products, products_total

    def push_product_to_favorites(self, customer: Customer, product: Product) -> Customer:
        LOGGER.debug(f'Pushing product to {customer.id}')
        customer.update(add_to_set__favorites=product)
        customer = Customer.objects(id=customer.id).first()
        return customer

    def pull_product_to_favorites(self, customer: Customer, product: Product) -> Customer:
        LOGGER.debug(f'Pulling product to {customer.id}')
        customer.update(pull__favorites=product)
        customer = Customer.objects(id=customer.id).first()
        return customer
