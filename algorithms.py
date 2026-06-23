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

    q = index
    bits = []
    steps = []

    for step_number in range(1, n + 1):
        old_q = q

        if q % 2 == 0:
            bit = "1"
            new_q = q // 2
            operation = f"{q} is even → write 1 → new q = {q} / 2 = {new_q}"
        else:
            bit = "0"
            new_q = (q + 1) // 2
            operation = f"{q} is odd → write 0 → new q = ({q} + 1) / 2 = {new_q}"

        bits.append(bit)

        steps.append({
            "step": step_number,
            "q": old_q,
            "parity": "Even" if old_q % 2 == 0 else "Odd",
            "bit": bit,
            "operation": operation,
            "new_q": new_q
        })

        q = new_q

    bit_pattern = "".join(bits)

    laghu_guru_pattern = ""

    for bit in bit_pattern:
        if bit == "1":
            laghu_guru_pattern += "L"
        else:
            laghu_guru_pattern += "G"

    standard_binary = bin(index - 1)[2:].zfill(n)

    return {
        "index": index,
        "length": n,
        "bit_pattern": bit_pattern,
        "laghu_guru_pattern": laghu_guru_pattern,
        "standard_binary": standard_binary,
        "steps": steps,
        "total_patterns": total_patterns
    }


def uddista(pattern):
    pattern = pattern.upper().strip()

    for ch in pattern:
        if ch not in ["L", "G", "0", "1"]:
            return None

    bit_pattern = ""

    for ch in pattern:
        if ch == "L" or ch == "1":
            bit_pattern += "1"
        else:
            bit_pattern += "0"

    r = 1
    steps_algorithm_1 = []

    for bit in reversed(bit_pattern):
        old_r = r

        if bit == "1":
            r = 2 * r
            operation = f"2 × {old_r} = {r}"
        else:
            r = (2 * r) - 1
            operation = f"2 × {old_r} - 1 = {r}"

        steps_algorithm_1.append({
            "bit": bit,
            "old_r": old_r,
            "operation": operation,
            "new_r": r
        })

    weights = []
    selected_sum = 0

    for i, bit in enumerate(bit_pattern):
        weight = 2 ** i

        if bit == "1":
            selected_sum += weight
            selected = True
        else:
            selected = False

        weights.append({
            "bit": bit,
            "weight": weight,
            "selected": selected
        })

    rank_by_binary_method = selected_sum + 1

    return {
        "input_pattern": pattern,
        "bit_pattern": bit_pattern,
        "length": len(bit_pattern),
        "rank": r,
        "steps_algorithm_1": steps_algorithm_1,
        "weights": weights,
        "selected_sum": selected_sum,
        "rank_by_binary_method": rank_by_binary_method
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