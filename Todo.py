# todo list


def todo_list(list1):
    user = False

    while not user:
        add_items = input("Enter the things to todo :")
        list1.append(add_items)
        add_more = input("Do you to add more items (Y/N) : ").upper()
        if add_more == "Y":
            while add_more == "Y":
                add_items = input("Enter the things to todo :")
                list1.append(add_items)
                add_more = input("Do you to add more items (Y/N) : ").upper()
                if add_more == "N":
                    user = True
                    break
        elif add_more == "N":
            user = True
            break
        else:
            print("Enter a valid input")
            add_more = input("Do you to add more items (Y/N) : ").upper()
            if add_more == "N":
                user = True
                break

    print("List is created ")


def display(list1):
    if len(list1) == 0:
        print("List is empty")
        add_task = input("Do you want to add items to your list (Y/N) : ").upper()
        if add_task == "Y":
            todo_list(list1)
        else:
            if add_task == "N":
                exit()

    else:
        for items in list1:
            print("-->", items)


def remove_task(list1):
    if len(list1) != 0:
        remove_more_task = False
        while not remove_more_task:
            while len(list1) != 0:
                enume_list = enumerate(list1)
                print(list(enume_list))
                index_of_obj = int(input("Select index of the task which is to be removed"))
                list1.pop(index_of_obj)
                print("new list is :", list1)
                ask_user = input("do you want to remove more task (Y/N) : ").upper()
                if ask_user == "N":
                    remove_more_task = True
            remove_more_task = True
        print("List is empty")



    else:
        if len(list1) == 0:
            print("List is empty")
            add_task = input("Do you want to add items to your list (Y/N) : ").upper()
            if add_task == "Y":
                todo_list(list1)
            else:
                print("Enter a valid input")


def sort_task(list1):
    print("list sorted in  order is :")
    for cards in sorted(list1):
        print("-->", cards)


def main():
    list1 = []
    print("******TODO LIST******")
    opr_done = False
    while not opr_done:
        print("Select the operation you want to perform\n"
              "1)CREATE A TODO LIST\n"
              "2)DISPLAY THE LIST \n"
              "3)SORT THE LIST\n"
              "4)REMOVE A TASK FROM THE LIST\n ")
        operation = int(input("Enter the option number of operation to be performed :"))
        if operation == 1:
            todo_list(list1)
        elif operation == 2:
            display(list1)
        elif operation == 3:
            sort_task(list1)
        else:
            remove_task(list1)
        opr_again = input("Do you want to continue('Y/N') :").upper()
        if opr_again == "Y":
            while opr_again == "Y":
                print("Select the operation you want to perform\n"
                      "1)CREATE A TODO LIST\n"
                      "2)DISPLAY THE LIST \n"
                      "3)SORT THE LIST\n"
                      "4)REMOVE A TASK FROM THE LIST\n ")
                operation = int(input("Enter the option number of operation to be performed :"))
                if operation == 1:
                    todo_list(list1)
                elif operation == 2:
                    display(list1)
                elif operation == 3:
                    sort_task(list1)
                else:
                    remove_task(list1)
                opr_again = input("Do you want to continue('Y/N') :").upper()
                if opr_again == "N":
                    opr_done = True
                    break

        elif opr_again == "N":
            opr_done = True
            exit()
        else:
            print("Enter a valid input")


if __name__ == '__main__':
    main()
