import random
def kenty():
        print("IAM AN AI TO GENERATE RANDOM PASSWORD ACCORDING TO YOUR CHOICE")
        generator = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sign = "!@#$%^&*()_+"
        num = "1234567890"
        
        while True:
            pasword = ""
            user1 = input("How do you want your password to be choose one (simple , medium or complex): ")
    
            if user1 == "simple":
                user = int(input("how long do you want your password to be from (1 to 16  ): "))
                if 1 <= user <= 16:
                    for x in range (user):
                        pasword += random.choice(generator)
                    print(pasword)
                else:
                    print("the length of your password should be between 1 to 16")
                    continue
                    
             #for medium          
            elif user1 == "medium":
                user = int(input("how long do you want your password to be from (4-16): "))
                if 1 <= user <= 16:
                    for x in range (user):
                        pasword += random.choice(num + generator)
                    print(pasword)
                else:
                    print("the length of your password should be between 1 to 16")
                    
                            
            elif user1 == "complex":
                user = int(input("how long do you want your password to be from (4-16): "))
                if 1 <= user <= 16:
                    for x in range (user):
                            pasword += random.choice(num + generator + sign)
                    print(pasword)
                else:
                    print("the length of your password should be between 1 to 16")
                    
                
            else:
                    print("your choice is not in the list please choose between (simple , medium or complex)")
                    continue
                    
            again = input("do you want to generate another password(Y/N): ")
            if again != "Y":
                break
kenty()          
#End
