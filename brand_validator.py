def validate_card_brand(card_number: int) -> str:
    card_str = str(card_number)
    
    if len(card_str) != 16:
        return "Invalid card number length"
    
    if card_str.startswith(('4041', '4312', '4389')):
        return "Elo"
    elif card_str.startswith('4'):
        return "Visa"
    elif card_str.startswith(('51', '52', '53', '54', '55')):
        return "MasterCard"
    elif 2221 <= int(card_str[:4]) <= 2720:
        return "MasterCard"
    elif card_str.startswith(('34', '37')):
        return "American Express"
    elif card_str.startswith('6011') or card_str.startswith('65') or 644 <= int(card_str[:3]) <= 649:
        return "Discover"
    elif card_str.startswith('6062'):
        return "Hipercard"
    else:
        return "Unknown card brand"

def main():
    card_number = input("Enter the card number: ")
    try:
        card_number = int(card_number)
        result = validate_card_brand(card_number)
        print(f"Card brand: {result}")
    except ValueError:
        print("Invalid input. Please enter a numeric card number.")

if __name__ == "__main__":
    main()