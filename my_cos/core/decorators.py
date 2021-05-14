from django.db import transaction


def on_transaction_commit(func):
    """Transaction which make on commit."""
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))

    return inner
