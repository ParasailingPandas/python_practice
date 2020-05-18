practice_file = open("file_io_practice.txt", "r+")
print(practice_file.name)
# print(practice_file.read(101))
practice_file.write("poop")
print(practice_file.read(205))
practice_file.write("\n butt")
practice_file.close