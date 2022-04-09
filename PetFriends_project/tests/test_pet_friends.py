from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()


def test_get_api_key_for_valis_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result  # result == "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729"
