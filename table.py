import psycopg2


class TABLES:
    def USER_TABLE(self, dbase):
        mycursor = dbase.cursor()
        #mycursor.execute("DROP TABLE IF EXISTS USER_table")
        mycursor.execute("CREATE TABLE USER_table (User_ID int ,"
                         "Email_ID varchar(30) ,"
                         " Password varchar(100),ROle varchar(20),Team_ID VARCHAR(50) NOT NULL PRIMARY KEY)")
        dbase.commit()

    def SERVER_TABLE(self, dbase):
        mycursor = dbase.cursor()

        #mycursor.execute("DROP TABLE IF EXISTS SERVER_table")
        mycursor.execute("CREATE TABLE SERVER_table (Server_ID int NOT NULL,"
                         "VENDOR varchar(50),BMC_IP VARCHAR(15) not null primary key ,"
                         "BMC_USER varchar(50),"
                         "BMC_password varchar(16),server_location varchar(50),CPU_GENERATION VARCHAR(50),"
                         "RESERVED VARCHAR(50),"
                         "ASSIGNED_TO VARCHAR(50),ASSIGNED_ON varchar(50),OS_IP VARCHAR(15),OS_USER VARCHAR(50),"
                         "OS_PASSWORD VARCHAR(16), PURPOSE VARCHAR(50), Team_ID VARCHAR(50) NOT NULL,"
                         "Cluster_ID VARCHAR(25),"
                         #"ADD CONSTRAINT FOREIGN KEY(Team_ID),"
                         "FOREIGN KEY(Team_ID) REFERENCES USER_table(Team_ID))")
        dbase.commit()

    def HISTORIC_TABLE(self, dbase):
        mycursor = dbase.cursor()

        #mycursor.execute("DROP TABLE IF EXISTS historic_table")
        mycursor.execute("CREATE TABLE historic_table (BMC_IP VARCHAR(15) primary key ,Team_ID VARCHAR(50),"
                         " USER_TYPE VARCHAR(50),"
                         " Assigned_from DATE, Assigned_to DATE ,"
                         "FOREIGN KEY(Team_ID) REFERENCES USER_TABLE(Team_ID))")
        dbase.commit()


dbase = psycopg2.connect(
    host='localhost',
    dbname='server_management',
    user='postgres',
    password='tomandjerry',
    port=5432
)
s = TABLES()
s.USER_TABLE(dbase)
s.SERVER_TABLE(dbase)
s.HISTORIC_TABLE(dbase)