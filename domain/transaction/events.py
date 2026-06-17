from protean.fields import Identifier, Float

from .. import domain


@domain.event(part_of="Transaction")
class TransactionRegistered:
    transaction_id: Identifier(required=True)
    from_id: Identifier(required=True)
    to_id: Identifier(required=True)
    amount: Float(required=True)