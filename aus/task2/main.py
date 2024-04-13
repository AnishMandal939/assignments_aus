def search_word_occurrences(file_name, word):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        content = "".join(lines).lower()
        count = content.count(word)
        return count

def main():
    file_name = "alice_in_wonderland.txt"
    print("Reading the content of the file...")
    with open(file_name, 'r') as file:
        lines = file.readlines()
    print("Content read successfully!")

    print("Enter a word to count its occurrences in the book or type 'exit' to end.")
    while True:
        user_input = input("Please enter a word: ")
        if user_input.lower() == "exit":
            print("END!")
            break
        else:
            count = search_word_occurrences(file_name, user_input.lower())
            print(f"The word '{user_input}' appears {count} times in this book")

if __name__ == "__main__":
    main()

