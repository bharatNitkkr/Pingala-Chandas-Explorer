SUTRA_DETAILS = {
    "nasta": {
        "title": "Naṣṭa Algorithm",
        "purpose": "To recover the Laghu-Guru pattern from a given rank number.",
        "sutras": [
            "लर्धे ॥ ८.२४ ॥",
            "सैके ग् ॥ ८.२५ ॥"
        ],
        "padaccheda": [
            "ल् + अर्धे",
            "स + एके + ग्"
        ],
        "word_meanings": [
            {
                "word": "ल्",
                "literal": "Laghu",
                "algorithm": "Write Laghu when the number is even and can be halved directly."
            },
            {
                "word": "अर्धे",
                "literal": "On halving",
                "algorithm": "Divide the current number by 2."
            },
            {
                "word": "स + एके",
                "literal": "With one added",
                "algorithm": "If the number is odd, add 1 before halving."
            },
            {
                "word": "ग्",
                "literal": "Guru",
                "algorithm": "Write Guru when the number is odd."
            }
        ],
        "sutra_to_algorithm": [
            {
                "sutra": "लर्धे",
                "meaning": "When halving is possible directly, it indicates Laghu.",
                "step": "If q is even: write L, then q = q / 2."
            },
            {
                "sutra": "सैके ग्",
                "meaning": "When one must be added before halving, it indicates Guru.",
                "step": "If q is odd: write G, then q = (q + 1) / 2."
            }
        ],
        "example": [
            "Let rank r = 5 and length n = 3.",
            "5 is odd → write Guru → q = (5 + 1) / 2 = 3.",
            "3 is odd → write Guru → q = (3 + 1) / 2 = 2.",
            "2 is even → write Laghu → q = 2 / 2 = 1.",
            "Final pattern = G G L = 001."
        ],
        "source": "Piṅgala Chandaḥsūtra 8.24–8.25 with Halāyudha commentary."
    },

    "uddista": {
        "title": "Uddiṣṭa Algorithm",
        "purpose": "To find the rank number of a given Laghu-Guru pattern.",
        "sutras": [
            "प्रतिलोमगणं द्विर्लाद्यम् ॥ ८.२६ ॥",
            "ततो ग्येकं जह्यात् ॥ ८.२७ ॥"
        ],
        "padaccheda": [
            "प्रतिलोम-गणम् + द्विः + ल्-आद्यम्",
            "ततः + गि + एकम् + जह्यात्"
        ],
        "word_meanings": [
            {
                "word": "प्रतिलोम",
                "literal": "Reverse order",
                "algorithm": "Read the pattern from right to left."
            },
            {
                "word": "द्विः",
                "literal": "Twice",
                "algorithm": "Double the current rank value."
            },
            {
                "word": "ल्",
                "literal": "Laghu",
                "algorithm": "For Laghu, use r = 2r."
            },
            {
                "word": "गि",
                "literal": "When Guru occurs",
                "algorithm": "For Guru, modify the doubled value."
            },
            {
                "word": "एकं जह्यात्",
                "literal": "Subtract one",
                "algorithm": "For Guru, use r = 2r - 1."
            }
        ],
        "sutra_to_algorithm": [
            {
                "sutra": "प्रतिलोमगणम्",
                "meaning": "Counting is done in reverse order.",
                "step": "Read the pattern from right to left."
            },
            {
                "sutra": "द्विर्लाद्यम्",
                "meaning": "For Laghu, double the value.",
                "step": "If bit = 1, r = 2r."
            },
            {
                "sutra": "ततो ग्येकं जह्यात्",
                "meaning": "For Guru, subtract one after doubling.",
                "step": "If bit = 0, r = 2r - 1."
            }
        ],
        "example": [
            "Pattern = G G L = 001.",
            "Start r = 1.",
            "Read from right: 1 → r = 2 × 1 = 2.",
            "Read 0 → r = 2 × 2 - 1 = 3.",
            "Read 0 → r = 2 × 3 - 1 = 5.",
            "Final rank = 5."
        ],
        "source": "Piṅgala Chandaḥsūtra 8.26–8.27 with Halāyudha commentary."
    }
}
