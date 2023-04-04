#write a 'split_name' function that takes a string && returns a dict with first_name and last_name

def split_name(name):
    names = name.split()
    first_name = names [0]
    last_name = names [-1]
    return {
        'first_name': first_name,
        'last_name': last_name,
    }
    
assert split_name("Raffy Raf") == {
    "first_name": "Raffy",
    "last_name": "Raf",
} f"Expected {{'first_name': 'Raffy', 'last_name': 'Raf'}} but received {split_name('Raffy Raf')}"


assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

