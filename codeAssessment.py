from collections import Counter
import math


def is_magical_potion(power: int) -> str:
    if round(power ** (1/3)) ** 3 == power:
        return "YES"
    else:
        return "NO"

print(is_magical_potion(132651201231))



def find_sneaky_outcomes(outcomes: list) -> list:
    seen = set() 
    duplicates = []  
    
    for outcome in outcomes:
        if outcome in seen:
            duplicates.append(outcome)
        else:
            seen.add(outcome)
    
    return duplicates

print(find_sneaky_outcomes([123456, 234567, 123347, 456789, 567890, 678901,
                             789012, 890123, 901234, 112233, 223344, 334455, 
                             789012, 222234, 123347]))


def reformat_string(s: str) -> str:
    result = []  
    is_upper = True
    
    for char in s:
        if char.isalpha():  
            if is_upper:
                result.append(char.upper())  
            else:
                result.append(char.lower()) 
            is_upper = not is_upper  
        else:
            result.append(char) 
    
    return ''.join(result)  

print(reformat_string("Za^B8g@E2jH*kWl!MoPqXr7YvT1c$Fs3Ud9IwZ&yX0pLkV6sHqN^tB4rA+oZ%gFj"))



def can_organize_books(shelf):
    book_counts = Counter(shelf)

    frequencies = list(book_counts.values())
    gcd_value = frequencies[0]
    
    for count in frequencies[1:]:
        gcd_value = math.gcd(gcd_value, count)

    if gcd_value > 1:
        return "YES"
    else:
        return "NO"

shelf = [1234567, 1234567, 2345678, 2345678, 3456789, 3456789, 1234567, 2345678,
          3456789, 4567890, 4567890, 5678901, 5678901, 6789012, 6789012, 1234567, 
          2345678, 3456789, 4567890, 5678901, 4567890, 5678901]
print(can_organize_books( shelf))

