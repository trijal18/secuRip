import random
import string
import pandas as pd
import selenium

names=pd.read_csv(r"D:\projects\secuRIP\Indian-Male-Names.csv") #path to dataset

def get_name():
     
    random_index = random.choice(names.index)
        
        # Retrieve the name at the randomly chosen index
    random_name = names.loc[random_index, 'Name']
        
    return str(random_name)

def get_email(name):
    # Remove spaces and convert the name to lowercase for the username
    username = ''.join(name.split()).lower()

    # Generate a random string of letters and digits to append to the username
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=4))

    # Generate a random domain for the email
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'aol.com', 'hotmail.com']
    domain = random.choice(domains)

    # Combine the username, random string, '@', and domain to form the email address
    email = f"{username}{random_string}@{domain}"

    return email

def get_number():
    # The first digit of the mobile number is between 7 and 9
    first_digit = random.randint(7, 9)
    
    # The remaining nine digits can be any number
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    
    # Combine the first digit and remaining digits to form the mobile number
    mobile_number = f"{first_digit}{remaining_digits}"

    return mobile_number


def genrate_usn():
    year=["22","21","23"]
    num=random.randint(10,99)
    branch=["CS","CY","AI","AL","EI","ME","IS","CI","EC"]
    usn=f"1MS{random.choice(year)}{random.choice(branch)}{num}"
    if "23" in usn:
        return usn+"-T"
    return usn

fake_students=pd.DataFrame(columns=["Name","Usn","mail","mobile"])

for i in range(500):
    name = get_name()
    h=[
             name,
             genrate_usn(),
             get_email(name),
            get_number()
                ]
    fake_students.loc[len(fake_students)]=h
  


