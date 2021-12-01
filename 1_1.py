import little_helper

entries = little_helper.get_input(1, 2021).split()

last_entry = None
increased = 0
for x in entries:
    ix = int(x)
    if last_entry and ix > last_entry:
        increased += 1
    last_entry = ix

print(increased)
