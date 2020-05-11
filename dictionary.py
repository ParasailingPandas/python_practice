heh = {

    "butt":69,
    "cheese whiz":"personality",
    "cow":"fort"

}
print(heh)

heh["cow"] = "poop"
print(heh)

heh["unicorn"] = "bitch"
print(heh)

print(heh["butt"])

del heh["butt"]
print(heh)

heh.pop("cow")
print(heh)

print(heh.get("unicorn"))

color = {"wheels":"purple"}
heh.update(color)
print(heh)