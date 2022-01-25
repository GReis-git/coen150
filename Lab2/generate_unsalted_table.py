import hashlib

#intiial tests
#salt = "30124".encode('utf8')
#pw = "Test".encode('utf8')
#hash = hashlib.sha256(b"" + salt + hashlib.sha256(pw).digest()).hexdigest()

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


#empty lists to be filled by files
dictionary = []
nosalt = []
salt = []

# read in dictionary
with open('passes_real.txt', 'r') as f:
    dictionary = f.readlines()
f.close

with open('breached_data.txt', 'r') as f:
    nosalt = f.readlines()
f.close

with open('breached_data_salted.txt', 'r') as f:
    salt = f.readlines()
f.close

#clean dictionary
dictionary_words = []
for x in dictionary:
    dictionary_words.append(x.strip())


#clean nosalt and organize into two lists
nosalt_users = []
nosalt_hashes = []
for x in nosalt:
    nosalt_users.append(x.split('\t\t')[0])
    nosalt_hashes.append(x.split('\t\t')[1].strip())

#clean salt and organize into three lists
salt_users = []
salt_salts = []
salt_hashes = []
for x in salt:
    salt_users.append(x.split('\t\t')[0])
    salt_salts.append(x.split('\t\t')[1])
    salt_hashes.append(x.split('\t\t')[2].strip())

#hash dictionary
dictionary_hashes = []
for x in dictionary_words:
    hash = hashlib.sha256(b"" + x.encode('utf8')).hexdigest()
    dictionary_hashes.append(hash)
