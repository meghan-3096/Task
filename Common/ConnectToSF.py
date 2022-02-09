import snowflake.connector


class ConnectToSF:

    @staticmethod
    def connect_snowflake():

        conn = snowflake.connector.connect(
            user='meghanandi',
            password='Lumos@0921',
            account='ak75437.southeast-asia.azure',
            warehouse='TASK',
            database='TASK',
            schema='PUBLIC'
        )
        curs = conn.cursor()
        return curs
