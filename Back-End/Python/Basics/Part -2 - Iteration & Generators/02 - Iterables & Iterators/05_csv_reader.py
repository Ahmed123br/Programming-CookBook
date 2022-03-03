with open('cars.csv') as file:
    for row_index, line in enumerate(file):
        if row_index == 0:
            # header row
            headers = line.strip('\n').split(';')
            print(headers)
        elif row_index == 1:
            # data type row
            data_types = line.strip('\n').split(';')
            print(data_types)
        else:
            # data rows
            data = line.strip('\n').split(';')
            print(data)