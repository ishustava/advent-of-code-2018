def cell_power(x, y, serial_number):
    rack_id = x + 10
    power_level = (rack_id * y + serial_number) * rack_id
    hundreds = int(power_level / 100) - int(power_level / 1000) * 10
    return hundreds - 5


max_power = 0
max_power_point = (0, 0)


def power_of_square_of_size(x, y, serial_number, size=3):
    power = 0
    x_end = min(x + size, 301)
    y_end = min(y + size, 301)
    for i in range(x, x_end):
        for j in range(y, y_end):
            power += cell_power(i, j, serial_number)
    return power


serial_number = 1955
# for x in range(1, 301):
#     for y in range(1, 301):
#         power = power_of_square_of_size(x, y, serial_number)
#         if power > max_power:
#             max_power = power
#             max_power_point = (x, y)
#
# print(max_power_point, max_power)

max_size = 1
max_power = 0
max_power_point = (0, 0)
for s in range(1, 301):
    for x in range(1, 301):
        for y in range(1, 301):
            power = power_of_square_of_size(x, y, serial_number, s)
            if power > max_power:
                max_power = power
                max_power_point = (x, y)
                max_size = s
    print("checked size:", s, max_power, max_power_point)
print(max_power_point, max_power, max_size)
