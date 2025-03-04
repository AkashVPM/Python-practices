
# open file text file
file = open(r"Actuator_Body_txt_file.txt","r")

# Read each line
Lines = file.readlines()

#find ward vertex
for line in Lines:
      if "vertex" in line:
            print(line)


