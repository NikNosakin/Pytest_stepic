# from src.calculator import add
import pytest
import sys


# def test_add():
#     assert add(2, 3) == 5


# @pytest.mark.smoke
# def test_pop_from_empty_list():
#     with pytest.raises(IndexError):
#         lst=[]
#         assert not lst.pop()

# @pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
# def test_python310_feature():
#     # Тест использует match-case, который появился в 3.10
#     value = 1
#     match value:
#         case 1:
#             assert True


def square(n):
    return n * n

@pytest.mark.parametrize("number, expected", [(2, 4), (5, 25), (-3, 9)])
def test_square(number, expected):
    assert square(number) == expected