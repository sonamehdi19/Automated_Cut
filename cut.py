import os
from itertools import islice
n = 1000

# the directory where the txt file located
dir_name = "/Users/sonamehdizade/Desktop/automated_cut"

# get the first 1000 lines from the txt file
# write the remaining into the temporary file
with open(os.path.join(dir_name, "big.txt"), "r") as f, open(os.path.join(dir_name, "bigfiletmp.txt"), "w+") as out:
    nfirstlines = list(islice(f, n))
    for line in f:
        out.write(line)

# write the 1000 lines into the new file
with open(os.path.join(dir_name, "new_slice.txt"), "w+") as f2:
    for item in nfirstlines:
        f2.write(item)

# removing the original big file and rename the new file with the old name
os.remove(os.path.join(dir_name, "big.txt"))
os.rename(os.path.join(dir_name, "bigfiletmp.txt"),
          os.path.join(dir_name, "big.txt"))
