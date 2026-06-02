BAD_COMPOUND_NUMBERS = {
    13: "Unexpected obstacles and instability",
    16: "Sudden loss or downfall",
    18: "Conflicts, deception, emotional stress",
    26: "Financial losses and partnership problems",
    29: "Emotional disappointments",
    31: "Isolation and struggles",
    34: "Delayed success and instability",
    38: "Unpredictable financial fluctuations",
    44: "Heavy karmic burden",
    47: "Sudden setbacks",
    56: "Loss through relationships"
}

def check_bad_number(compound):
    if compound in BAD_COMPOUND_NUMBERS:
        return {
            "is_bad": True,
            "reason": BAD_COMPOUND_NUMBERS[compound]
        }
    
    return {
        "is_bad": False,
        "reason": "No negative vibration detected"
    }
