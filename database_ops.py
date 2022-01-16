import sqlalchemy as db

engine = db.create_engine('mysql://root@localhost:3306/Organization')

connection = engine.connect()



metadata = db.MetaData()
employees= db.Table('Employee', metadata, autoload=True, autoload_with=engine)


# where 

query =  db.select([employees]).where(employees.columns.departmentid == '301')
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

#IN

query = db.select([employees.columns.HRA, employees.columns.DA]).where(employees.columns.HRA.in_(['4000', '200']))
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

#order by
query = db.select([employees]).order_by(db.desc(employees.columns.department_id), employees.columns.basic_salary)
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)


#m = db.select([employees]).where(employees.columns.departmentid == '301')

#print(m)









'''
query = db.select([employees]).where(employees.columns.HRA == 600)
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
'''