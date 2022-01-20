import hashlib
import base64




file = open("password.lst")

quebra = raw_input("type the hash to crack: ")





for i in file:
        i = i.replace('\n', '')

        primeiro = hashlib.md5(i).hexdigest()
#       print (primeiro)

        segundo = base64.b64encode(primeiro)
#       print(segundo)

        terceiro = hashlib.sha1(segundo).hexdigest()
#       print(terceiro)

        if quebra == terceiro:
                print("__________________________________")
                print("[+] the hash has been broken")
                print("[i] the password is bellow:")
                print (i)


