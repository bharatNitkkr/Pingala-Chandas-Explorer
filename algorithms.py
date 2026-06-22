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
    total_patterns = 2 ** n

    if index < 1 or index > total_patterns:
        return None

    binary_number = bin(index - 1)[2:]

    binary_number = binary_number.zfill(n)

    pattern = ""

    for bit in binary_number:
        if bit == "1":
            pattern += "L"
        else:
            pattern += "G"

    return {
        "index": index,
        "length": n,
        "binary": binary_number,
        "pattern": pattern
    }


def uddista(pattern):
    pattern = pattern.upper()

    for ch in pattern:
        if ch not in ["L", "G"]:
            return None

    binary_number = ""

    for ch in pattern:
        if ch == "L":
            binary_number += "1"
        else:
            binary_number += "0"

    decimal_value = int(binary_number, 2)

    index = decimal_value + 1

    return {
        "pattern": pattern,
        "binary": binary_number,
        "decimal": decimal_value,
        "index": index,
        "length": len(pattern)
    }


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