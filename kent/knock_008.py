import sys

def cipher(text):
    new_text = ""
    for char in text:
        if char.islower():
            char = chr(219 - ord(char))
        new_text += char
    return new_text


if __name__  == "__main__":
    text = sys.stdin.readline()
    print cipher(text)
