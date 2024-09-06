roman_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def roman_to_number(roman_numeral):

  number = 0
  prev_value = 0
  for char in roman_numeral.upper():
    if char not in roman_map:
      raise ValueError(f"Invalid character '{char}' in Roman numeral")
    current_value = roman_map[char]
    if current_value <= prev_value:
      # Add previous value
      number += prev_value
    else:
      # Subtract previous value from current value and accumulate
      number -= prev_value 
    prev_value = current_value
  # Add the final value
  number += prev_value
  return number

# Example usage
roman_numeral = "IV"
number = roman_to_number(roman_numeral)
print(f"Roman numeral '{roman_numeral}' is equivalent to {number}")

