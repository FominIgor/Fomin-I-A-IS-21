


import sqlite3
import sys




def auth():

    auth = input("введите свои права:")

    names = {
        "админ":"админ"
    }

    for k,v in names.items():

        if k == auth:
            return k
        else:
            sys.exit()


def main():

    
    n1 = input('select tabeles:')
    if n1 == '1':
        sys.exit()
    return n1.replace(' ','')

#теперь можно запарить себе мозги каждый раз вписывая путь до бд 


qwe = '/home//rab/db/автосервис/autoservice.db'


def communication_user():

    main_question = main()
    try:
        question1 = input("Enter whether sorting is needed: ")
    except UnicodeDecodeError:
        print('возникла ошибка')
        main()


    if question1 == "yes" or question1 == "да":

        question2 = input("enter which column to sort by: ")

        question3 = input("sort in descending(DESC) or ascending(ASC) order:")

        return (f" SELECT * FROM '{main_question}' ORDER BY {question2.replace(' ','')} {question3.replace(' ','')};")
    
    if question1 == 'no' or question1 == "нет":
        return (f" SELECT * FROM  '{main_question}'")
    
    else:
        main()
    


def out_put_base_date(x):

    auth()

    while True:
        n = sqlite3.connect(x)
        
        cur = n.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
        
        try:
            
            name_colums = []
             
            res = cur.execute(communication_user())
            for data in res.description:
                name_colums.append(data[0])
            print(f'{name_colums}')
                
            for i, row in enumerate(res):
                print(row)
                
        except sqlite3.OperationalError:
            out_put_base_date(qwe)


out_put_base_date(qwe)