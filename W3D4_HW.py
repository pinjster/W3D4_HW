"""
Function that intakes file name and regex pattern.
Returns string of valid and invalid counts according to pattern.
Included are two extra patterns:
exact_pattern patterns as the Google Doc HW shows, ie. first two lines.
my_pattern I made to show each record if it has at least a full name, age, and country, regardless the breaks. 
"""
import re

def validate_file(file_name, pattern):
    with open(f'./{file_name}') as records:
        data = records.readlines()

    valid_count = { 'valid' : 0 , 'invalid' : 0 }
    for line in data:
        info = pattern.match(line)           
        if info:
            print(f"Age: {info.group(2)}, Country: {info.group(3)}")
            valid_count['valid'] += 1
        else:
            print("Invalid record")
            valid_count['invalid'] += 1
    return f'valid: {valid_count["valid"]} invalid: {valid_count["invalid"]}'

exact_pattern = re.compile('([A-Z][a-z]+ [A-Z][a-z]+), ([0-9][0-9]), (United States|Canada)$')
desired_pattern = re.compile('([A-Z][a-z]+ [A-Z][a-z]+), ([0-9][0-9]), (([A-Z][a-z]+)( [A-Z][a-z]+)?)$')
my_pattern = re.compile('([A-Z][a-z]+ [A-Z][a-z]+)\W*([0-9][0-9])\W*(([A-Z][a-z]+)( [A-Z][a-z]+)?)$')

print(validate_file('user_records.txt', desired_pattern))