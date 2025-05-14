import sys
import re

def split_by_commas_except_in_strings(s):
    return [x.strip('"') for x in re.findall(r'"[^"]*"|[^,]+', s)]

def read_contents(path: str):
    with open(path) as f:
        file_string: str = f.read()
        array_two_d: list = file_string.split("\n")
        for i in range(len(array_two_d)):
            array_two_d[i] = split_by_commas_except_in_strings(array_two_d[i])
        return array_two_d, file_string

def process_dollar_to_float(item_array):
    temp_array = item_array.split("$")
    temp2_array = temp_array[1].split(",")
    item_array = ""
    for i in range(len(temp2_array)):
        item_array += temp2_array[i]
        
    return item_array

def main():
    csv_array, file_string = read_contents(sys.argv[1])
    count = 0
    
    #print(file_string)
    
    for item in csv_array:
        if not "Account ID" in item:
            item[3] = process_dollar_to_float(item[3])
            item[4] = process_dollar_to_float(item[4])
        print(item)
        count += 1
        if count > 10:
            break
    
    
    
main()