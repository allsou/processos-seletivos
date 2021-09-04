from validations.general import is_object_id


class FavoriteValidations:
    @staticmethod
    def validate_customer_product_id(customer_id: str, product_id: str):
        for identity in [customer_id, product_id]:
            is_object_id(identity)

