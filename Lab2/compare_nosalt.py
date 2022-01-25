from generate_unsalted_table import *
import time

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
# check with TA if this includes duplicates?
#print(len(dictionary_hashes))
#print(len(nosalt_hashes))
#matches = set(nosalt_hashes).intersection(dictionary_hashes)
matches = [x for x in nosalt_hashes if x in dictionary_hashes]
outputs = []
#print(len(matches))
for x in matches:
    outputs.append(nosalt_users[nosalt_hashes.index(x)] + ":" + dictionary_words[dictionary_hashes.index(x)] + "\n")

#print(outputs)

with open('cracked_passwords.txt', 'w') as f:
    f.writelines(outputs)
    
f.close

time2 = time.time()

print('compare_nosalt cracked %d passwords in %fms' % (len(outputs), ((time2-time1)*1000)))