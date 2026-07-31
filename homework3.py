def get_input():
    m = input("Enter 12 rainfall values separated by spaces: ")
    return m

def validate(m):
    values = m.split()
    if len(values) != 12:
        raise ValueError("You must enter exactly 12 numbers.")

    rainfall = []
    for value in values:
        rainfall.append(float(value))

    return rainfall

def calculate(rainfall):
    month = [
        "January", "February", "March", "April",
        "May", "June", "July", "August", 
        "September", "October", "November", "December"
    ]

    t = sum(rainfall)
    average = t / 12
    maxi = max(rainfall)
    mini = min(rainfall)
    maxi_index = rainfall.index(maxi)
    mini_index = rainfall.index(mini)

    return( t, average, 
            (maxi, month[maxi_index]),
            (mini, month[mini_index]))

def print_result(result):
    print(result)

def main():
    info = get_input()
    rainfall = validate(info)
    result = calculate(rainfall)
    print_result(result)


main()