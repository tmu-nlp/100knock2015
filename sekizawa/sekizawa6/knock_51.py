#!usr/bin/python

if __name__ == "__main__":
    input_file =  open("output_50.txt", "r")
    output_file = open("output_51.txt", "w")

    for line in input_file:
        terms = line.split(" ")
        for term in terms:
            print term
            output_file.write(term + "\n")

    input_file.close()
    output_file.close()
