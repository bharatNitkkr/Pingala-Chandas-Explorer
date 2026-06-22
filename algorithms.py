def prastara(n):
    result = []

    def generate(current, length):
        if length == n:
            result.append(current)
            return

        generate(current + "L", length + 1)
        generate(current + "G", length + 1)

    generate("", 0)
    return result


def sankhya(n):
    return 2 ** n


def nasta(n, index):
    patterns = prastara(n)

    if index < 1 or index > len(patterns):
        return None

    return patterns[index - 1]


def uddista(pattern):
    n = len(pattern)
    patterns = prastara(n)

    if pattern not in patterns:
        return None

    return patterns.index(pattern) + 1


def adhvayoga(n):
    total = 0
    values = []

    for i in range(n + 1):
        count = 2 ** i
        total += count
        values.append({
            "length": i,
            "count": count,
            "cumulative": total
        })

    return values


def meru_prastara(rows):
    triangle = []

    for i in range(rows):
        row = [1]

        if i > 0:
            previous = triangle[i - 1]

            for j in range(len(previous) - 1):
                row.append(previous[j] + previous[j + 1])

            row.append(1)

        triangle.append(row)

    return triangle