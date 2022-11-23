from datetime import datetime

def write(user, data: str):
    file = 'log.txt'
    with open(file, 'a', encoding='UTF-8') as f:
        now = f"{datetime.now():%Y-%m-%d %H:%M}"
        user_str = f"{user['first_name']} {user['last_name']} ({user['id']})"

        f.writelines(f'{now} {user_str}: {data} \n')
        
