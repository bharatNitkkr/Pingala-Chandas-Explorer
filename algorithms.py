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


'''def sankhya(n):
    return {
        "length": n,
        "formula": f"2^{n}",
        "total": 2 ** n
    }'''

def sankhya(n):
    steps_down = []
    temp = n

    while temp > 0:
        if temp % 2 == 0:
            steps_down.append({
                "current": temp,
                "code": 2,
                "operation": f"{temp} / 2 = {temp // 2}"
            })
            temp = temp // 2
        else:
            steps_down.append({
                "current": temp,
                "code": 0,
                "operation": f"{temp} - 1 = {temp - 1}"
            })
            temp = temp - 1

    value = 1
    steps_up = []

    for step in reversed(steps_down):
        if step["code"] == 2:
            new_value = value * value
            steps_up.append({
                "code": 2,
                "operation": f"{value}² = {new_value}",
                "result": new_value
            })
            value = new_value
        else:
            new_value = value * 2
            steps_up.append({
                "code": 0,
                "operation": f"{value} × 2 = {new_value}",
                "result": new_value
            })
            value = new_value

    return {
        "length": n,
        "steps_down": steps_down,
        "steps_up": steps_up,
        "total": value,
        "direct_formula": f"2^{n}"
    }

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
    terms = []
    cumulative = 0

    for length in range(1, n + 1):
        count = 2 ** length
        cumulative += count

        terms.append({
            "length": length,
            "formula": f"2^{length}",
            "count": count,
            "cumulative": cumulative
        })

    direct_answer = (2 ** (n + 1)) - 2

    return {
        "n": n,
        "terms": terms,
        "total": cumulative,
        "direct_formula": f"2^({n}+1) - 2",
        "direct_answer": direct_answer
    }


def meru_prastara(n):
    triangle = []

    for i in range(n + 1):
        row = [1]

        if i > 0:
            previous = triangle[i - 1]

            for j in range(len(previous) - 1):
                row.append(previous[j] + previous[j + 1])

            row.append(1)

        triangle.append(row)

    meru_row = triangle[n]

    guru_counts = []

    for gurus, count in enumerate(meru_row):
        laghus = n - gurus

        guru_counts.append({
            "gurus": gurus,
            "laghus": laghus,
            "count": count
        })

    return {
        "length": n,
        "triangle": triangle,
        "meru_row": meru_row,
        "guru_counts": guru_counts,
        "total_patterns": 2 ** n
    }