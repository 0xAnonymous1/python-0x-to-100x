# def calculate_love_score(name1, name2):
#     combined_names = name1.lower() + name2.lower()
#     love_score = 0

#     for char in combined_names:
#         love_score += ord(char)

#     return love_score % 100

# def main():
#     print("Welcome to the Love Score Calculator!")
#     name1 = input("Enter the first name: ")
#     name2 = input("Enter the second name: ")

#     score = calculate_love_score(name1, name2)
#     print(f"The love score between {name1} and {name2} is: {score}")

# if __name__ == "__main__":
#     main()

print("wellcome to the love calculator")
name1 = input("Enter your name 😎:").lower()
name2 = input("Enter their name 😍:").lower()
combine_string=name1+name2
lettercount=combine_string.count("a")
print(f"here is you and your lover {combine_string}")
print(f"hello your string count {lettercount}")
