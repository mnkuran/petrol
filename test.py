import uuid

from protean.utils.globals import current_domain

from domain import domain
from domain.account.models import Account
from domain.account.commands import RegisterAccount
from domain.transaction.models import Transaction
from domain.transaction.commands import RegisterTransaction


if __name__ == "__main__":
    with domain.domain_context():
        mahmut_id = str(uuid.uuid4())
        shell_id = str(uuid.uuid4())
        
        current_domain.process(RegisterAccount(account_id=mahmut_id, name="Mahmut Kuran"))
        current_domain.process(RegisterAccount(account_id=shell_id, name="Shell"))

        current_domain.process(RegisterTransaction(transaction_id=uuid.uuid4(), from_id=mahmut_id, to_id=shell_id, amount=50000))
        
        account_repo = current_domain.repository_for(Account)
        print(f"Account count: {account_repo.query.all().total}")
        transaction_repo = current_domain.repository_for(Transaction)
        print(f"Transaction count: {transaction_repo.query.all().total}")

        mahmut = account_repo.get(mahmut_id)
        print(f"Mahmut (Balance: {mahmut.balance})")

        shell = account_repo.get(shell_id)
        print(f"Shell (Balance: {shell.balance})")