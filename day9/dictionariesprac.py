dictio = {
    "Bug" : "An error in code",
    "Java" : "An ancient programming language",
    "Python" : "A newer high level programming language", 
    "C++" : "THe most powerful language",
    "JavaScript" : "The most universal language"
}

print(dictio["JavaScript"])

for key in dictio:
    print(key)
    print (dictio[key])

dictio["Rust"] = "THe new things"

for key, value in dictio.items():
    print (key, "->", value)