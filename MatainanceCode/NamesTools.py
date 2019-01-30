import pickle
import os

data_path = "C:\\Users\\thepe_000\\Desktop\\PP5\\VoidScribe\\void_scribe\\data\\Names\\"

def createIndex(path):
        #helper function, yields all files in a directory
        def files(path):  
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    yield file

        index = {}
        for file in files(path):
            key = file.split('.')[0]
            index[key] = path + file
        return index

def loadNameType(Name_Type, index):
        return pickle.load(open(index[Name_Type], "rb" ))

def writeNameType(data_path, new_Name_Type, new_Data, old_Name_Type=None):
    # Writes a new pickled dictionairy object to data_path using new_Name_Type as the filename 
    # and new_Data as the data
    # if old_Name_Type is specified, the file will be removed

    # Setup for deletion
    to_del = ""
    if old_Name_Type != None:
        to_del = data_path + old_Name_Type
    else:
        to_del = data_path + new_Name_Type

    # Check to ensure file is valid
    if os.path.isfile(to_del):
        # delete file
        os.remove(to_del)

    # Pickle new file
    pickle.dump(new_Data, open(data_path + new_Name_Type + '.p', "wb"))

def saveNameType(index, Name_Type, data):

    to_del = data_path + Name_Type + '.p'
    # Check to ensure file is valid
    if os.path.isfile(to_del):
        # delete file
        os.remove(to_del)
    pickle.dump(data, open(data_path + Name_Type + '.p', "wb"))

def Console(options):
    # Options is dictionary where:
    #   key is name of the option
    #   value is a function to call

    def printOptions():
        print("Select an option by entering a valid number.")
        i = 0
        for i, option in enumerate(options.keys()):
            print(f'{i}. {option}')
        print(f'{i + 1}. exit')

    def getInput():
        arg = input()
        if arg == 'exit':
            return arg
        if arg not in options.keys():
            return None
        return arg

    def loop():

        while True:
            printOptions()
            option = getInput()
            while option == None:
                print("Invalid input, please re-enter")
                option = getInput()
            if option == 'exit':    
                break
            else:
                options[option]()

    loop()

def search():

    def searchForName_Type():
        index = createIndex(data_path)
        print('Please enter a valid Name_Type, or exit')
        while True:
            arg = input()
            if arg == 'exit':
                return
            if arg not in index.keys():
                print(f'{arg} Name_Type not found, please check spelling')
                continue
            break 

        Name_Type = loadNameType(arg, index)

        def Tags():
            def view():
                print(f"Name_Type: {arg} has the following tags.")
                for tag in Name_Type['Tags']:
                    print(tag)
            def add():
                print(f"Please enter a new tag for the {arg} Name_Type.")
                new = input()
                print(f"Adding Tag: {new}, confirm (y/n)")
                confirm = input()
                if confirm == 'y':
                    Name_Type['Tags'].append(new)
                    saveNameType(index, arg, Name_Type)
                    print("New Tag Added")
            def remove():
                view()
                print(f"Please enter a tag to remove from the {arg} Name_Type.")
                rmv = input()
                if rmv == 'exit':
                    return
                while rmv not in Name_Type['Tags']:
                    print('Entered Tag not found, please check spelling or enter "exit"')
                    rmv = input()
                    if rmv == 'exit':
                        return
                print(f"Removing Tag: {rmv}, confirm (y/n)")
                confirm = input()
                if confirm == 'y':
                    Name_Type['Tags'].remove(rmv)
                    saveNameType(index, arg, Name_Type)
                    print("Tag Deleted")
            

            options = {'view':view, 'add':add, 'remove':remove}
            Console(options)

        def Category():
            def rename():
                    print("Please enter a new name")
                    new = input()
                    cat = Name_Type["Category"]
                    print(f"Replacing category name: {cat} with new category: {new}. Confirm? (y/n)")
                    confirm = input()
                    if confirm == 'y':
                        Name_Type['Category'] = new
                        saveNameType(index, arg, Name_Type)
                        print("Category renamed")
    
            options = {'rename':rename}
            print(f"Name_Type {arg} is categorized as {Name_Type['Category']}.")
            Console(options)

        options = {'Tags':Tags, 'Category':Category}
        Console(options)


    def searchByTag():
        print('Gathering Tags...')

        tag_data = {}
        index = createIndex(data_path)
        for key in index.keys():
            for tag in loadNameType(key, index)['Tags']:
                if tag not in tag_data.keys():
                    tag_data[tag] = []
                tag_data[tag].append(key)

        print('Finished indexing tags, please enter a tag to search')
        print(tag_data.keys())
        arg = input()
        while arg not in tag_data.keys():
            print('Tag not found please enter a valid tag or exit')
            arg = input()
            if arg == 'exit':
                break
        print(f"Tag {arg} has the following associated Name_Types:")
        for name_type in tag_data[arg]:
            print(name_type)
    
    def searchByCategory():
        print('Gathering Cateories...')

        cat_data = {}
        index = createIndex(data_path)
        for key in index.keys():
            cat = loadNameType(key, index)['Category']
            if cat not in cat_data.keys():
                cat_data[cat] = []
            cat_data[cat].append(key)

        print('Finished indexing Categories, please enter a Category to search')
        print(cat_data.keys())
        arg = input()
        while arg not in cat_data.keys():
            print('Category not found please enter a valid tag or exit')
            arg = input()
            if arg == 'exit':
                break
        print(f"Category {arg} has the following associated Name_Types:")
        for name_type in cat_data[arg]:
            print(name_type)

    options = {'nameType':searchForName_Type, 'tag':searchByTag, 'category':searchByCategory}
    Console(options)

def Analysis():

    def sumTags():
        rates_of_apearance = {}
        index = createIndex(data_path)
        for key in index.keys():
            for tag in loadNameType(key, index)['Tags']:
                if tag not in rates_of_apearance.keys():
                    rates_of_apearance[tag] = 1
                else:
                    rates_of_apearance[tag] += 1
        
        for key in rates_of_apearance.keys():
            print(f"Tag {key} apears {rates_of_apearance[key]} times.")

    def sumCategories():
        rates_of_apearance = {}
        index = createIndex(data_path)
        for key in index.keys():
            cat = loadNameType(key, index)['Category']
            if cat not in rates_of_apearance.keys():
                rates_of_apearance[cat] = 1
            else:
                rates_of_apearance[cat] += 1
        
        for key in rates_of_apearance.keys():
            print(f"Category {key} apears {rates_of_apearance[key]} times.")

    options = {'tags':sumTags, 'category':sumCategories}
    Console(options)

options = {'search':search, 'analysis':Analysis}

if __name__ == '__main__':
    Console(options)



    

    
        

    

