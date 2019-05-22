import hashlib
hash_to_crack = "098f6bcd4621d373cade4e832627b4f6"
dict_file = "/home/pi/python_test/dict.txt"

def main():
    with open(dict_file) as fileobj:
        for line in fileobj:
            line = line.strip()
            if hashlib.md5(line).hexdigest() == hash_to_crack:
                print("successfully cracked the hash %s: It's %s") % (hash_to_crack, line)
                return ""
    print("FAiled to crack the file.")

if __name__ == "__main__":
    main()
