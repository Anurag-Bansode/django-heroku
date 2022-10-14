import psycopg2
def connect():
    try:
        conn = psycopg2.connect(database='StockExchange',
                                user='Anurag',
                                password='password',
                                host='localhost',
                                port='5432'
                                )
        cur=conn.cursor()
    except(Exception, psycopg2.DatabaseError) as error:
        print("Error",error)
    return conn,cur

def insert_data(id = 1, Index = 'NYA', Date = ' 1965-12-31', open=528.00, high=531.01,low=521 , close=528):
  
    conn, cur = connect()
  
    try:
        # inserting values into the emp table
        cur.execute('INSERT INTO stock VALUES(%s, %s, %s, %f,%f,%f,%f)',
                                    (id, Index,Date,open,high,low,close))
      
    except Exception as e:
  
        print('error', e)
    # commiting the transaction.
    conn.commit()