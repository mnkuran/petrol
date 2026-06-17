from protean import handle
from protean.utils.globals import current_domain

from .. import domain
from .commands import RegisterTransaction
from .models import Transaction


@domain.command_handler(part_of=Transaction)
class TransactionCommandHandler:
    @handle(RegisterTransaction)
    def register_transaction(self, command: RegisterTransaction):
        transaction = Transaction(id=command.transaction_id, from_id=command.from_id, to_id=command.to_id, amount=command.amount)
        current_domain.repository_for(Transaction).add(transaction)