import json


class Converter:
    __file = None
    __table_name = None

    def __init__(self, file, table_name):
        self.__file = file
        self.__table_name = table_name

    def __write_file(self, content):
        file = open("data.sql", "w")
        file.write(content)
        file.close()

    def get_file(self):
        return self.__file

    def get_table_name(self):
        return self.__table_name

    def read_file(self):
        file = open(self.get_file())
        data = json.load(file)
        file.close()

        return data
    
    def convert(self):
        data = self.read_file()
        sql = f"INSERT INTO {self.get_table_name()} (name, dial_code, code) VALUES\n"

        for item in data:
            sql += "\t(\"" + item["name"] + "\", "
            sql += "\"" + item["dial_code"] + "\", "
            sql += "\"" + item["code"] + "\"),\n"

        sql = sql[:-2] + ";"

        self.__write_file(sql)
