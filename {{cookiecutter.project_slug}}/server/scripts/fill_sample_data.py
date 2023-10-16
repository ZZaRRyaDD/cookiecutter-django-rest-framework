from apps.users.factories import UserFactory

COUNT_USERS = 10


def run():
    """Generate example data."""
    UserFactory.create_batch(size=COUNT_USERS)
