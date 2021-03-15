
import pyautogui


def selection_sort(arrayy):
    for i in range(0,len(arrayy),4):
        for j in range(i+4,len(arrayy),4):
            if save[i] > save[j]:
                save[i] , save[j] = save[j] , save[i]
                save[i+1],save[j+1] = save[j+1] , save[i+1]
                save[i + 2], save[j + 2] = save[j + 2], save[i + 2]
                save[i + 3], save[j + 3] = save[j + 3], save[i + 3]
                #print(a[i])
                #print(a[j])
    return arrayy


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



def binarysearch(data):
    save_data =[]
    l = 0
    r = len(search) - 1
    while (l <= r):
        mid = (l + r) // 2
        if data < search[mid]:
            r = mid - 1
        elif data > search[mid]:
            l = mid + 1
        elif data == search[mid]:
            print("Data found")
            name = search[mid]
            a = save.index(name)
            name1 =save[a]
            seat = save[a+1]
            time = save[a+2]
            taka = save[a+3]


            save_data.append(name1)
            save_data.append(seat)
            save_data.append(time)
            save_data.append(taka)

            break
    return save_data
















#How many seat left
def seat(n,s):
    if s>0:
        total = s - n
        return total

# amount of seat booking
def amount(n):
    taka = 350
    total_taka = n * taka
    return total_taka

# Delete  Booking
def delete(n,s):
   DELETE = n + s
   return DELETE

# add more ticket
def add_ticket(n,s):
    add_tick = n + s
    return add_tick


# remove ticket
def rem_ticket(n,s):
    if n > s :
        r_tick = n - s
        return r_tick







# Main Function

total_amount = 0
sum = 0
S = 10
S1 = 15
S2 = 20
aa = []
aa1 = []
aa2 = []
save =[]
save1 = []
save2=[]

search = []

NAME = []
#PASS= []
print("\n")
print("_/\__/\___/\__/\__/\__/\_LOG IN FIRST_/\__/\___/\__/\__/\__/\__/\_")
print("\n")

