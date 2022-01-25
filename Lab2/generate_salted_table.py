from generate_unsalted_table import *

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

#change to a maximum of 1000
NUMBER_OF_SALTS = 100

table = []

#test prints
#print(len(salt_salts))
#print(salt_salts[0])
#print(dictionary_hashes[0])
#print(salt_salts[0].encode('utf-8') + dictionary_hashes[0].encode('utf-8'))

i = 0
for x in dictionary_hashes:
    for y in range(NUMBER_OF_SALTS):
        table.append(hashlib.sha256(salt_salts[y].encode('utf-8') + x.encode('utf-8')).hexdigest())
        #print(i*100+y)
    i=i+1

#test print
#print(table[0])

#for x in range(len(salt_users)):
