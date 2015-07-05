#!/usr/bin/python
# _*_ coding:utf-8 _*_

def main():
    labels_file =  open("output_76_raw2.txt")
    correct_list = list()
    predict_list = list()
    length = 0
    for line in labels_file:
        line = line.strip()

        correct, predict, probablity = line.split("\t")
        correct_list.append(correct)
        predict_list.append(predict)
        length += 1

    success = 0

    for correct, predict in zip(correct_list, predict_list):
      if correct == predict:
         success += 1

    precision = success/float(len(correct_list))
    recall    = success/float(len(predict_list))

    print success/float(length)
    print precision
    print recall
    print (2*precision*recall)/(precision+recall)


    labels_file.close()

if __name__=="__main__":
   main()
