import csv
import traceback
import os
import custom_module
from datetime import datetime





def read_employees():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data['fields'] = row
                else:
                    rows.append(row)

            data['rows'] = rows
            return data
    except Exception as e:
        print("An exception occurred.")
        print("Exception type:", type(e).__name__)
        print("Exception message:", str(e))
        print("Traceback:")
        traceback.print_tb(e.__traceback__)
        exit()

employees = read_employees()
print(employees)

def column_index(column_name):
    return employees['fields'].index(column_name)

employee_id_column = column_index("employee_id")

def first_name(row_number):
    index = column_index('first_name')
    return employees['rows'] [row_number] [index]

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees['rows']))

    return matches

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees['rows']))
    return matches

def sort_by_last_name():
    last_name_column = column_index('last_name')

    employees['rows'].sort(key=lambda row: row[last_name_column])

    return employees['rows']

def employee_dict(row):
    result ={}

    for i, field in enumerate(employees['fields']):
        if field == 'employee_id':
            continue
        result[field] = row[i]
    return result

def all_employees_dict():
    result = {}
    data = read_employees()
    rows = data["rows"]  

    for row in rows:
        emp_id = row[0]
        result[emp_id] = employee_dict(row)  
    return result


def get_this_value():
    return os.getenv("THISVALUE")

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
if __name__ == "__main__":
    set_that_secret("abracadabra")
    print("Secret is now:", custom_module.secret)

def load_minutes_dict(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
        return {"fields": fields, "rows": rows}

def read_minutes():
    minutes1 = load_minutes_dict("../csv/minutes1.csv")
    minutes2 = load_minutes_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes() 

minutes1, minutes2 = read_minutes()

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1 | set2
    return combined

minutes_set = create_minutes_set()

def create_minutes_list():
    minutes = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes))
    return converted

minutes_list = create_minutes_list()

def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])

    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))


    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted) 

    return converted

final_minutes = write_sorted_list()    



    






