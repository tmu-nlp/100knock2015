#!usr/bin/python


def print_np(word_list, begin):
    if 'NP' in word_list[begin]:
        count = 1
        for num in range(begin + 1, len(word_list) ):
            word = word_list[num]
            if '(' in word:
                count += 1
            elif ')' in word:
                count -= word.count(')')
                print word.replace(')', ''),
            if count < 1:
                break;
        print 


def main_roop(xml_name):
    parse_tag = '<parse>'
    for line in open(xml_name):
        if parse_tag in line:
            word_list = line.split()
            for begin in range(len(word_list) ):
                print_np(word_list, begin)
            print 



if __name__ == "__main__":
    file_name = "nlp.txt.xml"
    main_roop(file_name)
