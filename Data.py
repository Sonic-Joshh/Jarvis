user_data = []

def add_log(username, role, parts):
    user_data.append({'user': username, 'role': role, 'parts': parts})

def delete_user(username):
    for log in user_data:
        if log['user'] == username:
            user_data.remove(log)

def get_logs(username):
    sp_user_data = []
    for log in user_data:
        if log['user'] == username:
            sp_user_data.append(log)
    return (sp_user_data)

# print("""******************************************\n******************************************\n******************************************\n""")
# print(user_data)
# print("""******************************************\n******************************************\n******************************************\n""")
# admin_logs = get_logs('admin')
# print(admin_logs)
# print("""******************************************\n******************************************\n******************************************\n""")
# delete_user('potty')
# print(user_data)
# print("""******************************************\n******************************************\n******************************************\n""")
