# για να διαβάσουμε ένα αρχείο txt 

rf = open('art.txt', 'r')

# ή 

with open("file.txt", "r") as fp:
  # do what you need to do with the file

# για να κάνουμε print το αρχείο

rf.read()

# για να διαβάσουμε σειρά σειρά

rf.readlines()

# για iteration σειρά με σειρά

for line in rf.readlines():
  print line
  
# για να βγάλουμε τον χαρακτήρα αλλαγής σειράς

rf.read().splitlines()

# ή με list comprehension

temp = [line[:-1] for line in rf]
