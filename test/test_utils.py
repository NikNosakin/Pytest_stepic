from src.utils import get_random_number

def test_mocker(mocker):
    mocker.patch("src.utils.random.randint", return_value=58)
    assert get_random_number() == 58