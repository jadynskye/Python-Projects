#Word Encoder and Decoder
#By: Jadyn Reid

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt():

    original_text = input("Type the message that you want coded here: ").lower()
    shift_amount = int(input("What shall the shift amount be? "))

    new_code = ''

    for letter in original_text:
        if letter not in alphabet:
            new_code += letter
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            new_code += alphabet[shifted_position]

    print(f"Here is the encoded result: {new_code}")

def decrypt():
    decode_text = str(input("Type the message that you want to be decoded here: ").lower())
    shift_amount_2 = int(input("What shall the shift amount be? "))

    uncoded_code = ''

    for letter in decode_text:
        if letter not in alphabet:
            uncoded_code += letter
        if letter in alphabet:
            reversed_position = alphabet.index(letter) - shift_amount_2
            reversed_position %= len(alphabet)
            uncoded_code += alphabet[reversed_position]

    print(f"Here are the decoded results: {uncoded_code}")



#Main function that calls the rest
def main():
    wants_to_continue = True

    while wants_to_continue:
        #Welcome message 
        print("\nWelcome to Jadyn's Encoder and Decoder\n")
        #Users choice
        users_choice = input("Type 'encode' to encode a message and 'decode' to decode a message: ").lower()

        if users_choice == "encode":
            encrypt()
        elif users_choice == "decode":
         decrypt()
        else:
            print("Invalid choice. Please type 'encode' or 'decode'.")
        
        # Ask if user wants to go again
        user_wish = input("\nWould you like to encode or decode another message? Type 'yes' or 'no': ").lower()
        if user_wish == 'no':
            wants_to_continue = False
            print("Goodbye!")
main()

