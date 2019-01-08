import mysql.connector
def SQL(query):
    print(query)
    _cnx = mysql.connector.connect(user='user', password='Password123',database='test')
    _cur = _cnx.cursor()
    _cur.execute(query)
    if (query[0:6]=="SELECT"):
        _return=_cur.fetchall()
        if (len(_return)==0):
            return
        elif (len(_return)==1):
            _list=[]
            for i in range(len(_return[0])):
                _list.append(_return[0][i])
            return _list
        else:
            _list=[]
            for i in range(len(_return)):
                _list.append([])
                for j in range(len(_return[i])):
                    _list[i].append(_return[i][j])
            return _list
    elif (query[0:6]=="UPDATE" or query[0:6]=="INSERT"):
        _cnx.commit()
        _cnx.close()
        return
    else:
        _return=_cur.fetchall()
        _cnx.commit()
        _cnx.close()
        return _return
def SQL_getTables():
    tables=SQL("SHOW tables")
    list=[]
    for i in tables:
        list+=i
    return list
def SQL_getColonnes(table):
    _return=SQL("SHOW COLUMNS FROM {}".format(table))
    list=[]
    for i in range(len(_return)):
        list.append(_return[i][0])
    return list
def SQL_insertLine(table,values):
    return SQL("INSERT INTO {} values {}".format(table,values))
def SQL_getTable(table):
    return SQL("SELECT * FROM {}".format(table))