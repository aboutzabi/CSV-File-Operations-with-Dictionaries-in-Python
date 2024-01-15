import csv

def read_dict(file_location):
    with open(file_location, 'r+') as csv_file:
        reader = csv.DictReader(csv_file)
        print(str([row for row in reader]))
        return  [row for row in reader]
    
def write_dict(file_location, dictionry):
    with open(file_location, 'w+' ) as csv_file:
        header = [k for k in dictionry[0]]
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for key in dictionry:
            writer.writerow(key)

def test_data():
    input_rows = []
    keep_going = True
    while keep_going:
        name = input('name: ')
        last_name = input('last_name: ' )
        age = input('age ')
        input_rows.append({'name': name,'last_name': last_name, 'age': age})
        ui_keep_going = input('continue? (y/n):')
        if ui_keep_going != 'y':
            keep_going =False
        
        print(input_rows)
        write_dict('dict.csv', input_rows)
        written_value = read_dict('dict.csv')
        print(str(written_value))

test_data()
        
    