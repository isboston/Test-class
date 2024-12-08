def palindrome(word: str):
    if word == word[::-1]:
        return 'palindrome'
    else:
        return 'not palindrome'


words = ['abba', 'test', 'level']
for word in words:
    print(f'{word} is {palindrome(word)}')
