import little_helper

x_range, y_range = little_helper.get_input(17, 2021).split(":")[1].split(",")

x_range = x_range.strip()[2:]
y_range = y_range.strip()[2:]

x_range = tuple(int(d) for d in x_range.split(".."))
y_range = tuple(int(d) for d in y_range.split(".."))

num_velocity_values = 0
for start_dx in range(1,288):
    for start_dy in range(-103,200):
        dx, dy = start_dx, start_dy
        x, y = 0, 0
        step = 0
        while True:
            step += 1
            x += dx
            y += dy
            dx = max(0, dx-1)
            dy -= 1
            if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
                num_velocity_values += 1
                break

            if x > x_range[1] or y < y_range[0]:
                break

print(num_velocity_values)
