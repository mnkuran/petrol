import uuid

from protean.utils.globals import current_domain

from domain import domain
from domain.account.models import Account
from domain.account.commands import RegisterAccount


if __name__ == "__main__":
    with domain.domain_context():
        mahmut_id = str(uuid.uuid4())
        
        current_domain.process(RegisterAccount(account_id=mahmut_id, name="Mahmut Kuran"))
        
        repo = current_domain.repository_for(Account)
        accounts = repo.query.all()
        print(accounts.total)