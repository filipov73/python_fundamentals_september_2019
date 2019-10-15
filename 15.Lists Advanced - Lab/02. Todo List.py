note = input()
notes_list = [None] * 10
while note != "End":
    note = note.split("-")
    idx = int(note[0])
    text = note[1]
    notes_list.insert(idx, text)
    note = input()
print(list(filter(lambda x: x != None, notes_list)))
