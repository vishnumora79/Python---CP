import re
s = input("Enter expression:")

new_text = re.sub(r"[()+-/*]"," ",s)
#new_text = ord(s)
print(new_text)

# print(ord("a"))