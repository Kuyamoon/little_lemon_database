try:
    # get password
    from getpass import getpass
    import mysql.connector as connector
    # text color module
    from colorama import Fore, Style

except Exception as e:
    print(e)

    # trying to install mysql-connector-python
    from pip._internal import main as pipmain
    print("Trying to install mysql-connector-python...")
    pipmain(["install", "mysql-connector-python"])
    pipmain(["install", "colorama"])
    
    # text color module
    from colorama import Fore, Style
    from getpass import getpass
    import mysql.connector as connector
    

def get_user_info():
    user_name = input(Fore.LIGHTYELLOW_EX+"Please enter MySQL user name:\n"+Fore.RESET)
    password = getpass(Fore.LIGHTYELLOW_EX+"Please enter MySQL password:\n"+Fore.RESET)

    dbconfig = {
        'user': user_name,
        'password': password,
    }
    return dbconfig

def drop_database(cursor, db_name):
    try:
        print(Fore.RED+"-------------------"+Fore.RESET)
        print(Fore.RED+"Droping Database..."+Fore.RESET)
        print(Fore.RED+"-------------------"+Fore.RESET)

        sql = f"DROP DATABASE {db_name};"
        cursor.execute(sql)
    except Exception as e:
        print(e)

def create_database(cursor, db_name):
    sql = f"CREATE DATABASE {db_name};"
    try:
        print(Fore.GREEN+"-------------------------------------------"+Fore.RESET)
        print(Fore.GREEN+f"Creating database '{db_name}'"+Fore.RESET)
        print(Fore.GREEN+"-------------------------------------------"+Fore.RESET)

        cursor.execute(sql)

    except Exception as e:
        print(e)
        drop_database(cursor=cursor, db_name=db_name)
        create_database(cursor=cursor, db_name=db_name)

def create_table(cursor):
    try:
        sql_list = {
            # Customers
            'Customers':'''CREATE TABLE Customers(
                CustomerID INT AUTO_INCREMENT PRIMARY KEY,
                CustomerName VARCHAR(255) NOT NULL,
                ContactNumber VARCHAR(50),
                Email VARCHAR(255)
                );''',
                
            # Menus
            'Menus':'''CREATE TABLE Menus(
                MenuID INT AUTO_INCREMENT PRIMARY KEY,
                MenuName VARCHAR(100) NOT NULL,
                MenuType VARCHAR(50) NOT NULL,
                MenuPrice DECIMAL(10,2) NOT NULL
                );''',
            
            # Bookings
            'Bookings':'''CREATE TABLE Bookings(
                BookingID INT AUTO_INCREMENT PRIMARY KEY,
                CustomerID INT,
                ReserveDate DATETIME NOT NULL,
                MenuID INT,
                Quantity INT NOT NULL,
                TotalPrice DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
                ON DELETE CASCADE
                ON UPDATE CASCADE,
                FOREIGN KEY (MenuID) REFERENCES Menus (MenuID)
                ON DELETE CASCADE
                ON UPDATE CASCADE
                );'''}
        
        for table in sql_list:
            cursor.execute(sql_list.get(table))
            print(Fore.GREEN+f"Create {table} table success."+Fore.RESET)

        table_list = sql_list.keys()
        print('\n')
    
    except Exception as e:
        print(e)
        drop_tables(cursor=cursor, table_list=table_list)
        create_table(cursor=cursor)
        

def drop_tables(cursor, table_list):
    for table in table_list:
        cursor.execute(f"DROP TABLE {table};")
        print(Fore.RED+f"{table} has been dropped."+Fore.RESET)

