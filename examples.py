#!/usr/bin/env python
# coding: utf-8

# In[4]:


#prints exponents in a range
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2


# In[9]:


# break - example
print("The break instruction:")
for i in range(1, 6):    
    if i == 3:        
        break    
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):    
    if i == 3:        
        continue    
    print("Inside the loop.", i)
print("Outside the loop.")


# In[3]:


#usage of while and break
largestNumber = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")


# In[2]:


#usage of time module and range
import time
for second in range(1, 6):    
    print(second, "Mississippi")    
    time.sleep(1)    
print("Ready or not, here I come!")


# In[ ]:


#while loop and continue usage
largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")


# In[1]:


#while loop loop until answered
while True:
    word = input("enter answer: ")
    print("checking...",word)
    if word == "answer":
        break
    print(word,"is incorrect")
print(word,"is correct")


# In[2]:


#Removes vowels from a word
wordWithoutVowels = ""
userWord = input("Enter your word: ")
userWord = userWord.upper()
for letter in userWord:   
    if letter == "A":        
        continue    
    elif letter == "E":       
        continue    
    elif letter == "I":       
        continue   
    elif letter == "O":        
        continue   
    elif letter == "U":        
        continue    
    else:       
        wordWithoutVowels += letter      
print(wordWithoutVowels)


# In[6]:


#demontrates while and else usage
i = 1
while i < 5:    
    print(i)    
    i += 1
else:    
    print("else:", i)

i = 1
#for and else usage
for i in range(5):
    print(i)
else:
    print("else:", i)


# In[ ]:


#counts blocks of pyramid
blocks = int(input("Enter the number of blocks: "))

height = 0
inlayer = 1
while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1

print("The height of the pyramid:", height)


# In[1]:


# Walther Collatz mathematical hypothesis
c0 = int(input("Enter c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")


# In[1]:


#for loop to print odd numbers
for i in range(0, 11):
    if i % 2 != 0:
        print(i)
#while loop to print odd numbers
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1


# In[ ]:


#for loop finds @ and prints everything before it
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")


# In[ ]:


#for loop finds and replaces 0 with x in a string
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")


# In[ ]:


#while countdown
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
    
#for countdown
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)


# In[ ]:




