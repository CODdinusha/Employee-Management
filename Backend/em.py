import pymysql
import calendar
import os

# Assuming your password environment variable is named 'Pass'
db_password = 'dinushA@727'

con = pymysql.connect(host="localhost", user='root', passwd=db_password, database='xiia')

cur1 = con.cursor()

def menu():
    print("\t\t\t-----------------------------------------------------------------------")
    print("\t\t\t**********************************MENU*********************************")
    print("\t\t\t-----------------------------------------------------------------------")
    print()
    print("\t\t\t***********************1. REGISTER NEW EMPLOYEES***********************")
    print("\t\t\t********************2. UPDATE DETAILS OF EMPLOYEES*********************")
    print("\t\t\t******************3. DISPLAY DETAILS OF AN EMPLOYEE********************")
    print("\t\t\t*************4. REMOVE AN EMPLOYEE WHO HAVE LEFT OFFICE****************")
    print("\t\t\t******************5. DISPLAY ALL EMPLOYEE DETAILS**********************")
    print("\t\t\t********6. DISPLAY DETAILS OF EMPLOYEES WHO HAVE LEFT THE OFFICE*******")
    print("\t\t\t******************7. DISPLAY SORTED EMPLOYEE DETAILS*******************")
    print("\t\t\t**********8. DISPLAY AVERAGE SALARY THAT AN EMPLOYEE RECEIVES**********")
    print("\t\t\t******************9. CREATE PAY SLIP OF AN EMPLOYEE********************")
    print("\t\t\t******************10. REMOVE ALL EMPLOYEE'S DETAILS********************")
    print("\t\t\t********************11. CREATE TABLE*********************")
    print("\t\t\t******************12. DISPLAY ALL TABLES****************")

def insert(office):
    while True:
        try:
            Id = input("enter emp_id: (should have unique value)")
            name = input("employee name: ")
            depar = input('enter department: ')
            desig = input('enter designation: ')
            sal = input('enter salary: ')
            mob = input("enter mob: ")
            doj = input("enter date of joining (yyyy-mm-dd): ")
            query = "INSERT INTO mdps VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            cur1.execute(query, (Id, name, depar, desig, sal, mob, doj, office))
            con.commit()
            print()
            print("\t\t\t\t*************EMPLOYEE REGISTERED SUCCESSFULLY ;^) ***********")
            print()
            ch = input('do you want to register more employees? y or n: ')
            if ch in 'nN':
                break
        except pymysql.err.IntegrityError:
            print('\t\t\t\t*****Employee ID already exists! Please enter a unique ID.*****')
        except:
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def update():
    while True:
        try:
            name = input("enter name of employee whose details are to be updated: ")
            query1 = "SELECT * FROM mdps"
            cur1.execute(query1)
            c = cur1.fetchall()
            for i in c:
                if i[1] == name:
                    print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining')
                    print()
                    c_field = input('enter field name to be updated: ')
                    new = input('enter new value: ')
                    query = f'UPDATE mdps SET {c_field}=%s WHERE emp_name=%s'
                    cur1.execute(query, (new, name))
                    con.commit()
                    print('\t\t\t\t*****DETAILS OF EMPLOYEE UPDATED SUCCESSFULLY ;^) *****')
            ch = input('do you want to update more ? y or n: ')
            if ch == 'n':
                break
        except:
            print("\t\t\t\t****enter a valid employee name, the one provided earlier doesn't exist :^( **** ")
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def search():
    while True:
        try:
            print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining')
            print()
            c = input('enter field name on whose basis you wish to display details of the employee: ')
            j = input('enter value: ')
            query = f'SELECT * FROM mdps WHERE {c}=%s'
            cur1.execute(query, (j,))
            k = cur1.fetchall()
            if len(k) == 0:
                print('\t\t\t\t\t*********EMPLOYEE DETAILS NOT FOUND**********')
            else:
                print("\t\t\t******************DISPLAYING DETAILS OF EMPLOYEE**********************")
                for i in k:
                    print("emp_id : ", i[0])
                    print("emp_name : ", i[1])
                    print("department : ", i[2])
                    print("designation : ", i[3])
                    print("salary : ", i[4])
                    print("mob : ", i[5])
                    print("date_of_joining : ", i[6])
                    print("office : ", i[7])
                    print('\n')
            ch = input('do you want to display more ? y or n: ')
            if ch in 'nN':
                break
        except:
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def delete():
    while True:
        try:
            a = input('enter employee id who have left the office: ')
            query = 'SELECT * FROM mdps WHERE emp_id=%s'
            cur1.execute(query, (a,))
            r = cur1.fetchall()
            if len(r) == 0:
                print('\t\t\t\t\t*********EMPLOYEE NOT FOUND**********')
            else:
                query1 = 'DELETE FROM mdps WHERE emp_id=%s'
                e, f, g, h, i, j, k, l = r[0]
                query3 = 'INSERT INTO DEL VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
                cur1.execute(query3, (e, f, g, h, i, j, k, l))
                cur1.execute(query1, (a,))
                print('\t\t\t\t**********EMPLOYEE REMOVED SUCCESSFULLY**********')
        except:
            print('\t\t\t\t*************************Sorry Not Possible :( *********************************')
        con.commit()
        ch = input('do you want to remove more employees ? y or n: ')
        if ch == 'n':
            break

