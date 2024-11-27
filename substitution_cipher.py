'''
    Programmer:     Sayed Abdul Ahad Ibrahimi
    Date:           09/10/2023
    Class:          COMP-375 (Computer Security)
    Description:    
                    This program allows users to perform text encryption and decryption using a substitution cipher. It reads a key file to determine character mappings, accepts input text from a file, and produces encrypted or decrypted text as output. Users can specify the operation (encrypt or decrypt) and the input files, with results saved to corresponding output files.
'''

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_char = key[ord(char) - ord('a')]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            decrypted_char = chr(key.index(char) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def read_key_file(key_file):
    key = ""
    with open(key_file, 'r') as file:
        for line in file:
            columns = line.strip().split(' ')
            if len(columns) > 1:
                key += columns[1]
    return key.strip()


def read_input_file(input_file):
    with open(input_file, "r") as file:
        return file.read()


def write_output_file(output_file, result):
    with open(output_file, "w") as file:
        file.write(result)


def main():

    operation = input("Enter 'encrypt' or 'decrypt': ")
    key_file = input("Enter the name of the key file: ")
    input_file = input("Enter the name of the input file: ")

    key = read_key_file(key_file)

    text = read_input_file(input_file)

    if operation == 'encrypt':
        result = encrypt(text, key)
        output_file = "encrypted-text.txt"
    elif operation == 'decrypt':
        result = decrypt(text, key)
        output_file = "decrypted-text.txt"
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
        return

    write_output_file(output_file, result)

    print(f"Operation completed. Result written to {output_file}.")


if __name__ == "__main__":
    main()
