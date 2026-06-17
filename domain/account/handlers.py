from protean import handle
from protean.utils.globals import current_domain

from .. import domain
from .commands import RegisterAccount
from .models import Account


@domain.command_handler(part_of=Account)
class AccountCommandHandler:
    @handle(RegisterAccount)
    def register_account(self, command: RegisterAccount):
        account = Account(id=command.account_id, name=command.name, balance=0)
        current_domain.repository_for(Account).add(account)
