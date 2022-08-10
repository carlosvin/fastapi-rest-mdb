from fastapi_rest_mdb.logics.user_logic import UserModel


def test_user_model():
    username = "A"
    is_admin = True
    user = UserModel(username=username, is_admin=is_admin)
    assert user.username == username
    assert user.is_admin == is_admin
