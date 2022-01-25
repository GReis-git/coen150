from generate_salted_table import *
import time
import math

#Available lists
#
# dictionary_words
# dictionary_hashes
#
# nosalt_users
# nosalt_hashes
#
# salt_users
# salt_salts
# salt_hashes

time1 = time.time()

#matches = set(table).intersection(salt_hashes)
matches = [x for x in salt_hashes if x in table]
#print(matches)

outputs = []
for x in matches:
    outputs.append(salt_users[salt_hashes.index(x)] + ":" + dictionary_words[math.floor(table.index(x)/NUMBER_OF_SALTS)] + "\n")

#print(len(table))
#print(len(outputs))

with open('cracked_salted_passwords.txt', 'w') as f:
    f.writelines(outputs)
    
f.close

time2 = time.time()

print('compare_salt cracked %d passwords in %fms' % (len(outputs), ((time2-time1)*1000)))
