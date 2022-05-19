from read_data import read_csv_data


def get_data(data):
    """
    Get data from list.
    Gender: Change Male to 0 and Female to 1
    Weight: Place the column in the Kg view given in Pound (1 kg = 2,205 pound).
    Height: Place the column on the list in the cm view given in inches (2.54 cm = 1 inch).
    Args:
        data(list): data split row
    Returns:
        tuple: gender, weight and height

    """
    gender = []
    weight = []
    height = []

    # WRITE YOUR CODE HERE
    for row in data[1:]:
        # print(row)
        gender.append(row[0] == 'Female')
        # print(type(row[1]))
        weight.append(float(row[1]) / 2.205)
        height.append(float(row[2]) * 2.54)

    return gender, weight, height


data = read_csv_data('data/weight-height.csv')
res = get_data(data)
print(res)
