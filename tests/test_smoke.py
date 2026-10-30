import dobby


def test_package_imports():
    assert dobby is not None


def test_maths():
    assert 1 + 1 == 2
