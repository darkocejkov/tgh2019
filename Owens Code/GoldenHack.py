import pyodbc
# print([x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')])


#Policy Object
class policy_object():
    def __init__(self,pid, sponsor,policy_num, insurance_ID, company_name, typer, base_am, adj_am,desc):
        self.Policy_ID=pid
        self.Sponsor=sponsor
        self.Policy_Number=policy_num
        self.Insurance_ID = insurance_ID
        self.Company_Name = company_name
        self.Type = typer
        self.Base_Amount = base_am
        self.Adjusted_Amount = adj_am
        self.Description = desc

#User Object
class user_object():
    def __init__(self,uid,first, last, dob, email, address, country, province):
        self.User_ID = uid
        self.First_Name=first
        self.Last_Name=last
        self.DOB = dob
        self.Email=email
        self.Address=address
        self.Country=country
        self.Province=province

#Creates a user
def add_user(first_name, last_name,DOB,email,address,country,province):
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Code\IDS.accdb;'
        )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (First_Name,Last_Name,DOB,Email,Address,Country,Province) values (?,?,?,?,?,?,?)",
    first_name,last_name,DOB,email,address,country,province)
    conn.commit()

#Creates a policy at a user id
def create_policy(user_id,sponsor, policyNum, insurance_ID , company_name, typers, base_am,adj_am, desc ):
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Code\IDS.accdb;'
        )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Policy (Sponsor, Policy_Number, Insurance_ID, Company_Name, Type, Base_Amount, Adjusted_Amount, Description) values (?,?,?,?,?,?,?,?)",
     sponsor, policyNum, insurance_ID,company_name,typers,base_am,adj_am, desc)
    conn.commit()
    cursor.execute("SELECT @@IDENTITY")
    user_num = cursor.fetchone()[0]
    print(user_num)
    print(user_id)
    cursor.execute("INSERT INTO policy_user (User_ID, Policy_ID) values (?,?)",user_id,user_num)
    conn.commit()


#Delete a particular Policy
def delete_policy(policy_id):
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=C:\Code\IDS.accdb;'
        )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Policy where Policy_ID =?",policy_id)
    conn.commit()
    cursor.execute("DELETE FROM policy_user where Policy_ID=?", policy_id)
    conn.commit()


#Gets all policies attached to a user id
def get_all_policy(user_id):
    conn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Code\IDS.accdb;'
            )
    cursor = conn.cursor()
    policy_array=[]
    cursor.execute("SELECT Policy_ID FROM policy_user where User_ID=?",user_id)
    for val in cursor.fetchall():
        print(val[0])
        cursor.execute("SELECT * FROM Policy where Policy_ID=?",val)
        grabbed_policy= cursor.fetchone()
        to_return = policy_object(grabbed_policy[0],grabbed_policy[1],grabbed_policy[2],grabbed_policy[3],
        grabbed_policy[4],grabbed_policy[5],grabbed_policy[6],grabbed_policy[7],grabbed_policy[8])
        policy_array.append(to_return)
    return policy_array


#Gets all of a policy info and returns as object
def get_policy(policy_id):
    conn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Code\IDS.accdb;'
            )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Policy where Policy_ID=?',policy_id)
    grabbed_policy = cursor.fetchone()
    to_return = policy_object(grabbed_policy[0],grabbed_policy[1],grabbed_policy[2],grabbed_policy[3],
    grabbed_policy[4],grabbed_policy[5],grabbed_policy[6],grabbed_policy[7],grabbed_policy[8])
    return to_return

#Gets and returns user object of all user data at specified ID
def get_user_data(user_id):
    conn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Code\IDS.accdb;'
            )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User where User_ID=?",user_id)
    user_arr = []
    for val in cursor.fetchone():
        
        user_arr.append(val)
    
    to_return = user_object(user_arr[0],user_arr[1],user_arr[2],user_arr[3],user_arr[4],user_arr[5],user_arr[6],user_arr[7])
    return to_return


#Adjusts policy up or down
def adjust_policy(policy_id, amount):
    conn = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Code\IDS.accdb;'
            )
    cursor = conn.cursor()
    cursor.execute("SELECT Adjusted_Amount FROM Policy where Policy_ID=?", policy_id)
    the_val = cursor.fetchone()[0]
    the_val=int(the_val)
    the_val=the_val+amount
    cursor.execute("UPDATE Policy SET Adjusted_Amount=? where Policy_ID=?",the_val,policy_id)
    conn.commit()
    
    
# this is the testing

#create_policy(2,"Cooperators","34","18","The Co-operators Insurance Group Ltd","Health","1000","1000","Insurance health policy")
# add_user("Owen","Van Valkenburg","05/09/1998","placeholder@gmail.com","339 King Street North Waterloo","Canada","ON")
# delete_policy(11)
# print(get_policy(11))
#t=get_all_policy(2)
# adjust_policy(16,-1000)

