# coding:utf-8


def cipher(message):
    return "".join([char if not char.isalpha() or not char.islower()
                    else unichr(219 - ord(char)).encode("utf-8") for char in message])


def decode(message):
    return "".join([char if not char.isalpha() or not char.islower()
                    else unichr(219 - ord(char)).encode("utf-8") for char in message])


def main():
    original_message = "Now I need a drink, alcoholic of course, " \
                       "after the heavy lectures involving quantum mechanics."
    coded_message = cipher(original_message)
    decoded_message = decode(coded_message)
    print "original_message:", original_message
    print "coded_message:   ", coded_message
    print "decoded_message: ", decoded_message


if __name__ == '__main__':
    main()
