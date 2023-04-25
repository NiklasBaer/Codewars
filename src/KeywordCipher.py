def keyword_cipher(string, keyword):
    key = ''.join(sorted(set(keyword), key=keyword.index))
    
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in key:
            key += letter
    
    result = ''
    for letter in string:
        if letter.isalpha():
            result += key[ord(letter.lower()) - ord('a')]
        else:
            result += letter
    
    return result