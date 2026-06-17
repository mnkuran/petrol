import uuid

from protean import handle
from protean.utils.globals import current_domain

from .. import domain
from .models import Transaction
from ..account.models import Account
from .events import TransactionRegistered
from .projections import AccountTransaction


@domain.projector(projector_for=AccountTransaction, aggregates=[Transaction])
class AccountTransactionProjector:
    @handle(TransactionRegistered)
    def on_transaction_registered(self, event: TransactionRegistered):
        transaction_id = event.transaction_id
        amount = event.amount
        
        account_repo = current_domain.repository_for(Account)
        from_account = account_repo.get(event.from_id)
        to_account = account_repo.get(event.to_id)

        repo = current_domain.repository_for(AccountTransaction)

        from_transaction = AccountTransaction(
            source_id=transaction_id,
            account_id=from_account.id,
            account_name=from_account.name,
            debit=amount,
            credit=0
        )
        repo.add(from_transaction)

        to_transaction = AccountTransaction(
            source_id=transaction_id,
            account_id=to_account.id,
            account_name=to_account.name,
            debit=0,
            credit=amount
        )
        repo.add(to_transaction)