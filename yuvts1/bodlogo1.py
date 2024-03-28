def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


number_input = int(input())

if is_palindrome(number_input):
    print("Tiim")
else:
    print("ugui")