def deleten():
    query = 'TRUNCATE TABLE mdps'
    cur1.execute(query)
    con.commit()
    print('\t\t\t**********ALL THE EMPLOYEE DETAILS ARE DELETED SUCCESSFULLY************')

def display_all():
    query = 'SELECT * FROM mdps'
    cur1.execute(query)
    k = cur1.fetchall()
    x = len(k)
    if x == 0:
        print('\t\t\t*NO EMPLOYEE DETAILS ARE ENTERED YET... INSERT ONE AND PROCEED*')
    else:
        print("\t\t\t******************DISPLAYING ALL EMPLOYEE DETAILS**********************")
        for i in k:
            print("emp_id : ", i[0])
            print("emp_name : ", i[1])
            print("department : ", i[2])
            print("designation : ", i[3])
            print("salary : ", i[4])
            print("mob : ", i[5])
            print("date_of_joining : ", i[6])
            print("office : ", i[7])
            print('\n')

def display_sorted():
    try:
        print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining, office')
        c = input('enter field name on whose basis sorting should be done: ')
        query = f'SELECT * FROM mdps ORDER BY {c}'
        cur1.execute(query)
        k = cur1.fetchall()
        x = len(k)
        if x == 0:
            print('\t\t\t*NO EMPLOYEE DETAILS ARE ENTERED YET... INSERT ONE AND PROCEED*')
        else:
            print("\t\t\t******************DISPLAYING SORTED EMPLOYEE DETAILS**********************")
            for i in k:
                print("emp_id : ", i[0])
                print("emp_name : ", i[1])
                print("department : ", i[2])
                print("designation : ", i[3])
                print("salary : ", i[4])
                print("mob : ", i[5])
                print("date_of_joining : ", i[6])
                print("office : ", i[7])
                print('\n')
    except:
        print('\t\t\t\t*****please retry, try to enter field name correctly****')

def display_left():
    query = 'SELECT * FROM DEL'
    cur1.execute(query)
    k = cur1.fetchall()
    x = len(k)
    if x == 0:
        print('\t\t\t*NO EMPLOYEE HAS LEFT THE OFFICE YET...*')
    else:
        print("\t\t\t******************DISPLAYING DETAILS OF EMPLOYEES WHO LEFT OFFICE**********************")
        for i in k:
            print("emp_id : ", i[0])
            print("emp_name : ", i[1])
            print("department : ", i[2])
            print("designation : ", i[3])
            print("salary : ", i[4])
            print("mob : ", i[5])
            print("date_of_joining : ", i[6])
            print("office : ", i[7])
            print('\n')

def avg():
    query = 'SELECT AVG(salary) FROM mdps'
    cur1.execute(query)
    k = cur1.fetchall()
    print('\t\t\t\t*************AVERAGE SALARY THAT AN EMPLOYEE RECEIVES IS********** : ', k[0][0])

def create_table():
    while True:
        try:
            table_name = input("Enter the name of the new table: ")
            columns = []
            while True:
                column_name = input("Enter column name (or 'done' to finish): ")
                if column_name.lower() == 'done':
                    break
                column_type = input("Enter column type (e.g., VARCHAR(255), INT, DATE): ")
                columns.append(f"{column_name} {column_type}")
            columns_str = ", ".join(columns)
            query = f"CREATE TABLE {table_name} ({columns_str})"
            cur1.execute(query)
            con.commit()
            print(f"Table '{table_name}' created successfully.")
            break
        except pymysql.MySQLError as e:
            print(f"Error creating table: {e}")
            con.rollback()

def display_tables():
    query = "SHOW TABLES"
    cur1.execute(query)
    tables = cur1.fetchall()
    if len(tables) == 0:
        print("No tables found in the database.")
    else:
        print("Tables in the database:")
        for table in tables:
            print(table[0])

while True:
    menu()
    choice = int(input("\t\t\tENTER YOUR CHOICE: "))
    if choice == 1:
        office = input('enter office: ')
        insert(office)
    elif choice == 2:
        update()
    elif choice == 3:
        search()
    elif choice == 4:
        delete()
    elif choice == 5:
        display_all()
    elif choice == 6:
        display_left()
    elif choice == 7:
        display_sorted()
    elif choice == 8:
        avg()
    elif choice == 9:
        create()
    elif choice == 10:
        deleten()
    elif choice == 11:
        create_table()
    elif choice == 12:
        display_tables()
    else:
        break
