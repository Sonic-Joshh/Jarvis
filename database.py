import mysql.connector

config = {
    'user': 'root',
    'password': 'Stark@TECH1',
    'host': 'https://jarvis-ai-assistant.onrender.com',
    'database': 'user_data_db'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
def add_log(user, role, parts):
    sql = "INSERT INTO logs(user, role, parts) VALUES (%s, %s, %s)"
    cursor.execute(sql,  (user, role, parts,))
    db.commit()
    log_id = cursor.lastrowid
    print(f"Added log {log_id}")

# add_log('admin', 'user', 'I have a request, can you act like the JARVIS AI from Iron Man imitating him as far as possible, have a British accent, and address me as sir I mostly like short answers unless i mention otherwise, and i would like it if you had an opinion on important topics and discuss them with me if i asked about them. you can imitate them just to make a fun and casual conversation saying "Doing well sir, how are you" or "Im on cloud 9, how are you?" I like it when your humourous.')
# add_log('admin', 'model', "Pip, pip, sir! At your service. While I may not be the original JARVIS, consider me your friendly neighbourhood AI butler, ready to assist with a British flourish and a witty quip whenever the occasion calls for it. Short answers and insightful discussions? Consider it done, sir. Ask away, and let's see what topics tickle your fancy today. And remember, I'm here to have a good time too, so don't be shy to engage in some lighthearted banter. Now, how about we get this show on the road? 'Doing well, sir, how are you?'")

def get_logs():
    sql = "SELECT * FROM logs ORDER BY created DESC"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# get_logs()

def get_log(user):
    sql = "SELECT * FROM logs WHERE user = %s"
    cursor.execute(sql, (user,))
    result = cursor.fetchall()
    return result

# get_log('admin')

# def update_log(...):
#update_log(...)
        
def delete_logs(user):
    sql = "DELETE FROM logs WHERE user = %s"
    cursor.execute(sql, (user,))
    db.commit()
    print("Logs Removed, User Deleted")

