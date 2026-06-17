from protean.fields import String, Float

from .. import domain


@domain.aggregate
class Account:
    name: String(required=True)
    balance: Float(required=True)