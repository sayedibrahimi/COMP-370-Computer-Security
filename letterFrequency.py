'''
    Programmer:     Sayed Abdul Ahad Ibrahimi
    Date:           09/10/2023
    Class:          COMP-375 (Computer Security)
    Description:    
                    The purpose of this program is to analyze the content of a text file and calculate the frequency of each alphabetic character (letters) within the file. It then sorts these letter frequencies in descending order and saves the results to a new text file named "letter_frequencies.txt." Finally, it prints a confirmation message indicating that the letter frequencies have been successfully written to the output file.
'''


def read_file_contents(file_name):
    with open(file_name, "r") as file:
        return file.read()


def calculate_letter_frequency(file_contents):
    letter_frequency = {}

    for char in file_contents:
        if char.isalpha():
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1
    return letter_frequency


def write_letter_frequencies(letter_frequency, output_file_name):
    sorted_letter_frequency = sorted(
        letter_frequency.items(), key=lambda x: x[1], reverse=True)

    with open(output_file_name, "w") as output_file:
        for letter, frequency in sorted_letter_frequency:
            output_file.write(f"{letter}: {frequency}\n")


def main():
    input_file_name = input("Enter the text file name: ")
    file_contents = read_file_contents(input_file_name)

    letter_frequency = calculate_letter_frequency(file_contents)

    output_file_name = "letter_frequencies.txt"
    write_letter_frequencies(letter_frequency, output_file_name)

    print("Letter frequencies written to", output_file_name)
