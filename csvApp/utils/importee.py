import csv
import re
from pathlib import Path

re_csv = r'\.csv$'
re_txt = r'\.txt$'


regex =(re.compile(re_txt),
        re.compile(re_csv)) 


def file_inputer(file_path):
    input_file = file_path
    csv_list = []
    for reg_obj in regex:
        match = reg_obj.search(str(input_file))
    if match: 
        with open(str(input_file), mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',') #if txt use , delimiter
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    names = [e for e in row]
                    line_count += 1
                else:
                    csv_dict = {}
                    for i in names:
                        csv_dict[i] = row[i]
                    csv_list.append(csv_dict)      
                    line_count += 1      
        return names, csv_list
    else:
        empty_dict = {}
        return csv_list, empty_dict    
if __name__ == '__main__':
    file_inputer(file)