while True :
    print("1. CREAT ACCOUNT  ")
    print("2. LOG IN ")
    print("3. EXIT")

    NN = int(input("PRESS NUMBER : "))
    # Create account
    if NN == 1:
        NAMEE = input("WRITE A USER NAME :")
        NAME.append(NAMEE)
        PASSW = pyautogui.password("CREATE A  PASSWORD")
        NAME.append(PASSW)
        print("ACCOUNT CREATE SUCCESSFUL")
        print("Now go to LOG IN part ")
        print("\n")



    if NN == 2:
        print("\n")
        print("NOW LOG IN TO YOUR ACCOUNT")
        print("\n")
        NAMEE2 = input("ENTER NAME :")
        PASSW2 = pyautogui.password("ENTER PASSWORD")
        print("\n")

        for i in range(0,len(NAME),2):

            if NAME[i] == NAMEE2 and NAME[i + 1] == PASSW2:
                print("LOG IN SUCCESSFUL")
                print("\n")

                print("_/\__/\___/\__/\__/\__/\__/\_WELCOME ONLINE TICKET BOOKING_/\__/\___/\__/\__/\__/\__/\_")
                print("\n")

                print("1. Already Booked Ticket")
                print("2. Want to Ticket Booking")
                numm = int(input("PRESS NUMBER : "))
                if numm == 2 :
                    district = input("which District you want to go : ")
                    print("\n")

                    print("10.00am for AC bus ")
                    print("10.30am for Non AC bus ")
                    #print("11.00am for AC bus ")
                    #print("11.30am for Non AC bus ")
                    print("\n")

                    time = input("Time for your travel  :")
                    print("\n")

                    print("so you want to go {} District at {}".format(district, time))
                    print("\n")

                    print("\n")
                    if time == "10.00":
                        while True:

                            print("1. Ticket Booking")
                            print("2. Edit Ticket ")
                            print("3. Your Ticket ")
                            print("4. Exit ")
                            print("\n")
                            number = int(input("press Number : "))
                            print("\n")

                            if number == 1:
                                name = input(" Plz enter your nick name : ")
                                print("\n")

                                while True:
                                    print("\n")
                                    num = int(input("How many tickets u want to buy :"))
                                    print("\n")

                                    sum += num

                                    if S > 0 and num <= S :
                                        seatt = seat(num, S)

                                        print("seat have :" + str(seatt))
                                        T = (amount(num))
                                        total_amount += T
                                        print("Total taka :" + str(T))
                                        S = seat(num, S)
                                        aa.append(S)


                                        yes = input("Do u want more ticket  Yes or No?")
                                        if yes == "yes" or yes == "YES":
                                            continue
                                        else:
                                            save.append(name)
                                            search.append(name)
                                            save.append(sum)
                                            save.append(time)
                                            save.append(total_amount)
                                            sum = 0
                                            total_amount = 0
                                            print("\n")
                                            print(
                                                "_/\__/\___/\__/\__/\__/\__/\_THANK'S FOR BOOKING_/\__/\__/\__/\__/\__/\__/\_")
                                            print("\n")
                                            break

                                    elif num > S:
                                        print("sorry we have only {} seat :".format(str(S)))
                                        sum = 0
                                        total_amount = 0
                                        break

                            # Edit Ticket
                            if number == 2:
                                name1 = input(" Plz enter your nick name : ")
                                indexx = save.index(name1)
                                for i in range(indexx, indexx + 4):
                                    save1.append(save[i])

                                print("                         Name  Seat  Time  Taka ")
                                print("Your Ticket Details : " + str(save1))
                                del save1[::]
                                print("\n")
                                print("11.delete ticket")
                                print("22. Edit Ticket ")
                                d = int(input("which platform do you want :"))
                                print("\n")
                                # Delete ticket
                                if d == 11:
                                    indexx = save.index(name1)
                                    del_seat = save[indexx + 1]
                                    have_seat = aa[-1]



                                    dele = delete(del_seat, have_seat)
                                    S = dele
                                    aa.append(S)

                                    a = indexx + 4
                                    del save[indexx:a]
                                    print(save)
                                    print("DElETE SUCCESSFUL")
                                # add or remove Ticket
                                if d == 22:
                                    indexx1 = save.index(name1)
                                    your_seat = save[indexx1 + 1]
                                    your_taka = save[indexx1 + 3]
                                    have_seat2 = aa[-1]


                                    print("1.Add ticket : ")
                                    print("2.Remove ticket : ")

                                    edit_num = int(input("press Number : "))

                                    if edit_num == 1:
                                        add_tickett = int(input(" How many ticket you want to add : "))

                                        addining = seat(add_tickett, have_seat2)
                                        S = addining
                                        aa.append(S)

                                        tick = add_ticket(your_seat, add_tickett)
                                        total_amount1 = amount(add_tickett)
                                        your_total_taka = your_taka + total_amount1

                                        for i in range(indexx1, indexx1 + 4):
                                            if save[i] == your_seat:
                                                save[i] = tick
                                            elif save[i] == your_taka:
                                                save[i] = your_total_taka

                                            else:
                                                continue

                                    if edit_num == 2:

                                        indexx2 = save.index(name1)
                                        your_seat = save[indexx2 + 1]
                                        your_taka = save[indexx1 + 3]
                                        have_seat1 = aa[-1]

                                        remove_tickett = int(input(" How many ticket you want to Remove : "))

                                        dele = delete(remove_tickett, have_seat1)
                                        S = dele
                                        aa.append(S)

                                        tickk = rem_ticket(your_seat, remove_tickett)
                                        total_amount2 = amount(remove_tickett)
                                        your_total_taka1 = your_taka - total_amount2

                                        for i in range(indexx2, indexx2 + 4):
                                            if save[i] == your_seat:
                                                save[i] = tickk
                                            elif save[i] == your_taka:
                                                save[i] = your_total_taka1

                                            else:
                                                continue

                            # see ticket details

                            if number == 3:
                                name2 = input(" Plz enter your nick name : ")
                                selection_sort(save)
                                insertionSort(search)
                                print("                         Name  Seat  Time  Taka ")
                                print("Your Ticket Details : ", binarysearch(name2))
                                #print("Your Ticket Details : ", linearsearch(name2))

                            # Exit from This syestem
                            if number == 4:
                                break
                    if time == "10.30":
                        while True:

                            print("1. Ticket Booking")
                            print("2. Edit Ticket ")
                            print("3. Your Ticket ")
                            print("4. Exit ")
                            print("\n")
                            number = int(input("press Number : "))
                            print("\n")

                            if number == 1:
                                name = input(" Plz enter your nick name : ")
                                print("\n")

                                while True:
                                    print("\n")
                                    num = int(input("How many tickets you want to buy :"))
                                    print("\n")

                                    sum += num

                                    if S1 > 0 and num <= S1:
                                        seatt = seat(num, S1)

                                        print("seat have :" + str(seatt))
                                        T = (amount(num))
                                        total_amount += T
                                        print("Total taka :" + str(T))
                                        S1 = seat(num, S1)
                                        aa1.append(S1)


                                        yes = input("Do u want more ticket  Yes or No?")
                                        if yes == "yes" or yes == "YES":
                                            continue
                                        else:
                                            save.append(name)
                                            search.append(name)
                                            save.append(sum)
                                            save.append(time)
                                            save.append(total_amount)
                                            sum = 0
                                            total_amount = 0
                                            print("\n")
                                            print(
                                                "_/\__/\___/\__/\__/\__/\__/\_THANK'S FOR BOOKING_/\__/\__/\__/\__/\__/\__/\_")
                                            print("\n")
                                            break

                                    elif num > S1:
                                        print("sorry we have only {} seat :".format(str(S)))
                                        sum = 0
                                        total_amount = 0
                                        break

                            # Edit Ticket
                            if number == 2:
                                name1 = input(" Plz enter your nick name : ")
                                indexx = save.index(name1)
                                for i in range(indexx, indexx + 4):
                                    save1.append(save[i])

                                print("                         Name  Seat  Time  Taka ")
                                print("Your Ticket Details : " + str(save1))
                                del save1[::]
                                print("\n")
                                print("11.delete ticket")
                                print("22. Edit Ticket ")
                                d = int(input("which platform do you want :"))
                                print("\n")
                                # Delete ticket
                                if d == 11:
                                    indexx = save.index(name1)
                                    del_seat = save[indexx + 1]
                                    have_seat = aa1[-1]



                                    dele = delete(del_seat, have_seat)
                                    S1 = dele
                                    aa1.append(S1)

                                    a = indexx + 4
                                    del save[indexx:a]
                                    print(save)
                                    print("DElETE SUCCESSFUL")
                                # add or remove Ticket
                                if d == 22:
                                    indexx1 = save.index(name1)
                                    your_seat = save[indexx1 + 1]
                                    your_taka = save[indexx1 + 3]
                                    have_seat2 = aa1[-1]

                                    print("1.Add ticket : ")
                                    print("2.Remove ticket : ")

                                    edit_num = int(input("press Number : "))

                                    if edit_num == 1:
                                        add_tickett = int(input(" How many ticket you want to add : "))

                                        addining = seat(add_tickett, have_seat2)
                                        S1 = addining
                                        aa1.append(S1)

                                        tick = add_ticket(your_seat, add_tickett)
                                        total_amount1 = amount(add_tickett)
                                        your_total_taka = your_taka + total_amount1

                                        for i in range(indexx1, indexx1 + 4):
                                            if save[i] == your_seat:
                                                save[i] = tick
                                            elif save[i] == your_taka:
                                                save[i] = your_total_taka

                                            else:
                                                continue

                                    if edit_num == 2:

                                        indexx2 = save.index(name1)
                                        your_seat = save[indexx2 + 1]
                                        your_taka = save[indexx1 + 3]
                                        have_seat1 = aa1[-1]

                                        remove_tickett = int(input(" How many ticket you want to Remove : "))

                                        dele = delete(remove_tickett, have_seat1)
                                        S1 = dele
                                        aa1.append(S1)

                                        tickk = rem_ticket(your_seat, remove_tickett)
                                        total_amount2 = amount(remove_tickett)
                                        your_total_taka1 = your_taka - total_amount2

                                        for i in range(indexx2, indexx2 + 4):
                                            if save[i] == your_seat:
                                                save[i] = tickk
                                            elif save[i] == your_taka:
                                                save[i] = your_total_taka1

                                            else:
                                                continue

                            # see ticket details
                            if number == 3:
                                name2 = input(" Plz enter your nick name : ")
                                selection_sort(save)
                                insertionSort(search)
                                print("                         Name  Seat  Time  Taka ")
                                print("Your Ticket Details : ", binarysearch(name2))
                                #print("Your Ticket Details : ", linearsearch(name2))

                            # Exit from This syestem
                            if number == 4:

                                break
                if numm == 1:
                    name2 = input(" Plz enter your nick name : ")
                    selection_sort(save)
                    insertionSort(search)
                    print("                         Name  Seat  Time  Taka ")
                    print("Your Ticket Details : ", binarysearch(name2))
                    #print("Your Ticket Details : ", linearsearch(name2))
                    while True:

                        print("1. Edit Ticket ")
                        print("2. Your Ticket ")
                        print("3. Exit ")
                        print("\n")
                        number = int(input("press Number : "))
                        print("\n")

                        # Edit Ticket
                        if number == 1:
                            name1 = input(" Plz enter your nick name : ")
                            indexx = save.index(name1)
                            for i in range(indexx, indexx + 4):
                                save1.append(save[i])

                            print("                         Name  Seat  Time  Taka ")
                            print("Your Ticket Details : " + str(save1))
                            del save1[::]
                            print("\n")
                            print("11.delete ticket")
                            print("22. Edit Ticket ")
                            d = int(input("which platform do you want :"))
                            print("\n")
                            # Delete ticket
                            if d == 11:
                                indexx = save.index(name1)
                                del_seat = save[indexx + 1]
                                have_seat = aa1[-1]


                                dele = delete(del_seat, have_seat)
                                S1 = dele
                                aa1.append(S1)

                                a = indexx + 4
                                del save[indexx:a]
                                print(save)
                                print("DElETE SUCCESSFUL")
                            # add or remove Ticket
                            if d == 22:
                                indexx1 = save.index(name1)
                                your_seat = save[indexx1 + 1]
                                your_taka = save[indexx1 + 3]
                                have_seat2 = aa1[-1]


                                print("1.Add ticket : ")
                                print("2.Remove ticket : ")

                                edit_num = int(input("press Number : "))

                                if edit_num == 1:
                                    add_tickett = int(input(" How many ticket you want to add : "))

                                    addining = seat(add_tickett, have_seat2)
                                    S1 = addining
                                    aa1.append(S1)

                                    tick = add_ticket(your_seat, add_tickett)
                                    total_amount1 = amount(add_tickett)
                                    your_total_taka = your_taka + total_amount1

                                    for i in range(indexx1, indexx1 + 4):
                                        if save[i] == your_seat:
                                            save[i] = tick
                                        elif save[i] == your_taka:
                                            save[i] = your_total_taka

                                        else:
                                            continue

                                if edit_num == 2:

                                    indexx2 = save.index(name1)
                                    your_seat = save[indexx2 + 1]
                                    your_taka = save[indexx1 + 3]
                                    have_seat1 = aa1[-1]

                                    remove_tickett = int(input(" How many ticket you want to Remove : "))

                                    dele = delete(remove_tickett, have_seat1)
                                    S1 = dele
                                    aa1.append(S1)

                                    tickk = rem_ticket(your_seat, remove_tickett)
                                    total_amount2 = amount(remove_tickett)
                                    your_total_taka1 = your_taka - total_amount2

                                    for i in range(indexx2, indexx2 + 4):
                                        if save[i] == your_seat:
                                            save[i] = tickk
                                        elif save[i] == your_taka:
                                            save[i] = your_total_taka1

                                        else:
                                            continue

                        # see ticket details
                        if number == 2:
                            name2 = input(" Plz enter your nick name : ")
                            selection_sort(save)
                            insertionSort(search)
                            print("Your Ticket Details : ", binarysearch(name2))
                            #print("Your Ticket Details : ", linearsearch(name2))

                        # Exit from This syestem
                        if number == 3:
                            break
                break
            else:
                print("NAME OR PASSWORD DIDN'T MATCH")







    if NN == 3:
        break















