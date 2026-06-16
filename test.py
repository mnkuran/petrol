from domain import domain
from domain.account.models import Account


if __name__ == "__main__":
    with domain.domain_context():
        account = Account(name="Mahmut Kuran")

        print(account.name)