import pandas as pd
import re

fileName = '/Users/brooks/GitHub/PythonProjects/Tutorials/Regex/CS_data.txt'

_file = open(fileName,encoding='utf-8').read()

# This will remove all \u200e (non-visible) strings from the file. 
_file = re.sub('\u200e','',_file)

def phone_series_func():
    pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
    phone_matches = pattern.finditer(_file)

    phoneNumbers = []
    for match in phone_matches:
        p_number = match.group()
        phoneNumbers.append(p_number)

    phoneSeries = pd.Series(phoneNumbers)
    return phoneSeries

def email_series_func():
    emailAddressList = []
    pattern = re.compile(r'[A-Za-z0-9.-]+@[A-Za-z-]+\.[A-Za-z0-9.]+')
    email_matches = pattern.finditer(_file)

    for match in email_matches:
        eMail = match.group()
        emailAddressList.append(eMail)

    emailSeries = pd.Series(emailAddressList)
    return emailSeries

def names_func():
    f_names_list = []
    l_names_list = []

    pattern = re.compile(r'([A-Z][a-z]+)\s([A-Z][a-z-]+[A-Z]?[a-z]?[a-z]+)')
    name_matches = pattern.finditer(_file)

    for match in name_matches:
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
    return firstNameSeries, lastNameSeries


def address_func():
    pattern = re.compile("(\d{3})(\s)([0-9][a-z]+|[A-Z][a-z]+)(\s)(\w{2,9})" \
                         "([.,]+)(\s)([A-Z][a-z']+\s[A-Z][a-z-]+|[A-Z][a-z-]+)" \
                         "(\s)([A-Z]{2})(\s)(\d{5})")
    address_matches = pattern.finditer(_file)

    street_num_name_list = []
    city_list = []
    state_list = []
    zip_list = []

    for match in address_matches:
        num_street_list = f'{match.group(1)} {match.group(3)} {match.group(5)}'
        street_num_name_list.append(num_street_list)
        city = match.group(8)
        city_list.append(city)
        state = match.group(10)
        state_list.append(state)
        zip = match.group(12)
        zip_list.append(zip)

    streetAddressSeries = pd.Series(street_num_name_list)
    citySeries = pd.Series(city_list)
    zipSeries = pd.Series(zip_list)
    stateSeries = pd.Series(state_list)

    return streetAddressSeries,citySeries,zipSeries,stateSeries


def final_dataframe():
    email = email_series_func()
    phone = phone_series_func()
    first, last = names_func()
    street_add, city, zip, state = address_func()
    
    info_dict = {"First Name":first,"Last Name":last,"Street Address": 
    street_add,"City":city,"State":state,"Zip":zip,"Email Address":email,
    "Phone Number":phone}

    df = pd.DataFrame(info_dict)
    return df

pbook_data = final_dataframe()
print(pbook_data)
