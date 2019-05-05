import pytest


# test data
udid_8 = ["FRFF9ZYA", "FRFF8ZY6", "FRFF7ZYS"]
@pytest.fixture(params = udid_8)
def udid_8_success(request):
    return request.param