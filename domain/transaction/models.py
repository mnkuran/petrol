from protean.fields import Identifier, Float

from .. import domain
from .events import TransactionRegistered


@domain.aggregate
class Transaction:
    from_id: Identifier(required=True)
    to_id: Identifier(required=True)
    amount: Float(required=True)

    def register(self):
        self.raise_(
            TransactionRegistered(
                transaction_id=self.id,
                from_id=self.from_id,
                to_id=self.to_id,
                amount=self.amount
            )
        )