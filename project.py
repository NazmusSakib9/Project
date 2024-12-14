atomic_weights = {
    "H": 1.008, "O": 16.00, "C": 12.01, "N": 14.01,
    "Na": 22.99, "Cl": 35.45, "K": 39.10,
}
import re


atomic_weights = {
    "H": 1.008, "O": 16.00, "C": 12.01, "N": 14.01,
    "Na": 22.99, "Cl": 35.45, "K": 39.10,
    
}

def parse_formula(formula):
    """Parse a chemical formula and count atoms."""
    pattern = r"([A-Z][a-z]*)(\d*)"
    matches = re.findall(pattern, formula)
    composition = {}
    for element, count in matches:
        count = int(count) if count else 1
        composition[element] = composition.get(element, 0) + count
    return composition

def calculate_molecular_weight(formula):
    """Calculate the molecular weight of a chemical formula."""
    composition = parse_formula(formula)
    weight = 0
    for element, count in composition.items():
        if element not in atomic_weights:
            raise ValueError(f"Unknown element: {element}")
        weight += atomic_weights[element] * count
    return weight


formula = input("Enter a chemical formula: ")
try:
    mw = calculate_molecular_weight(formula)
    print(f"Molecular weight of {formula}: {mw} g/mol")
except ValueError as e:
    print(e)