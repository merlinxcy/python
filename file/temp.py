"""
import sqlite3

cxn=sqlite3.connect("temp.db")
cur=cxn.cursor()
cur.execute('create table a123(name varchar,id int)')
cur.close()
cxn.commit()
cxn.close()
"""

from distutils.log import warn as printf
import os
from random import randrange as rand

if isinstance(__builtins__,dict) and 'raw_input ' in __builtins__:
  scanf=raw_input
elif hasattr(__builtins__,'raw_input'):
  scanf=raw_input
else:
  scanf=input

COLSIZ=10
FIELDS=('login','userid','projid')
RDBMS={'s':'sqlite','m':'mysql','g':'gadfly'}
DBNAME='test'
DBUSER='root'
DB_EXC=None
NAMELEN=16

tformat=lambda a : str(a).title().ljust(COLSIZ)
cformat=lambda s: s.upper().ljust(COLSIZ)

def setup():
  return RDBMS[raw_input('''choose a database system:mysql gadfly sqlite enter choice''').strip().lower()[0]]

def connect(db,DBNAME):
  global DB_EXE
  dbDir='%s_%s' % (db,DBNAME)
  if db=='sqlite':
    try:
      import sqlite3
    except ImportError:
      try:
        from pysqlite2 import dbapi2 as sqlite3
      except ImportError:
        return None
    DB_EXC=sqlite3
    if not os.path.isdir(dbDir):
        os.mkdir(dbDir)
    cxn=sqlite3.connect(os.path.join(dbDir,DBNAME))
  elif db=='mysql':
    try:
      import MySQLdb
      import _mysql_exceptions as DB_EXEC
      try:
        cxn=MySQLdb.connect(db=DBNAME)
      except DB_EXC.OperationalError:
        try:
          cxn=MySQLdb.connect(user=DBUSER)
          cxn.query('Create database %s' % DBNAME)
          cxn.commit()
          cxn.close()
          cxn=MySQLdb.connect(db=DBNAME)
        except DB_EXEC.OperationalError:
          return None
    except ImportError:
      try:
        import mysql.connector
        import mysql.connector.errors as DB_EXC
        try:
          cxn=mysql.connector.Connect(**{'database':DBNAME,'user':DBUSER,})
        except DB_EXC.InterfaceError:
          return None
      except ImportError:
          return None
  elif db=='gadfly':
     pass

def create(cur):
  try:
    cur.execute("create table uesr(login varchar(10),userid integer,projid integer)")
  except DB_EXC.OperationalError,e:
    drop(cur)
    create(cur)

drop=lambda cur: cur.execute('drop table users')

NAMES=(
  ('aaron',8832),('anagela','7630'),
)

def randName():
  pick=set(NAMES)
  while pick:
      yield pick.pop()

def insert(cur,db):
  if db=='sqlite':
    cur.executemany("insert into users vaules(?,?,?)",[(who,uid,rand(1,5)) for who,uid in randName()])
  elif db=='mysql':
    cur.executemany("insert into users vaules(%s,%s,%s)",[(who,uid,rand(1,5)) for who,uid in randName()])
  elif db=='gadlfy':
    pass
getRC=lambda cur: cur.rowcount if hasattr(cur,'rowcount') else -1

def update(cur):
  fr=rand(1,5)
  to=rand(1,5)
  cur.execute("update users set projid=%d where projid=%d" % (to,fr))
  return fr,to,getRC(cur)

def delete(cur):
  rm=rand(1,5)
  cur.execute('delete from users where projid=%d' % rm)
  return rm,getRC(cur)

def dbDump(cur):
  cur.execute('select * from users')
  printf('\n%s' % ''.join(map(tformat,data)))

def main():
  db=setup()
  printf('*** connect to %r database' % db)
  cxn=connect(db,DBNAME)
  if not cxn:
    printf('ERROR:%r not supported or unreachable,exit' % db)
    return
  cur =cxn.cursor()

  printf('\n*** Creating users table')
  create(cur)

  printf('\n*** Inserting names into table')
  insert(cur,db)
  dbDump(cur)

  printf('\n*** Randomly moving folks')
  fr,to,num=update(cur)
  dbDump(cur)

  printf('\n*** Dropping users table')
  drop(cur)
  cur.close()
  cxn.commit()
  cxn.close()



if __name__=='__main__':
  main()



























