for num in range(5):

    predict_file = open('predict' + str(num) + '.txt', 'r').readlines()

    all_count = 0
    concord_count = 0
    correct_count = 0
    correct_match_count = 0
    for line in predict_file:
        all_count += 1
        correct, predict, prob = line.split('\t')
        if correct == predict:
            concord_count += 1
        if correct == '1':
            correct_count += 1
            if correct == predict:
                correct_match_count += 1

    print 'roop:', num
    print 'rate of concordance:', concord_count / float(all_count)
    pre = correct_match_count / float(all_count)
    rec = correct_match_count / float(correct_count)
    print 'Precision:', pre
    print 'Recall:', rec
    print 'F-measure:', 2 * rec * pre / (rec + pre)
    print ''
