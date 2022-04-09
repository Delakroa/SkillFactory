from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()


def test_get_api_key_for_valis_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result  # result == "d524b1fb97990041ae6c5138c688ac35ab0292a971e458827b2f41fd"
