test_settings={
    "theme":"dark",
    "language":"english",
    "notifications":"enabled",
    
}
def add_setting(setting,kv):
    key=kv[0].lower()
    value=kv[1].lower()
    if key in setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(setting,kv):
    key =kv[0].lower()
    value =kv[1].lower()
    if key in setting:
        setting[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(setting,key):
    key=key.lower()
    
    if key in setting:
        del setting[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
def view_settings(setting):
    if len(setting)==0: # '''if not setting'''
        return f"No settings available." 
    else:
        result="Current User Settings:\n"
        for key,value in setting.items():
               result += f"{key.capitalize()}: {value}\n"
        return result


while True:
    
    print("   USER CONFIGURATION MANAGER")
    
    print("1. Add Setting")
    print("2. Update Setting")
    print("3. Delete Setting")
    print("4. View Settings")
    print("5. Exit")
   
    choice = input("Enter your choice: ")

    if choice == "1":
        key = input("Enter setting name: ")
        value = input("Enter setting value: ")
        print(add_setting(test_settings, (key, value)))
    elif choice == "2":
        key = input("Enter setting name to update: ")
        value = input("Enter new value: ")
        print(update_setting(test_settings, (key, value)))
    elif choice == "3":
        key = input("Enter setting name to delete: ")
        print(delete_setting(test_settings, key))
    elif choice == "4":
        print(view_settings(test_settings))
    elif choice == "5":
        break
    else:
        print("Invalid choice!")