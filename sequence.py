def elem(n):
    if n % 2:
        return int(3 * n + 1)
    return int(n / 2)


def chain_length(n, cache):
    v, count = n, 1

    while v != 1:
        if v in cache:
            return count + cache[v] - 1
        v, count = elem(v), count + 1

    return count


def longest(n):
    _longest, cache = 0, {0: 0, 1: 1}

    for i in range(1, n):
        cache[i] = chain_length(i, cache)
        _longest = max(cache[i], _longest)

    return _longest


if __name__ == '__main__':
    assert elem(13) == 40
    assert elem(elem(13)) == 20
    assert longest(13) == 20
