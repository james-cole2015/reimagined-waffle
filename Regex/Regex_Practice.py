# Regex_Practice.py

import pandas as pd
import re

fileName = 'CS_data.txt'

_file = open(fileName,encoding='utf-8').read()

# This will remove all \u200e (non-visible) strings from the file. 
_file = re.sub('\u200e','',_file)

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
phone_matches = pattern.finditer(_file)

phoneNumbers = []
for match in phone_matches:
    p_number = match.group()
    phoneNumbers.append(p_number)

phoneSeries = pd.Series(phoneNumbers)

emailAddress = []

pattern = re.compile(r'[A-Za-z0-9.-]+@[A-Za-z-]+\.[A-Za-z0-9.]+')
email_matches = pattern.finditer(_file)

for match in email_matches:
    #print(match)
    eMail = match.group()
    emailAddress.append(eMail)

emailSeries = pd.Series(emailAddress)

pattern = re.compile(r'([A-Z][a-z]+)\s([A-Z][a-z-]+[A-Z]?[a-z]?[a-z]+)')
name_matches = pattern.finditer(_file)

f_names_list = []
l_names_list = []
names_list = []

for match in name_matches:
    #print(match)
    f_names = match.group(1)
    f_names_list.append(f_names)
    l_names = match.group(2)
    l_names_list.append(l_names)

for name in f_names_list:
    if name == 'Vice':
        f_names_list.remove('Vice')
    if name == 'South':
        f_names_list.remove('South')

for name in l_names_list:
    if name == 'City':
        l_names_list.remove('City')
    if name == 'Park':
        l_names_list.remove('Park')


firstNameSeries = pd.Series(f_names_list)
lastNameSeries = pd.Series(l_names_list)


pattern = re.compile("(\d{3})(\s)([0-9][a-z]+|[A-Z][a-z]+)(\s)(\w{2,9})([.,]+)(\s)([A-Z][a-z']+\s[A-Z][a-z-]+|[A-Z][a-z-]+)(\s)([A-Z]{2})(\s)(\d{5})")
address_matches = pattern.finditer(_file)

street_num_name_list = []
city_list = []
state_list = []
zip_list = []


for match in address_matches:
    #print(match.group(8))
    num_street_list = f'{match.group(1)} {match.group(3)} {match.group(5)}'
    street_num_name_list.append(num_street_list)
    #print(match.group(8))
    city = match.group(8)
    city_list.append(city)
    state = match.group(10)
    state_list.append(state)
    zip = match.group(12)
    zip_list.append(zip)


""" print(len(zip_list)) """

streetAddressSeries = pd.Series(street_num_name_list)
citySeries = pd.Series(city_list)
zipSeries = pd.Series(zip_list)
stateSeries = pd.Series(state_list)




dictA = {"First Name":firstNameSeries,"Last Name":lastNameSeries,
"Street Address":streetAddressSeries,'City':citySeries,'State':stateSeries,
'Zipcode':zipSeries}


""" df = pd.DataFrame(dictA)
print(df) """