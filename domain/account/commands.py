from protean.fields import Identifier, String

from .. import domain


@domain.command(part_of="Account")
class RegisterAccount:
    account_id: Identifier(identifier=True)
    name: String(required=True)