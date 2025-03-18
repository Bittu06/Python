"""Repeat program 4 for a list of such words to be censored. """

words = ["donkey", "kaddu", "mote", "gadhe", "kamine", "animal"]


st = "Donkey is a domesticated member of the horse family. Donkey is very helpfull animal."
with open("donkey.txt", "w") as f:
    f.write(st.lower())


with open("donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, len(word)*"#")

with open("donkey.txt", "w") as f:
    f.write(content)