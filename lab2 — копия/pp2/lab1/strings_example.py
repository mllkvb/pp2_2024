print("Hello")
print('Hello')

#ASSIGN STRING TO A VAR
a = "Hello"
print(a)


#MULTLINE STRING
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#STRINGS ARE ARRAYS
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "hjhjbk":
  print(x)

#STRING LENGHT
a = "Hello, World!"
print(len(a))

#CHECK STRING
txt = "The best things in life are free!"
print("free" in txt)

#2nd example
txt='The best things in life are free!'
if 'free'in txt:
  print("Yes,'free' is present.")

#CHECK IF NOT
txt="Liverpool is the best football club"
print("basketball" not in txt)

#2nd example
txt="Liverpool is the best football club"
if "basketball" not in txt:
  print("no,'expensive is not present")
