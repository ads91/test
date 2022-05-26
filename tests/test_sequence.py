from sequence import elem, longest


def test_elem():
    assert elem(13) == 40
    assert elem(elem(13)) == 20


def test_longest():
    assert longest(13) == 20


if __name__ == '__main__':
    test_elem()
    test_longest()