def insert_datasets(cursor, conn):
    sql_list = {
        'Customers':'''INSERT INTO Customers (CustomerName, ContactNumber, Email)
            VALUES
            ('John Doe', '555-1234-5678', 'johndoe@example.com'),
            ('Jane Smith', '555-2345-6789', 'janesmith@example.com'),
            ('Mike Johnson', '555-3456-7890', 'mikejohnson@example.com'),
            ('Emily Wilson', '555-4567-8901', 'emilywilson@example.com'),
            ('David Brown', '555-5678-9012', 'davidbrown@example.com'),
            ('Linda Davis', '555-6789-0123', 'lindadavis@example.com'),
            ('Robert Lee', '555-7890-1234', 'robertlee@example.com'),
            ('Mary Martin', '555-8901-2345', 'marymartin@example.com'),
            ('Michael Taylor', '555-9012-3456', 'michaeltaylor@example.com'),
            ('Jennifer Harris', '555-0123-4567', 'jenniferharris@example.com'),
            ('William Clark', '555-1234-5678', 'williamclark@example.com'),
            ('Patricia Lewis', '555-2345-6789', 'patricialewis@example.com'),
            ('Richard Hall', '555-3456-7890', 'richardhall@example.com'),
            ('Jessica Young', '555-4567-8901', 'jessicayoung@example.com'),
            ('Thomas Walker', '555-5678-9012', 'thomaswalker@example.com'),
            ('Barbara Turner', '555-6789-0123', 'barbaraturner@example.com'),
            ('Daniel White', '555-7890-1234', 'danielwhite@example.com'),
            ('Susan Jackson', '555-8901-2345', 'susanjackson@example.com'),
            ('Matthew Moore', '555-9012-3456', 'matthewmoore@example.com'),
            ('Sarah Baker', '555-0123-4567', 'sarahbaker@example.com'),
            ('Joseph Green', '555-1234-5678', 'josephgreen@example.com'),
            ('Nancy Allen', '555-2345-6789', 'nancyallen@example.com'),
            ('Charles King', '555-3456-7890', 'charlesking@example.com'),
            ('Karen Scott', '555-4567-8901', 'karenscott@example.com'),
            ('Andrew Adams', '555-5678-9012', 'andrewadams@example.com'),
            ('Lisa Roberts', '555-6789-0123', 'lisaroberts@example.com'),
            ('Mark Turner', '555-7890-1234', 'markturner@example.com'),
            ('Betty Rodriguez', '555-8901-2345', 'bettyrodriguez@example.com'),
            ('Steven Carter', '555-9012-3456', 'stevencarter@example.com'),
            ('Megan Hall', '555-0123-4567', 'meganhall@example.com');
            ''',
        'Menus': '''INSERT INTO Menus (MenuName, MenuType, MenuPrice)
            VALUES
            ('Hamburger', 'Burger', 5.99),
            ('Cheeseburger', 'Burger', 6.49),
            ('Chicken Sandwich', 'Sandwich', 7.99),
            ('Fish and Chips', 'Seafood', 9.99),
            ('Caesar Salad', 'Salad', 8.49),
            ('Chicken Caesar Salad', 'Salad', 9.99),
            ('Margherita Pizza', 'Pizza', 11.99),
            ('Pepperoni Pizza', 'Pizza', 12.99),
            ('Spaghetti Bolognese', 'Pasta', 10.99),
            ('Fettuccine Alfredo', 'Pasta', 11.99),
            ('French Fries', 'Side', 3.49),
            ('Onion Rings', 'Side', 4.99),
            ('Milkshake', 'Beverage', 4.99),
            ('Coca-Cola', 'Beverage', 2.49),
            ('Pepsi', 'Beverage', 2.49),
            ('Iced Tea', 'Beverage', 2.49),
            ('Lemonade', 'Beverage', 2.49),
            ('Coffee', 'Beverage', 1.99),
            ('Hot Chocolate', 'Beverage', 3.49),
            ('Mojito', 'Cocktail', 7.99),
            ('Margarita', 'Cocktail', 7.99),
            ('Cosmopolitan', 'Cocktail', 8.99),
            ('Beer', 'Alcohol', 5.49),
            ('Wine', 'Alcohol', 7.99),
            ('Sushi Roll', 'Sushi', 14.99),
            ('Sashimi', 'Sushi', 16.99),
            ('Tempura', 'Sushi', 9.99),
            ('Miso Soup', 'Soup', 3.49),
            ('Tomato Soup', 'Soup', 4.49),
            ('Ice Cream', 'Dessert', 4.99);
            ''',
        'Bookings':'''INSERT INTO Bookings (CustomerID, ReserveDate, MenuID, Quantity, TotalPrice)
            VALUES
            (1, '2023-01-01 12:30:00', 1, 2, 0),
            (2, '2023-01-02 18:00:00', 5, 1, 0),
            (3, '2023-01-03 19:30:00', 10, 2, 0),
            (4, '2023-01-04 13:45:00', 12, 1, 0),
            (5, '2023-01-05 20:15:00', 20, 3, 0),
            (6, '2023-01-06 17:30:00', 24, 2, 0),
            (7, '2023-01-07 12:00:00', 6, 2, 0),
            (8, '2023-01-08 19:15:00', 15, 1, 0),
            (9, '2023-01-09 15:45:00', 8, 3, 0),
            (10, '2023-01-10 14:00:00', 19, 1, 0),
            (11, '2023-01-11 18:30:00', 18, 2, 0),
            (12, '2023-01-12 20:45:00', 28, 1, 0),
            (13, '2023-01-13 16:30:00', 26, 2, 0),
            (14, '2023-01-14 14:45:00', 25, 1, 0),
            (15, '2023-01-15 19:00:00', 30, 3, 0),
            (16, '2023-01-16 12:15:00', 27, 2, 0),
            (17, '2023-01-17 17:30:00', 3, 2, 0),
            (18, '2023-01-18 15:00:00', 9, 1, 0),
            (19, '2023-01-19 13:45:00', 16, 3, 0),
            (20, '2023-01-20 18:00:00', 2, 1, 0),
            (21, '2023-01-21 19:30:00', 11, 2, 0),
            (22, '2023-01-22 17:45:00', 7, 1, 0),
            (23, '2023-01-23 20:15:00', 4, 3, 0),
            (24, '2023-01-24 16:30:00', 17, 2, 0),
            (25, '2023-01-25 14:15:00', 13, 2, 0),
            (26, '2023-01-26 19:00:00', 29, 1, 0),
            (27, '2023-01-27 12:45:00', 21, 2, 0),
            (28, '2023-01-28 15:30:00', 22, 1, 0),
            (29, '2023-01-29 18:30:00', 23, 3, 0),
            (30, '2023-01-30 20:00:00', 14, 1, 0);
            '''}
    
    for sql in sql_list:
        print(Fore.GREEN+f"Insert datas into {sql}"+Fore.RESET)
        cursor.execute(sql_list.get(sql))
        conn.commit()
    print('\n')

    # calculate totalPrice -_-a
    total_price = """
        UPDATE Bookings AS b
        INNER JOIN Menus AS m
        ON m.MenuID = b.MenuID
        SET TotalPrice = m.MenuPrice * b.Quantity;"""
    cursor.execute(total_price)
    conn.commit()


def create_procedures(cursor):
    procedures = {
    'GetMaxQuantity' : '''
        CREATE PROCEDURE GetMaxQuantity()
        BEGIN
            SELECT MAX(Quantity) AS "MAX Quantity" FROM Bookings;
        END;
        ''',
    'ManageBooking':'''
        CREATE PROCEDURE ManageBooking(IN Date DATETIME)
        BEGIN
            SELECT * FROM Bookings WHERE ReserveDate = Date;
        END;
        ''',
    'UpdateBooking':'''
        CREATE PROCEDURE UpdateBooking(IN NewDate DATETIME, IN Email VARCHAR(255))
        BEGIN
            UPDATE Bookings AS b
            INNER JOIN Customers AS c ON c.Email = Email
            SET b.ReserveDate = NewDate;
        END;
        ''',
    'AddBooking':'''
        CREATE PROCEDURE AddBooking(IN CustomerName VARCHAR(255), IN Date DATETIME, IN food INT, IN Quantity INT)
        BEGIN
            DECLARE CustomerID INT;
            DECLARE TotalPrice DECIMAL(10,2);
            SELECT CustomerID = CustomerID FROM Customers WHERE CustomerName = CustomerName;
            SET TotalPrice = (SELECT MenuPrice FROM Menus WHERE MenuID = food) * Quantity;
            INSERT INTO Bookings (CustomerID, ReserveDate, MenuID, Quantity, TotalPrice)
            VALUES (CustomerID, Date, MenuID, Quantity, TotalPrice);
        END;

        ''',
    'CancelBooking':'''
        CREATE PROCEDURE CancelBooking(IN mail VARCHAR(255))
        BEGIN
            DELETE FROM Bookings WHERE BookingID = (
                SELECT b.BookingID FROM Bookings AS b
                INNER JOIN Customers AS c
                ON b.CustomerID = c.CustomerID 
                WHERE c.Email = mail);
        END;

        '''
    }


    try:
        # create Procedures
        for procedure in procedures:
            cursor.execute(procedures.get(procedure))
            print(Fore.GREEN+f"{procedure} created successfully."+Fore.RESET)

    except Exception as e:
        print(e)
        print(Fore.RED+"Droping 'All' procedures."+Fore.RESET)
        drop_procedures(p_list=procedures, cursor=cursor)
        print(Fore.GREEN+"Try to create procedures."+Fore.RESET)
        create_procedures(cursor=cursor)



def drop_procedures(p_list, cursor):
    for p in p_list:
        cursor.execute(f"DROP PROCEDURE IF EXISTS {p};")
        print(Fore.RED+f"{p} droped successfully."+Fore.RESET)

if __name__ == '__main__':
    
    try:
        dbconfig = get_user_info()
        # connection and cursor generate
        connection = connector.connect(**dbconfig)
        cursor = connection.cursor()
        dbconfig['database'] = input(Fore.LIGHTYELLOW_EX+"Please enter database name:\n'(Default: little_lemon_database)'\n"+Fore.RESET)
        # default
        if dbconfig['database'] == "":
            dbconfig['database'] = "little_lemon_database"

        # create database and check
        db_name = dbconfig["database"]
        create_database(cursor, db_name=db_name)
        cursor.execute(f"use {db_name};")

        print(Fore.CYAN+f"\nCurrent database is '{connection.database}'\n"+Fore.RESET)

        # create table
        create_table(cursor=cursor)

        # insert simple data
        insert_datasets(cursor=cursor, conn=connection)

        # create procedures
        create_procedures(cursor)

        # run procedures
        print(Fore.LIGHTCYAN_EX+"Running 'GetMaxQuantity' procedure"+Fore.RESET)
        cursor.callproc("GetMaxQuantity")
        results = next(cursor.stored_results())
        data = results.fetchall()
        print(data)

        # callproc("procedure_name", ('parameterss', 'as', 'sequence',))
        print(Fore.LIGHTCYAN_EX+"Running 'ManageBooking' procedure"+Fore.RESET)
        cursor.callproc("ManageBooking", ('2023-01-20 18:00:00',))
        results = next(cursor.stored_results())
        for result in results.fetchall():
            print(result)

        # UpdateBooking
        # UpdateBooking(IN NewDate DATETIME, IN Email VARCHAR(255))
        print(Fore.LIGHTCYAN_EX+"Running 'UpdateBooking' procedure"+Fore.RESET)
        cursor.execute("""SELECT * FROM Bookings AS b
                       INNER JOIN Customers AS c 
                       ON b.CustomerID = c.CustomerID
                       WHERE c.Email = 'johndoe@example.com'; """)
        print(cursor.fetchall())
        
        cursor.callproc("UpdateBooking", ('2023-12-25 19:00:00', 'johndoe@example.com',))
        
        cursor.execute("""SELECT * FROM Bookings AS b
                       INNER JOIN Customers AS c 
                       ON b.CustomerID = c.CustomerID
                       WHERE c.Email = 'johndoe@example.com'; """)
        print(cursor.fetchall())
        
        # AddBooking
        # AddBooking(IN CustomerName VARCHAR(255), IN Date DATETIME, IN MenuID INT, IN Quantity INT)
        print(Fore.LIGHTCYAN_EX+"Running 'AddBooking' procedure"+Fore.RESET)

        # check
        cursor.execute("""SELECT COUNT(BookingID) FROM Bookings;""")
        print(cursor.fetchall())

        cursor.callproc("AddBooking", ('Test Man', '2023-12-25 18:30:00', 27, 2,))
        # check
        cursor.execute("""SELECT COUNT(BookingID) FROM Bookings;""")
        print(cursor.fetchall())

        # CancelBooking
        # CancelBooking(IN Email VARCHAR(255))
        print(Fore.LIGHTCYAN_EX+"Running 'CancelBooking' procedure"+Fore.RESET)
        
        # check
        cursor.execute("""SELECT COUNT(BookingID) FROM Bookings;""")
        print(cursor.fetchall())
        
        cursor.callproc("CancelBooking", ("johndoe@example.com",))

        # check
        cursor.execute("""SELECT COUNT(BookingID) FROM Bookings;""")
        print(cursor.fetchall())

        
        print(Fore.RED+"It'd be next time to make pooling something.. -_-"+Fore.RESET)
        print(Fore.LIGHTRED_EX+"Byebye Long Journey!"+Fore.RESET)

        cursor.close()
        connection.close()
        
    except Exception as e:
        print(e)
        cursor.close()
        connection.close()
        

    

