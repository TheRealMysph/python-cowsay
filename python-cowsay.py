# Cowsay but Python / Also, a note: That's only a silly project that I made to learn Python, as I'm only a begginer. So, don't expect any well-written code.

cowsay = str(input("cowsay: "))
length = len(cowsay)
hyphens = "-" * length
underscores = "_" * length
print(" ", underscores, "\n" "<", cowsay, "> \n ", hyphens, "\n        \   ^__^ \n         \  (oo)\_______\n            (__)\       )\/\ \n                ||----w | \n                ||     || \n \n \n Credits of the original cowsay goes to Tony Monroe!")
input("\n Press enter to exit...")