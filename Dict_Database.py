# CREATE A DICTIONARY TO CONTAIN A PERSON : NAME, AGE, SEX, PHONE, ADDRESS  .......  AS ENTERED BY THE USER AND VALIDATED.
# ADDRESS SHOULD CONTAIN : HNO, STREET, ZONE, CITY, COUNTRY, PIN
con=True
while(con):
    name = input('Enter Name: ')
    if (name.isalpha()):
        pass
    else:
        print('Invalid Name, Please re-enter details\n')
        continue
    age = (input('Enter Age: '))
    if ((age.isdigit()) and int(age)>0):
        pass
    else:
        print('Invalid Age, Please re-enter details\n')
        continue
    sex = input('Enter Gender (M/F): ')
    sc = (sex=='M' or sex=='m' or sex=='F' or sex=='f' or \
    sex=='Male' or sex=='Female' or sex=='male' or sex=='female')
    if sc:
        pass
    else:
        print('Invalid Sex, Please re-enter details\n')
        continue
    pcon = input('Enter Contact No: ')
    if( (len(pcon)==10) and (pcon.isdigit()) and (pcon[0] in ['9', '8', '7']) ):
        pass
    else:
        print("Invalid Phone Number, Please re-enter details\n")
        print('*'*20)
        continue
    hno = input('House No:')
    strt = input('Street: ')
    zone = input('Zone: ')
    city = input('City: ')
    country = input('Country: ')
    pin = input('Pin: ')

    print()

    user_dict = dict(
        Name=name,
        Age=age,
        Sex=sex,
        Phone=pcon,
        Address=dict(
            House_No=hno,
            Street=strt,
            Zone=zone,
            City=city,
            Country=country,
            Pin=pin
        )
    )
    for key in user_dict:
        if not(key == 'Address'):
            print(key,"::",user_dict[key])
    print("Address :: ",end='')
    for key in user_dict['Address']:
        print(user_dict['Address'][key],end=' ')
    con=input('\n\nEnter 1 to add more, and 0 to stop: ')
    if con=='0':
        con=False

print('\n\nExiting Program... ')
