class Contact:
    def __init__(self,name,phone,email):
        self.name= name
        self.phone=phone
        self.email=email
    
def add_contact():
    name=str(input("Enter Full Name :"))
    phone=str(input("Enter Phone Number :"))
    email=str(input("Enter Email :"))
    c=Contact(name,phone,email)
    with open("contacts.txt","a") as f:
        f.write(f"{c.name},{c.phone},{c.email}\n")
    print("Contact Added Sucessfully!")

def view_contact():
    try:
        with open("contacts.txt") as f:
            contacts=f.readlines()
            if len(contacts)==0:
                print("No Contact Found")
            else:
                for i,line in enumerate(contacts):
                    name,phone,email = line.strip().split(",")
                    print(f"{i+1}.Name:{name} | Phone Number:{phone} | Email:{email}")
    except FileNotFoundError:
            print("File Not Found")

def search_contact():
    search=(input("Enter the name or phone number or email you want to search: "))
    try:
        with open("contacts.txt") as f:
            contacts=f.readlines()
            if len(contacts)==0:
                print("No Contact Found")
            else:
                found =False
                for i,line in enumerate(contacts):
                    name,phone,email = line.strip().split(",")
                    if(search.lower() in name.lower() or search.lower() in phone or search.lower() in email.lower()):
                        print("Contact Found")
                        print(f"{i+1}.Name:{name} | Phone Number:{phone} | Email:{email}")
                        found = True
                if not found:
                    print("Contact Not Found")
    except FileNotFoundError:
        print("File Not Found")

def delete_contact():

    try:
        delete=input("Enter the name / phone number / email you want to delete :")
        with open("contacts.txt") as f:
            contacts=f.readlines()
            found = False
            new_contact=[]
            if len(contacts)==0:
                print("No Contact Found")
            else:
                for i,line in enumerate(contacts):
                    name,phone,email = line.strip().split(",")
                    if(delete.lower() in name.lower() or delete.lower() in phone or delete.lower() in email.lower()):
                        print("Contact Found")
                        sure=input(f"Are you sure you want to delete the contact for {name}")
                        if "yes" in sure or "yeah" in sure or "sure":
                            found=True
                        else:
                            new_contact.append(line)
                    else:
                        new_contact.append(line)

        if found:
            with open("contacts.txt","w")as f:
                f.writelines(new_contact)
                print("Contact Deleted Sucessfully")                

    except FileNotFoundError:
        print("File Not Found")
    print(f"The new contact list is :")
    view_contact()
                
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
            