SUTRA_DETAILS = {
    "prastara": {
        "title": "Prastāra Algorithm",
        "purpose": "To systematically generate all possible Laghu-Guru patterns of a given length.",
        "sutras": [
            "द्विको ग्लौ ॥ ८.२० ॥",
            "मिश्री च ॥ ८.२१ ॥",
            "पृथग्ला मिश्राः ॥ ८.२२ ॥",
            "वसवस्त्रिकाः ॥ ८.२३ ॥"
        ],
        "padaccheda": [
            "द्विकः + ग्लौ",
            "मिश्री + च",
            "पृथक् + लाः + मिश्राः",
            "वसवः + त्रिकाः"
        ],
        "word_meanings": [
            {
                "word": "द्विकः",
                "literal": "Pair / twofold",
                "algorithm": "Start with two possible syllable types."
            },
            {
                "word": "ग्लौ",
                "literal": "Guru and Laghu",
                "algorithm": "Use G and L as the two binary choices."
            },
            {
                "word": "मिश्री",
                "literal": "Mixed arrangement",
                "algorithm": "Combine previous patterns with Guru and Laghu."
            },
            {
                "word": "पृथक्",
                "literal": "Separately",
                "algorithm": "Separate patterns into ordered rows."
            },
            {
                "word": "वसवः",
                "literal": "Eight",
                "algorithm": "For three syllables, total patterns become 8."
            }
        ],
        "sutra_to_algorithm": [
            {
                "sutra": "द्विको ग्लौ",
                "meaning": "There are two basic choices: Guru and Laghu.",
                "step": "For each position, choose either G = 0 or L = 1."
            },
            {
                "sutra": "मिश्री च",
                "meaning": "The choices are mixed systematically.",
                "step": "Generate combinations by changing Laghu-Guru positions in order."
            },
            {
                "sutra": "पृथग्ला मिश्राः",
                "meaning": "Laghu placements are separated and arranged.",
                "step": "Create rows where each unique position-pattern appears once."
            },
            {
                "sutra": "वसवस्त्रिकाः",
                "meaning": "For three syllables there are eight forms.",
                "step": "For n = 3, total = 2³ = 8 patterns."
            }
        ],
        "example": [
            "For n = 3, each place may be Guru or Laghu.",
            "Total patterns = 2³ = 8.",
            "Using G = 0 and L = 1, the patterns are generated in ordered Prastāra form.",
            "Example order: GGG, LGG, GLG, LLG, GGL, LGL, GLL, LLL."
        ],
        "source": "Piṅgala Chandaḥsūtra 8.20–8.23 with traditional commentary. This reading should be verified with the edition recommended by the mentor."
    },

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
    },

    "sankhya": {
        "title": "Saṁkhyāna Algorithm",
        "purpose": "To calculate the total number of Laghu-Guru patterns of length n.",
        "sutras": [
            "द्विरर्धे ॥ ८.२८ ॥",
            "रूपे शून्यम् ॥ ८.२९ ॥",
            "द्विः शून्ये ॥ ८.३० ॥",
            "तावदर्धे तद्गुणितम् ॥ ८.३१ ॥"
        ],
        "padaccheda": [
            "द्विः + अर्धे",
            "रूपे + शून्यम्",
            "द्विः + शून्ये",
            "तावत् + अर्धे + तत् + गुणितम्"
        ],
        "word_meanings": [
            {
                "word": "द्विः",
                "literal": "Two / twice",
                "algorithm": "Use doubling or squaring depending on the stored mark."
            },
            {
                "word": "अर्धे",
                "literal": "On halving",
                "algorithm": "If n is even, divide n by 2 and store mark 2."
            },
            {
                "word": "रूपे",
                "literal": "When one remains",
                "algorithm": "If n is odd, subtract 1."
            },
            {
                "word": "शून्यम्",
                "literal": "Zero",
                "algorithm": "Store mark 0 for the odd step."
            },
            {
                "word": "तद्गुणितम्",
                "literal": "Multiplied by itself",
                "algorithm": "For mark 2, square the current value."
            }
        ],
        "sutra_to_algorithm": [
            {
                "sutra": "द्विरर्धे",
                "meaning": "When n can be halved, mark it with 2.",
                "step": "If n is even: n = n / 2, store 2."
            },
            {
                "sutra": "रूपे शून्यम्",
                "meaning": "When n is reduced by one, mark it with 0.",
                "step": "If n is odd: n = n - 1, store 0."
            },
            {
                "sutra": "द्विः शून्ये",
                "meaning": "For zero-mark, double the value.",
                "step": "If mark = 0: value = value × 2."
            },
            {
                "sutra": "तावदर्धे तद्गुणितम्",
                "meaning": "For half-mark, multiply the value by itself.",
                "step": "If mark = 2: value = value²."
            }
        ],
        "example": [
            "For n = 10, the total number of patterns is 2¹⁰.",
            "10 is even → divide by 2 → store 2.",
            "5 is odd → subtract 1 → store 0.",
            "4 is even → divide by 2 → store 2.",
            "2 is even → divide by 2 → store 2.",
            "1 is odd → subtract 1 → store 0.",
            "Reconstructing in reverse gives 2¹⁰ = 1024."
        ],
        "source": "Piṅgala Chandaḥsūtra 8.28–8.31. The algorithm is interpreted as fast computation of 2ⁿ through halving, doubling, and squaring."
    },

    "adhvayoga": {
        "title": "Adhvayōga Algorithm",
        "purpose": "To calculate the total number of patterns from length 1 up to length n.",
        "sutras": [
            "द्विद्यूनं तदन्तानाम् ॥ ८.३२ ॥"
        ],
        "padaccheda": [
            "द्वि + द्यूनम् + तत् + अन्तानाम्"
        ],
        "word_meanings": [
            {
                "word": "द्वि",
                "literal": "Two",
                "algorithm": "Relates the sum to twice the final count."
            },
            {
                "word": "द्यून्ं / द्यूनम्",
                "literal": "Lessened / subtracted",
                "algorithm": "Subtract 2 from twice the final power."
            },
            {
                "word": "तदन्तानाम्",
                "literal": "Up to that end",
                "algorithm": "Sum all counts from 1 syllable up to n syllables."
            }
        ],
        "sutra_to_algorithm": [
            {
                "sutra": "द्विद्यूनम्",
                "meaning": "Two less than twice the final value.",
                "step": "Compute 2 × 2ⁿ - 2."
            },
            {
                "sutra": "तदन्तानाम्",
                "meaning": "For all values ending at n.",
                "step": "Sum 2¹ + 2² + ... + 2ⁿ."
            }
        ],
        "example": [
            "For n = 4, the total path count is 2¹ + 2² + 2³ + 2⁴.",
            "That is 2 + 4 + 8 + 16 = 30.",
            "Using the formula: 2 × 2⁴ - 2 = 32 - 2 = 30."
        ],
        "source": "Piṅgala Chandaḥsūtra 8.32, interpreted as the sum 2¹ + 2² + ... + 2ⁿ = 2ⁿ⁺¹ - 2."
    },

    "meru": {
        "title": "Lagakriyā / Meru-Prastāra Algorithm",
        "purpose": "To calculate how many patterns contain a fixed number of Guru or Laghu positions.",
        "sutras": [
            "परे पूर्णम् ॥ ८.३४ ॥",
            "परे पूर्णम् इति ॥ ८.३५ ॥"
        ],
        "padaccheda": [
            "परे + पूर्णम्",
            "परे + पूर्णम् + इति"
        ],
        "word_meanings": [
            {
                "word": "परे",
                "literal": "In the next / following place",
                "algorithm": "Move to the next row or next position of the triangular table."
            },
            {
                "word": "पूर्णम्",
                "literal": "Complete / fill",
                "algorithm": "Fill the table using values from the previous row."
            },
            {
                "word": "इति",
                "literal": "Thus",
                "algorithm": "Repeat the filling rule until the required row is completed."
            }
        ],
        "sutra_to_algorithm": [
            {
                "sutra": "परे पूर्णम्",
                "meaning": "The next place is filled from previous values.",
                "step": "Interior value = upper-left value + upper-right value."
            },
            {
                "sutra": "परे पूर्णम् इति",
                "meaning": "Continue filling in this manner.",
                "step": "Repeat row by row to form Meru / Pascal triangle."
            }
        ],
        "example": [
            "For n = 4, Meru row is 1, 4, 6, 4, 1.",
            "This means: 0 Guru → 1 pattern.",
            "1 Guru → 4 patterns.",
            "2 Gurus → 6 patterns.",
            "3 Gurus → 4 patterns.",
            "4 Gurus → 1 pattern.",
            "Total = 1 + 4 + 6 + 4 + 1 = 16 = 2⁴."
        ],
        "source": "Piṅgala Chandaḥsūtra 8.34–8.35 with Halāyudha's Meru-prastāra interpretation."
    }
}
