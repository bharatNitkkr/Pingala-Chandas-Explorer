def prastara(n):
    patterns = []

    total_patterns = 2 ** n

    for rank in range(1, total_patterns + 1):
        number = rank - 1

        bits = []

        for i in range(n):
            bit = (number // (2 ** i)) % 2
            bits.append(str(bit))

        bit_pattern = "".join(bits)

        laghu_guru_pattern = ""

        for bit in bit_pattern:
            if bit == "1":
                laghu_guru_pattern += "L"
            else:
                laghu_guru_pattern += "G"

        patterns.append({
            "rank": rank,
            "bit_pattern": bit_pattern,
            "laghu_guru_pattern": laghu_guru_pattern
        })

    return {
        "length": n,
        "total_patterns": total_patterns,
        "patterns": patterns
    }


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
    
    
def matra_chandas(m):
    counts = []

    # M(0) = 1 is used internally for recurrence.
    # It represents the empty pattern.
    dp = [0] * (m + 1)

    if m >= 0:
        dp[0] = 1

    if m >= 1:
        dp[1] = 1

    for i in range(2, m + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    for i in range(1, m + 1):
        counts.append({
            "matra": i,
            "formula": f"M({i}) = M({i - 1}) + M({i - 2})" if i >= 2 else "Base case",
            "count": dp[i]
        })

    patterns = []

    def generate(remaining, current):
        if remaining == 0:
            patterns.append(current)
            return

        if remaining >= 1:
            generate(remaining - 1, current + "L")

        if remaining >= 2:
            generate(remaining - 2, current + "G")

    # Generate actual patterns only for reasonable size
    if m <= 12:
        generate(m, "")

    return {
        "matra": m,
        "count": dp[m],
        "counts": counts,
        "patterns": patterns,
        "patterns_generated": m <= 12
    }
    
    
def combination(n, r):
    if r < 0 or r > n:
        return 0

    if r == 0 or r == n:
        return 1

    r = min(r, n - r)

    result = 1

    for i in range(1, r + 1):
        result = result * (n - r + i) // i

    return result


def matra_meru(m):
    guru_counts = []
    total = 0

    for gurus in range((m // 2) + 1):
        laghus = m - (2 * gurus)
        total_symbols = laghus + gurus

        count = combination(total_symbols, gurus)
        total += count

        guru_counts.append({
            "gurus": gurus,
            "laghus": laghus,
            "total_symbols": total_symbols,
            "formula": f"C({total_symbols}, {gurus})",
            "count": count
        })

    grouped_patterns = []

    def generate(remaining, current):
        if remaining == 0:
            gurus = current.count("G")
            grouped_patterns.append({
                "pattern": current,
                "gurus": gurus,
                "laghus": current.count("L")
            })
            return

        if remaining >= 1:
            generate(remaining - 1, current + "L")

        if remaining >= 2:
            generate(remaining - 2, current + "G")

    if m <= 12:
        generate(m, "")

    return {
        "matra": m,
        "guru_counts": guru_counts,
        "total": total,
        "patterns": grouped_patterns,
        "patterns_generated": m <= 12
    }


def factorial(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


def permutation_algorithm(items):
    from itertools import permutations

    clean_items = []

    for item in items:
        item = item.strip()

        if item:
            clean_items.append(item)

    n = len(clean_items)
    total = factorial(n)

    generated = []

    if n <= 6:
        for perm in permutations(clean_items):
            generated.append(perm)

    return {
        "items": clean_items,
        "n": n,
        "total": total,
        "permutations": generated,
        "generated": n <= 6
    }

def gana_decoder(pattern):
    pattern = pattern.upper().strip()

    bit_pattern = ""

    for ch in pattern:
        if ch == "L" or ch == "1":
            bit_pattern += "1"
        elif ch == "G" or ch == "0":
            bit_pattern += "0"
        else:
            return None

    gana_map = {
        "100": {
            "name": "Ya-gaṇa",
            "sanskrit": "यगण",
            "pattern": "Laghu Guru Guru"
        },
        "000": {
            "name": "Ma-gaṇa",
            "sanskrit": "मगण",
            "pattern": "Guru Guru Guru"
        },
        "001": {
            "name": "Ta-gaṇa",
            "sanskrit": "तगण",
            "pattern": "Guru Guru Laghu"
        },
        "010": {
            "name": "Ra-gaṇa",
            "sanskrit": "रगण",
            "pattern": "Guru Laghu Guru"
        },
        "101": {
            "name": "Ja-gaṇa",
            "sanskrit": "जगण",
            "pattern": "Laghu Guru Laghu"
        },
        "011": {
            "name": "Bha-gaṇa",
            "sanskrit": "भगण",
            "pattern": "Guru Laghu Laghu"
        },
        "111": {
            "name": "Na-gaṇa",
            "sanskrit": "नगण",
            "pattern": "Laghu Laghu Laghu"
        },
        "110": {
            "name": "Sa-gaṇa",
            "sanskrit": "सगण",
            "pattern": "Laghu Laghu Guru"
        }
    }

    groups = []
    remaining = ""

    for i in range(0, len(bit_pattern), 3):
        group = bit_pattern[i:i + 3]

        if len(group) == 3:
            groups.append({
                "bits": group,
                "gana": gana_map[group]
            })
        else:
            remaining = group

    return {
        "input_pattern": pattern,
        "bit_pattern": bit_pattern,
        "groups": groups,
        "remaining": remaining,
        "total_ganas": len(groups)
    }

def pattern_analyzer(pattern):
    pattern = pattern.upper().strip()

    bit_pattern = ""
    laghu_guru_pattern = ""

    for ch in pattern:
        if ch == "L" or ch == "1":
            bit_pattern += "1"
            laghu_guru_pattern += "L"
        elif ch == "G" or ch == "0":
            bit_pattern += "0"
            laghu_guru_pattern += "G"
        else:
            return None

    length = len(laghu_guru_pattern)
    laghu_count = laghu_guru_pattern.count("L")
    guru_count = laghu_guru_pattern.count("G")

    matra_value = (laghu_count * 1) + (guru_count * 2)

    # Uddista rank calculation according to lecture method
    rank = 1
    rank_steps = []

    for bit in reversed(bit_pattern):
        old_rank = rank

        if bit == "1":
            rank = 2 * rank
            operation = f"2 × {old_rank} = {rank}"
        else:
            rank = (2 * rank) - 1
            operation = f"2 × {old_rank} - 1 = {rank}"

        rank_steps.append({
            "bit": bit,
            "old_rank": old_rank,
            "operation": operation,
            "new_rank": rank
        })

    gana_map = {
        "100": {
            "name": "Ya-gaṇa",
            "sanskrit": "यगण",
            "pattern": "Laghu Guru Guru"
        },
        "000": {
            "name": "Ma-gaṇa",
            "sanskrit": "मगण",
            "pattern": "Guru Guru Guru"
        },
        "001": {
            "name": "Ta-gaṇa",
            "sanskrit": "तगण",
            "pattern": "Guru Guru Laghu"
        },
        "010": {
            "name": "Ra-gaṇa",
            "sanskrit": "रगण",
            "pattern": "Guru Laghu Guru"
        },
        "101": {
            "name": "Ja-gaṇa",
            "sanskrit": "जगण",
            "pattern": "Laghu Guru Laghu"
        },
        "011": {
            "name": "Bha-gaṇa",
            "sanskrit": "भगण",
            "pattern": "Guru Laghu Laghu"
        },
        "111": {
            "name": "Na-gaṇa",
            "sanskrit": "नगण",
            "pattern": "Laghu Laghu Laghu"
        },
        "110": {
            "name": "Sa-gaṇa",
            "sanskrit": "सगण",
            "pattern": "Laghu Laghu Guru"
        }
    }

    ganas = []
    remaining = ""

    for i in range(0, len(bit_pattern), 3):
        group = bit_pattern[i:i + 3]

        if len(group) == 3:
            ganas.append({
                "bits": group,
                "gana": gana_map[group]
            })
        else:
            remaining = group

    return {
        "input_pattern": pattern,
        "laghu_guru_pattern": laghu_guru_pattern,
        "bit_pattern": bit_pattern,
        "length": length,
        "laghu_count": laghu_count,
        "guru_count": guru_count,
        "matra_value": matra_value,
        "rank": rank,
        "rank_steps": rank_steps,
        "ganas": ganas,
        "remaining": remaining
    }

def chandas_identifier(pattern):
    """
    Identify the Chandas class, gaṇas, and an exact meter match
    from a Laghu-Guru or binary pattern.

    Laghu = L or 1
    Guru = G or 0
    """

    if not isinstance(pattern, str):
        return None

    bit_pattern = ""
    laghu_guru_pattern = ""

    for ch in pattern.upper().strip():

        # Allow grouped patterns such as LGG LGG LGG LGG
        if ch in {" ", "-", "_", "|", ","}:
            continue

        if ch in {"L", "1"}:
            bit_pattern += "1"
            laghu_guru_pattern += "L"

        elif ch in {"G", "0"}:
            bit_pattern += "0"
            laghu_guru_pattern += "G"

        else:
            return None

    if not bit_pattern:
        return None

    # Chandas class according to akṣara length
    class_by_length = {
        6: "Gāyatrī",
        7: "Uṣṇih",
        8: "Anuṣṭubh",
        9: "Bṛhatī",
        10: "Paṅkti",
        11: "Triṣṭubh",
        12: "Jagatī",
        13: "Atijagatī",
        14: "Śakvarī",
        15: "Atiśakvarī",
        16: "Aṣṭi",
        17: "Atyaṣṭi",
        18: "Dhṛti",
        19: "Atidhṛti",
    }

    gana_map = {
        "100": {
            "name": "Ya-gaṇa",
            "sanskrit": "यगण",
            "short": "Ya",
        },
        "000": {
            "name": "Ma-gaṇa",
            "sanskrit": "मगण",
            "short": "Ma",
        },
        "001": {
            "name": "Ta-gaṇa",
            "sanskrit": "तगण",
            "short": "Ta",
        },
        "010": {
            "name": "Ra-gaṇa",
            "sanskrit": "रगण",
            "short": "Ra",
        },
        "101": {
            "name": "Ja-gaṇa",
            "sanskrit": "जगण",
            "short": "Ja",
        },
        "011": {
            "name": "Bha-gaṇa",
            "sanskrit": "भगण",
            "short": "Bha",
        },
        "111": {
            "name": "Na-gaṇa",
            "sanskrit": "नगण",
            "short": "Na",
        },
        "110": {
            "name": "Sa-gaṇa",
            "sanskrit": "सगण",
            "short": "Sa",
        },
    }

    ganas = []
    remaining = ""

    for i in range(0, len(bit_pattern), 3):
        group = bit_pattern[i:i + 3]

        if len(group) == 3:
            ganas.append({
                "bits": group,
                "gana": gana_map[group],
            })
        else:
            remaining = group

    # Small meter library — we will expand this next
    meter_library = {
        "100100100100": {
            "name": "Bhujanga-prayāta",
            "sanskrit": "भुजङ्गप्रयात",
            "class_name": "Jagatī",
            "description": (
                "A 12-akṣara sama-vṛtta formed by four "
                "Ya-gaṇas: LGG × 4."
            ),
        }
    }

    length = len(bit_pattern)

    return {
        "input_pattern": pattern,
        "laghu_guru_pattern": laghu_guru_pattern,
        "bit_pattern": bit_pattern,
        "length": length,
        "class_name": class_by_length.get(
            length,
            "Class not yet added",
        ),
        "exact_meter": meter_library.get(bit_pattern),
        "ganas": ganas,
        "remaining": remaining,
    }
