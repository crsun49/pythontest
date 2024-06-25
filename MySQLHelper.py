import pymysql

class MySQLHelper:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',  # 连接主机名
            user='root',       # 用户名
            password='root',   # 密码
            database='your_database'   # 数据库名
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute_update(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def execute_insert(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def execute_delete(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
#
# # 示例用法：
# # 创建一个MySQLHelper对象
# helper = MySQLHelper()
#
# # 查询数据
# result = helper.execute_query("SELECT * FROM your_table")
# for row in result:
#     print(row)
#
# # 插入数据
# insert_sql = "INSERT INTO your_table(col1, col2) VALUES('value1', 'value2')"
# helper.execute_insert(insert_sql)
#
# # 更新数据
# update_sql = "UPDATE your_table SET col1 = 'new_value' WHERE condition"
# helper.execute_update(update_sql)
#
# # 删除数据
# delete_sql = "DELETE FROM your_table WHERE condition"
# helper.execute_delete(delete_sql)
#
# # 关闭连接
# helper.close_connection()
