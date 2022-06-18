import sqlite3

db_name = 'from_zero'

conn = sqlite3.connect(db_name + '.db', check_same_thread=False)
cursor = conn.cursor()

def createtables():
    try:
        sql_create_t_fund = '''create table IF NOT EXISTS fund(
            FUND_NAME VARCHAR(20) PRIMARY KEY,
            STOCK_NAME_1 VARCHAR(20) NOT NULL,
            PROPORTIONATE_1 VARCHAR(20) NOT NULL,
            STOCK_NAME_2 VARCHAR(20) NOT NULL,
            PROPORTIONATE_2 VARCHAR(20) NOT NULL,
            STOCK_NAME_3 VARCHAR(20) NOT NULL,
            PROPORTIONATE_3 VARCHAR(20) NOT NULL,
            CREATE_TIME TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
            MODEFY_TIME TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime'))   
        ) '''
        cursor.execute(sql_create_t_fund)
    except Exception as e:
        print(repr(e))

createtables()

fundColumns = ("FUND_NAME","STOCK_NAME_1","PROPORTIONATE_1","STOCK_NAME_2","PROPORTIONATE_2","STOCK_NAME_3","PROPORTIONATE_3")

def addstaff(data):
    try:
        data = data[1:-1]
        data = data.split(',')
        result = ''
        keys = ''
        values = ''
        for list in data:
            key = list.split(':')[0]
            value = list.split(':')[1]
            keys += key
            keys += ','
            if isinstance(value,str):
                values += ("'%s'"%value)
                values += ','
            else:
                values += str(value)
                values += ','
        keys = keys[:-1]
        values = values[:-1]
        sql = "INSERT INTO fund (%s) values (%s)" % (keys,values)
        cursor.execute(sql)
        result = "添加成功"
        print(result)
        conn.commit()
        re = {
            'code': 0,
            'message': result
        }
        return re
    except Exception as e:
        print(repr(e))
        re = {
            'code': -1,
            'message': repr(e)
        }
        return re

def getStaffList(job):
    # 当job为0时，表示获取所有数据
    tableName = 'fund'
    where = ''

    columns = ','.join(fundColumns)
    order = ' order by FUND_NAME desc'  #按照id的递减顺序排列，之后要改
    sql = "select %s from %s%s%s" % (columns, tableName, where, order)
    print(sql)

    cursor.execute(sql)

    dateList = cursor.fetchall()     # fetchall() 获取所有记录
    return dateList

def getStaffsFromData(dataList):
    staffs = []
    for itemArray in dataList:   # dataList数据库返回的数据集，是一个二维数组
        #itemArray: ('1', '1', '2', '3', '4')
        staff = {}
        for columnIndex, columnName in enumerate(fundColumns):
            columnValue = itemArray[columnIndex]
            # if columnValue is None: #后面remarks要用，现在不需要
            #     columnValue = 0 if columnName in (
            #         'job', 'education', 'birth_year') else ''
            staff[columnName] = columnValue

        staffs.append(staff)

    return staffs