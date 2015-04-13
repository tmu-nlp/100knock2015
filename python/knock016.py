'''
python knock016.py ../Data/hightemp.txt [out_dir] [n]
'''
import sys

if __name__ == '__main__':
    all_lines = list()
    dir_name = sys.argv[2]
    line_count = 0
    for line in open(sys.argv[1]):
        all_lines.append(line.strip())
        line_count += 1
    
    spl_num = -(-line_count / int(sys.argv[3]))
    file_count = 0
    for lines in (all_lines[i:i+spl_num] for i in range(0, len(all_lines), spl_num)):
        f = open('%s/split_file.%d.txt' % (dir_name, file_count), 'w')
        for line in lines:
            print >> f, line
        file_count += 1
