def find_the_redheads(fam):
    key = [n for n, color in fam.items() if color == "red"]
    return key

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))