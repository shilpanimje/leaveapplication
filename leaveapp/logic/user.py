from leaveapp.models import users


def create_user(data):
    """Logic handlers.

    Args:
        data: Data to submit.

    Returns:
        Response: response.
    """
    return users.create_user(data)

