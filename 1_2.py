import little_helper

entries = little_helper.get_input(1, 2021).split()

last_entry = None
increased = 0
for x in zip(entries, entries[1:], entries[2:]):
    ix = sum(int(y) for y in x)
    if last_entry and ix > last_entry:
        increased += 1
    last_entry = ix

print(increased)
