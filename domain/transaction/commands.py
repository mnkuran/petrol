from protean.fields import Identifier, Float

from .. import domain


@domain.command(part_of="Transaction")
class RegisterTransaction:
    transaction_id: Identifier(identifier=True)
    from_id: Identifier(required=True)
    to_id: Identifier(required=True)
    amount: Float(required=True)