import random
temp_pass = ""

password = input() #Says to input a password or word you like to be you password


vowels = ['a','e','i','o','u']   #what to add into the password

index_one, index_two = random.randint(0,len(password)),random.randint(0,len(password)) # random randint means to generate ramndom nubers/vowels in this case

temp1 = index_one # temp checks that everything is put into the generated password
temp2 = index_two

if index_one > index_two:
    index_one = temp2
    index_two = temp1
elif index_one == index_two:
    index_two += random.randint(1,len(password))

pass_num = [index_one,index_two]

password = f'{password[0].title()}{random.choice(vowels)}{index_one}{password[random.randint(0,2)]}{random.choice(vowels)}{index_two}{password[pass_num[0]:pass_num[1]]}{random.choice(vowels)}{index_two}{password[-1].upper()}'
for character in password:
    if character not in vowels: # if no vowels go back to temp 
        temp_pass+= character
      
print(temp_pass[:9]) # genrate numbers 0-9