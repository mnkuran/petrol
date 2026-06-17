from protean.fields import Identifier, Float, Auto, String

from .. import domain


@domain.projection
class AccountTransaction:
    id: Auto(identifier=True, increment=True)
    source_id: Identifier(required=True)
    account_id: Identifier(required=True)
    account_name: String(required=True)
    debit: Float(required=True)
    credit: Float(required=True)