#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("""
[1]Sum
[2]Difference
[3]Multiply
[4]Division
[5]Power
[Q]Çıkış

""")
entry=input("You select one value")

if entry=="1":
    x=float(input("You enter first number"))
    y=float(input("You enter second number"))
    print("Sum :",x+y)
elif entry=="2":
    x=float(input("You enter first number"))
    y=float(input("You enter second number"))
    print("Difference :",x-y)
elif entry=="3":
    x=float(input("You enter first number"))
    y=float(input("You enter second number"))
    print("Multiply :",x*y)
elif entry=="4":
    x=float(input("You enter first number"))
    y=float(input("You enter second number"))
    print("Divison :",x/y)
elif entry=="5":
    x=float(input("You enter first number"))
    y=int(input("You enter second number"))
    print("Power:",x**y)

elif entry=="Q" or "q" :
    print("Exist")
    quit()


# In[ ]:




