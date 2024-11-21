def array_of_names(name):
    n = [f"{name.capitalize()} {surname.capitalize()}" for name, surname in name.items()]
    return n

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
