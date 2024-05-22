def encrypt(text, shift):
    """Encrypts the text using Caesar Cipher with the given shift."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypts the text using Caesar Cipher with the given shift."""
    return encrypt(text, -shift)

def get_shift():
    """Get the shift value from user input (validating within 1-25)."""
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt or (q)uit? ").lower()
    while choice != 'q':
        text = input("Enter the text: ")
        shift = get_shift()
        if choice == 'e':
            result = encrypt(text, shift)
            print(f"Encrypted Text: {result}")
        elif choice == 'd':
            result = decrypt(text, shift)
            print(f"Decrypted Text: {result}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
        choice = input("Do you want to (e)ncrypt or (d)ecrypt or (q)uit? ").lower()

if __name__ == "__main__":
    main()
