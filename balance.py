import csv

def get_user(user_id):
    with open("UserData.csv", 'r') as file_content:
        content = list(file_content)
    
    check = -1
    count = 0
    bal_list = []
    for name_bal in content: # content is list of strings
        name_bal = name_bal.rstrip('\n') 
        nlist = name_bal.split(',')
        if nlist == ['']:
            continue
        if nlist[0] == str(user_id):
            check = count
        count += 1
        bal_list.append(nlist)
    
    return([bal_list, check])

def get_bal(user_id):
    credit_list = get_user(user_id)
    bal_list = credit_list[0]
    check = credit_list[1]

    with open("UserData.csv", 'a') as file_content:
        writer = csv.writer(file_content)
        if check == -1:
            writer.writerow([user_id, '0'])

    if check == -1:
        return '0'
    else:
        return bal_list[check][1]

def update_bal(user_id, credits):
    credit_list = get_user(user_id)
    bal_list = credit_list[0]
    check = credit_list[1]

    with open("UserData.csv", 'w') as file_content:
        writer = csv.writer(file_content)

        try:
            bal_list[check][1] = int(bal_list[check][1]) + int(credits)
            writer.writerows(bal_list)
        except(ValueError):
            pass