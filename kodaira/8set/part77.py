predict_file = open('predict_all.txt', 'r')

all_count = 0
concord_count = 0
correct_count = 0
correct_match_count = 0
for line in predict_file:
    all_count += 1
    print line
    correct, predict, prob = line.split('\t')
    if correct == predict:
        concord_count += 1
    if correct == '1':
        correct_count += 1
        if correct == predict:
            correct_match_count += 1




print 'rate of concordance:', concord_count / float(all_count)

pre = correct_match_count / float(all_count)
rec = correct_match_count / float(correct_count)
print 'Precision:', pre
print 'Recall:', rec
print 'F-measure:', 2 * rec * pre / (rec + pre)
