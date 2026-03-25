alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shifted_amount, encode_or_decode):
    output = ""
    if encode_or_decode == "decode":
        shifted_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output += letter
        else:
            shifted_position = alphabet.index(letter) + shifted_amount

            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result {output}")


continue_or_not = True
while continue_or_not:
    direction = input("Type 'encode' to encrypt. Type 'decode' to decrypt: \n" ).lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shifted_amount=shift, encode_or_decode=direction)

    choose = input("Type 'yes' if you want to go again otherwise 'no':\n").lower()
    if choose == "no":
        continue_or_not = False
        print("Good Bye")