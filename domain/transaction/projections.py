from protean.fields import Identifier, Float

from .. import domain


@domain.projection
class AccountTransaction:
    source_id: Identifier(identifier=True, required=True)
    account_id: Identifier(required=True)
    debit: Float(required=True)
    credit: Float(required=True)