from protean.fields import String

from .. import domain


@domain.aggregate
class Account:
    name: String(required=True)