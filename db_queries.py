class DB_Queries:

    def db_current_height(self, cnx):
        cursor = cnx.cursor()
        query = ("select current_height from config")
        cursor.execute(query)

        for (current_height) in cursor:
            height = current_height

        cursor.close()
        return height[0]

    def save_weight_data_2db(self, today_date, weight, bmi, cnx):
        cursor = cnx.cursor()
        query = ("INSERT INTO weight_his "
                 "(date, weight, bmi) "
                 "VALUES(%s, %s, %s)")
        weight_data = (today_date, weight, bmi)
        cursor.execute(query, weight_data)
        id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        return id