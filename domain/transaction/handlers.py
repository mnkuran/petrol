from protean import handle
from protean.utils.globals import current_domain

from .. import domain
from .commands import RegisterTransaction
from .events import TransactionRegistered
from .models import Transaction
from ..account.models import Account


@domain.command_handler(part_of=Transaction)
class TransactionCommandHandler:
    @handle(RegisterTransaction)
    def register_transaction(self, command: RegisterTransaction):
        transaction = Transaction(id=command.transaction_id, from_id=command.from_id, to_id=command.to_id, amount=command.amount)
        transaction.register()
        current_domain.repository_for(Transaction).add(transaction)


@domain.event_handler(part_of=Transaction)
class AccountBalanceEventHandler:
    @handle(TransactionRegistered)
    def on_transaction_registered(self, event: TransactionRegistered):
        repo = current_domain.repository_for(Account)
        
        from_account = repo.get(event.from_id)
        from_account.balance -= event.amount
        repo.add(from_account)
        
        to_account = repo.get(event.to_id)
        to_account.balance += event.amount
        repo.add(to_account)