import collections

# Class for presentation and Colors
class colors:
	reset='\033[0m'
	bold='\033[01m'
	disable='\033[02m'
	underline='\033[04m'
	reverse='\033[07m'
	strikethrough='\033[09m'
	invisible='\033[08m'
	class fg:
		black='\033[30m'
		red='\033[31m'
		green='\033[32m'
		orange='\033[33m'
		blue='\033[34m'
		purple='\033[35m'
		cyan='\033[36m'
		lightgrey='\033[37m'
		darkgrey='\033[90m'
		lightred='\033[91m'
		lightgreen='\033[92m'
		yellow='\033[93m'
		lightblue='\033[94m'
		pink='\033[95m'
		lightcyan='\033[96m'


#Creating the Nodes for LinkList
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

#LinkList class Start
class LinkList:
    #Constructor of LinkList
    def __init__(self):
        self.head = None    
    #printing the link list
    def Print_Linklist(self):
        if self.head is None:
            print(colors.bold , colors.fg.red)
            print("The List Is Empty Please Try Again!")
            print(colors.reset)
        else:
            n = self.head
            while n is not None:
                print(colors.bold , colors.fg.cyan , n.data,"-->" , colors.reset ,  end="")
                n = n.next
    
    
    
    #add elements from begning            
    def Add_Elements_begning(self,data):
        New_Node = node(data)
        New_Node.next = self.head
        self.head = New_Node
        
        return self.head
    
    
    
    #count method
    def count(self):
        if (self.head is None):
            print(colors.bold , colors.fg.red)
            print("The List Is Empty Please Try Again!")
            print(colors.reset)
        else:
            n = self.head
            Count = 1
            while n.next is not None:
                n = n.next
                Count += 1
        return Count
    #add elements at position
    def Add_Elements_position(self,data,position):
        if(position == 1):
            self.Add_Elements_begning(data)
        elif(position > 1 and position <= self.count() +1):
            n = self.head
            for i in range(1, position-1):
                n = n.next
            New_Node = node(data)
            New_Node.next = n.next
            n.next = New_Node
        self.head = self.head
        return self.head
    
    
    
    
    #delete elements from begning
    def Delete_Elements_begning(self):
        if(self.head is None):
            print(colors.bold , colors.fg.red)
            print("The List Is Empty Please Try Again!")
            print(colors.reset)
        else:
            self.head = self.head.next
            print(colors.bold , colors.fg.green)
            print(f"\nElement has been Deleted from Begning\n")
            print(colors.reset)
    
    
    
    
    #delete elements from position
    def Delete_Elements_position(self,position):
        if self.head is None:
            print(colors.bold , colors.fg.red)
            print("The List Is Empty Please Try Again!")
            print(colors.reset)
        elif(position == 1):
            self.head = self.head.next
            print(colors.bold , colors.fg.green)
            print(f"\nElement has been Deleted from Position {position}\n")
            print(colors.reset)
        elif(position > 0 and position <= self.count()):
            n = self.head
            for i in range(1,position-1):
                n = n.next
            n.next = n.next.next
            print(colors.bold , colors.fg.green)
            print(f"\nElement has been Deleted from Position {position}\n")
            print(colors.reset)
        else:
            print(colors.bold , colors.fg.red)
            print("Position Not Found Please Try Again!")
            print(colors.reset)
        
        return self.head
    
    
    
    
    #searching the elements
    def Search_Element(self,element):
        if self.head is None:
            print(colors.bold , colors.fg.red)
            print("The List Is Empty Please Try Again!")
            print(colors.reset)
        else:
            n = self.head
            while n is not None:
                if n.data == element:
                    return True
                n = n.next
            return False
    
    
    
    
    #sorting the List
    def Sort_List(self, node):
        if node is None:
            print(colors.bold , colors.fg.red)
            print("The List Is Empty Please Try Again!")
            print(colors.reset)
        else:
            values = []
            head = node
            while node:
                values.append(node.data)
                node = node.next
            for i in range(len(values) - 1):
                flag = False
                for j in range(len(values) - 1 -i):
                    if values[j] > values[j+1]:
                        temp = values[j]
                        values[j] = values[j+1]
                        values[j+1] = temp
                        flag = True
                    if (not flag):
                        break
            values = collections.deque(values)

            node = head
            while node:
                node.data = values.popleft()
                node = node.next
            print(colors.bold , colors.fg.green)
            print("The list has been Sorted")
            print(colors.reset)
            return head
    
#LinkList class end


#object of presentation class
b = colors()


#Menu of LinkList
while (True):
    print(colors.bold , colors.fg.blue)
    print("\n\t\t\t\t\t*************************************")
    print("\t\t\t\t\t\t Linked List Project ")
    print("\n\t\t\t\t\t*************************************")
    print(colors.reset)

    print("1 :------  CONSTRUCT THE LINKED LIST ------");
    print("2 :------  ADD ELEMENT IN THE BEGNING ------");
    print("3 :------  ADD ELEMENT AT POSITION ------");
    print("4 :------  DELETE ELEMENT FROM THE BEGNING ------");
    print("5 :------  DELETE ELEMENT AT POSITION ------");
    print("6 :------  SEARCH THE ELEMENT ------");
    print("7 :------  SORT THE LIST ------");
    print("8 :------  DISPLAY THE LIST ------");
    print("9 :------  Close the program ------ ");
    
    
    #CHOSE OPTION FROM MENU
    choice = int(input("\nEnter Your Choice: "))
    #PROGRAM END
    if (choice == 9):
        break
    #CONSTRUCTING THE LINKLIST
    elif(choice == 1):
        print()
        a = LinkList() 
    #ADDING ELEMENT AT BEGNING
    elif(choice == 2):
        print()
        element = int(input("Enter The Element: "))
        c = a.Add_Elements_begning(element)
        print(colors.bold , colors.fg.green)
        print(f"\nElement '{element}' has been inserted at Begning\n")
        print(colors.reset)
    #ADDING ELEMENT AT POSITION
    elif(choice == 3):
        print()
        position = int(input("Enter The Position To Insert Element: "))
        element = int(input("Enter The Element: "))
        c = a.Add_Elements_position(element,position)
        print(colors.bold , colors.fg.green)
        print(f"\nElement '{element}' has been inserted at Position {position}\n")
        print(colors.reset)
    #DELETE ELEMENT FROM BEGNING
    elif(choice == 4):
        c = a.Delete_Elements_begning()
    #DELETE ELEMENT FROM POSITION
    elif(choice == 5):
        position = int(input("Enter The Position To Delete Element: "))
        c = a.Delete_Elements_position(position)
    #SEARCHING FROM THE LIST
    elif(choice == 6):
        element = int(input("Enter The Element: "))
        if a.Search_Element(element):
            print(colors.bold , colors.fg.green)
            print("Element Is Found!")
            print(colors.reset)
        else:
            print(colors.bold , colors.fg.red)
            print("Element Is Not Found Please Try Again!")
            print(colors.reset)
    #SORTING THE LIST
    elif(choice == 7):
        a.Sort_List(c)
    #DISPLAY THE LIST
    elif(choice == 8):
        a.Print_Linklist()
print(b.bold , b.fg.purple)     
print("\nThank You")
print()
print("Created By: \nHasnain Raza Rajia \nMuhammad Zain Kanji \nM.Hammad Hussain")
print(b.reset)