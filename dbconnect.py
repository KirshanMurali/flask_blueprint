import MySQLdb as db

def connection():
    conn = db.connect(host="0.0.0.0" ,
    user = "root",
    passwd = "",
    db="webBPdb")
    
    c = conn.cursor()
    return c, conn