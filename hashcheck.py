import os
"""
1. ask for input1 and input2
2. compare input1 to input2
3. output both hashes on top of each other for viewer comparison and ouput VALID or INVALID
"""

"""
stage 2: identify the type of hash
common hashes: MD1,MD5,SHA1,SHA2,,SHA512
"""

def hc():
    #input sequence
    hash1 = input("Input first hash:\n")
    if hash1 == "":
        print("INVALID OR MISSING INPUT")
    else:
        pass

    hash2 = input("Input second hash:\n")
    if hash2 == "":
        print("INVALID OR MISSING INPUT")
    else:
        pass

    # get rid of whitespaces
    hash1 = hash1.strip()
    hash2 = hash2.strip()

    # clear terminal for clearer output
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #outputs accordingly if hashes match or not
    if hash1 == hash2:
        print(hash1)
        print(hash2)
        print("VALID MATCH")
    else:
        print(hash1)
        print(hash2)
        print("INVALID MATCH")

hc()
