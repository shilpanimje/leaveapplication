from flask import json
from leaveapp.connector import connector
from leaveapp.connector.connector import cur
from werkzeug import generate_password_hash, check_password_hash


def create_user(data):
    """Model.

    Args:
        data: Data to submit.

    Returns:
        Response: response.
    """
    _hashed_password = generate_password_hash(data['password'])
    cur.callproc('sp_createUser',(data['name'],data['username'],_hashed_password))
    results = cur.fetchone()

    if isinstance(results, tuple):
        return json.dumps(
            {'html': results[0],
             'flag': 0})
    else:
        return json.dumps(
            {'html': 'Created successfully',
             'flag': 1})

