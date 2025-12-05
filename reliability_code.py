import random

def read_primary_sensor():
    value = random.choice([1.8, 2.3, None])
    return value

def read_backup_sensor():
    value = random.choice([1.9, 2.1])
    return value

def get_distance():
    distance = read_primary_sensor()

    if distance is None or distance < 0:
        backup = read_backup_sensor()
        return backup
    else:
        return distance

for i in range(5):
    d = get_distance()
    print("Distance reading:", d)
