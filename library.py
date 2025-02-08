
def again():
    print("Do you want to continue",
          "press 1 to continue",
          "press 2 for EXIT")

    b=int(input("enter no:"))
    if(b==1):
        index()

    elif(b==2):
        print("THANKS FOR VISITING")
    
def index():
    
        print("Press 1 for BOOK: THE PSYCHOLOGY OF MONEY")
        print("Press 2 for BOOK: THE POWER OF YOUR SUBCONSCIOUS MIND")
        print("press 3 for BOOK: RICH DAD POOR DAD")
        print("press 4 for BOOK: THINK AND GROW RICH")
        a=int(input())

        if(a==1):
            print("name:Book 1: The psychology of money",
              "author: MORGAN HOUSEL",
              "description: The book deals with the complex relationship",
              "individual have with money emphasizing that financial success ",
              "is more about behaviour than knowledge."
              "price:- $5")
            again()
        elif(a==2):
            print("name:Book 2: The Power Of Your Subconscious Mind",
                  "author: JOSEPH MURPHY",
                  "description: A self help book that explore the potential",
                  "and influence the subconcious mind can have on our lives,"
                  "price:-$6")
            again()
        elif(a==3):
            print("name:Book 3: Rich Dad Poor Dad",
                  "author: Robert T. Kiyosaki",
                  "relesed_date: 1997"
                  "description: its a personal finance book that contrast the ",
                  "financial philosophies of two father figure."
                  "the book emphasizes financial education,investing and",
                  "wealth building strategies,advocating for assets like real state",
                  "business,and stock over traditional employement."
                  "price:-$10")
                
            again()
        elif(a==4):
            print("name:Book 4: Think and Grow Rich",
                  "author: NAPOLEON HILL",
                  "relesed_date: 1937",
                  "description: book explore the principle of success and wealth accumulation."
                  "Based on Hill's study of over 500 successful individualls,including",
                  "Andrew Carnegie,Henry Ford."
                  "The book outline 13 key principle such as dezire, faith , persistance",
                  "specialzed knowledge. it emphasize the power of mindset , goal setting",
                  "and taking action to personal and financial success.")
            again()
        elif(a==5):
                print("book 5")
                again()


print("____WELCOME TO SKILL CIRCLE____")
        
index()




    
    


          

        



