# string
name = "mani"
age = 22
s1 = "hello"
s2 = "world"

print((s1+ " " +s2 )*3)
print(s1*3)

text = "PYTHON"

print(len(text))
print(text[0])
print(text[-1])
print(text[2:4])
print(text[::-1])

msg =  " welCome To PYhton   "

print(msg.lower())
print(msg.upper())
print(msg.strip())
print(msg.replace("To","for"))
print(msg.split())
print(".".join(["py","is","cool"]))

# stirng checker

word = "ty3"

print(word.isalpha())
print(word.isdigit())
print(word.isalnum())
print(word.startswith("t"))


print("my name is %s and i am %d years old " % ("mani",22))
print("my name is {} and i am {} years old".format("mani",25))
print(f"my name is {name} and i am {age} years old. ")

print("name : ",name)
print("name : "+name)