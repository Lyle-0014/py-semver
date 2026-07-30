from semver import compare


def test_order():
    assert compare("1.2.0", "1.10.0") < 0
    assert compare("v2.0.0", "1.9.9") > 0
    assert compare("1.0.0", "1.0.0") == 0
