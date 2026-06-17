from protean.fields import Identifier, Float

from .. import domain


@domain.aggregate
class Transaction:
    from_id: Identifier(required=True)
    to_id: Identifier(required=True)
    amount: Float(required=True)