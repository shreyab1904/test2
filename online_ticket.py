class Ticketbooking():

    def Bookticket(self):

        username=input("enter mail id=")
        print("Movies available now= \n")
        f="Tenant"
        g="Gravity"
        h="All the bright places"
        j="To all the boys I loved before"
        k="Holidate"
        print(f)
        print(g)
        print(h)
        print(j)
        print(k)

        movname=input("enter the movie name for which you want ticket= ")

        if movname==(f or g or h or j or k):
            print("MOVIE : ",movname)

            number_ticket=int(input("enter number of tickets required : "))

            x=int(number_ticket * 300)

            available_ticket=80

            print("Number of ticket available are : ",available_ticket)

            if number_ticket<available_ticket:
                print("Price of ticket is : ",x)

                print("Combos available:")
                print("1.Burger Combo")
                print("2.Nachos Combo")
                print("3.Popcorn")

                u=int(input("enter number of combo :"))
                z=int(input("How many combo you want :"))
                y=int(z*500)

                print("your cost for food is : ",y)
                print("Total amount : ",x+y)

            else:
                print("Insufficient number of ticket")

        else:
            print("incorrect movie name")

    def CancelTicket(self):

        user=input("Enter email id: ")
        w=input("Are you sure you want to cancel your ticket: ")

        if w=='yes':
            otp=int(input("Enter otp : "))

            p=890
            if otp==p:
                print("OTP confirmed")
                print("Ticket cancelled successfully")
            else:
                print("Incorrect OTP")

        if w=='no':
            print("Ticket not cancelled")

obj1=Ticketbooking()
obj1.Bookticket()