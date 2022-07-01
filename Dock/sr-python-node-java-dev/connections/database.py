from typing import List

from mongoengine import Document

from exceptions.general import NotFoundException
from settings.base import LOGGER


class Database:
    @staticmethod
    def save(document: Document) -> Document:
        LOGGER.debug('Persisting document')
        document.save()
        return document

    @staticmethod
    def get(document_type: Document, query: dict) -> Document:
        LOGGER.debug(
            f'Getting {document_type().__class__.__name__} in database')
        document = document_type.objects(
            **query).first()  # pylint: disable=no-member
        if not document:
            LOGGER.debug('None document found to query informed')
            raise NotFoundException(
                message=f'{document_type().__class__.__name__} not found')
        return document

    @staticmethod
    def remove(document_type: Document, query: dict):
        LOGGER.debug(
            f'Removing {document_type().__class__.__name__} in database')
        document = document_type.objects(
            **query).delete()  # pylint: disable=no-member
        if not document:
            LOGGER.debug('None document found to query informed')
            raise NotFoundException(
                message=f'{document_type().__class__.__name__} not found')

    @staticmethod
    def list(document_type: Document, query: dict) -> List[Document]:
        LOGGER.debug(
            f'Listing {document_type().__class__.__name__} in database')
        return document_type.objects(**query).all()
