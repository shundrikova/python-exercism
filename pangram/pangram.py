def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if not letter in sentence.lower():
            return False
    return True
