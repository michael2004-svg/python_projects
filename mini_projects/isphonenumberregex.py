import re
phonenumberregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumberregex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())