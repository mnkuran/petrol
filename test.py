import uuid

from protean.utils.globals import current_domain
from protean import Q

from domain import domain
from domain.account.models import Account
from domain.account.commands import RegisterAccount
from domain.transaction.models import Transaction
from domain.transaction.projections import AccountTransaction
from domain.transaction.commands import RegisterTransaction


if __name__ == "__main__":
    with domain.domain_context():
        mahmut_id = str(uuid.uuid4())
        shell_id = str(uuid.uuid4())
        
        current_domain.process(RegisterAccount(account_id=mahmut_id, name="Mahmut Kuran"))
        current_domain.process(RegisterAccount(account_id=shell_id, name="Shell"))

        current_domain.process(RegisterTransaction(transaction_id=uuid.uuid4(), from_id=mahmut_id, to_id=shell_id, amount=50000))
        current_domain.process(RegisterTransaction(transaction_id=uuid.uuid4(), from_id=shell_id, to_id=mahmut_id, amount=25000))
        
        account_repo = current_domain.repository_for(Account)
        transactions_view = current_domain.view_for(AccountTransaction)

        first_account = account_repo.query.first
        print(f"{first_account.name}: {first_account.balance}")
        for accont_transaction in transactions_view.query.filter(account_id=first_account.id).all():
            print(f"{accont_transaction.account_name} => {accont_transaction.debit} | {accont_transaction.credit}")