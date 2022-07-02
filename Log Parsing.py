str1 = "hello world, how are you?" 
 
newStr = str1.split(" ") 
print("that’s the list we get from split {}".format(newStr)) 
for word in newStr: 
    if word == "world": 
        print("found the word 'world' :) ") 
        break