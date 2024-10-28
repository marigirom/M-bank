import sqlite3 as sqlite



class FinanceDatabase:
    def __init__(self, account_number, account_pin=None):
        self.account_number = account_number
        self.connection_status = False
        try:
            self.con = sqlite.connect(database='userFinance', timeout=5, check_same_thread= True)


        except Exception as e:
            print(e.args)

    def creating_user(self):

        db_cursor = sqlite.Cursor(self.connection_status)

        # creating user table
        sql = """CREATE TABLE UserDetails (
                    USERNAME VARCHAR(50) NOT NULL, 
                    USER_ACCOUNT_NUMBER VARCHAR(240) NOT NULL PRIMARY KEY, 
                    PASSWORD INT NOT NULL );"""
        query_add_user = db_cursor.execute(sql)

        if query_add_user:
            print("added _created ")
        else:
            print("operation failed ")


    def user_account_creation(self):
        con = sqlite.connect(database="UserFinance")
        tb_cursor = sqlite.Cursor(con)

        sql1 = """
        INSERT INTO USERDETAILS VALUES(
            'lABAN', '1237', '1236'        
        );"""
        result_info = tb_cursor.execute(sql1)

        if result_info:
            print("we did it ")

    def get_account_name(self, account_number):
        user_details = sqlite.Cursor(self.con)
        sql_find_user_name = f"""
        SELECT USERNAME FROM USERDETAILS 
        WHERE USER_ACCOUNT_NUMBER = {account_number}
        """
        results = user_details.fetchall()
        for i in results:
            print(i)
        # username_is = user_details.fetchall(sql_find_user_name)








obj1 = FinanceDatabase('1234')
# obj1.creating_user()
# obj1.user_account_creation()
obj1.get_account_name(account_number='1237')
