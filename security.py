from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
# username_mapping = {'bob':{
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
#     }
# }
userid_mapping = {u.id: u for u in users}
# userid_mapping = { 1: {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
#     }
# }

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
    