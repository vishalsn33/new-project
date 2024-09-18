print("hi")
print("h")

string1=input("enter first string:")
string2=input("Enter the second string:")
if len(string1)!=len(string2):
  print("Strings are not anagram")
elif sorted(string1)==sorted(string2):
   print("anagram")
else :
   print("not anagram")