from appJar import gui
from void_scribe.NamesDictionary import NamesDictionary
# from void_scribe.NamesDictionary import NamesDictionary
import pkg_resources

def update_Search():
    entry = app.getEntry('Search_Name_Type')
    matches, misses = [], []
    for name_type in nd.keys():
        if entry in name_type:
            matches.append(name_type)
        else:
            misses.append(name_type)
    display = matches
    display.append('----------------------------------------')
    for nt in misses:
        display.append(nt)

    app.updateListBox('Name_Types', display)
    
    if len(display) == 0:
        app.setEntryInvalid('Search_Name_Type')
    elif entry in display:
        app.setEntryValid('Search_Name_Type')
    else:
        app.setEntryWaitingValidation('Search_Name_Type')

def moveToEntry():
    entry = app.getListBox('Name_Types')
    if len(entry) != 0:
        app.setEntry('Search_Name_Type', entry[0])
        selectNameType()

def selectNameType():
    # verify the field is good

    inp = app.getEntry('Search_Name_Type')
    if inp not in nd.keys():
        app.setLabel('Selected_Name_Type', "Please Enter A Valid Name_Type. {} is invalid.".format(inp))
        app.setOptionBox('Category', 0)
        app.updateListBox('Tags', [])
    else:
        app.setLabel('Selected_Name_Type', "Selected Name_Type: {}.".format(inp))
        global selected, selected_nt
        selected = nd[inp]
        selected_nt = inp
        app.setOptionBox('Category', categories.index(selected['Category']))
        app.updateListBox('Tags', selected['Tags'])

def selectTag():
    tag = app.getListBox('Tags')[0]
    app.setEntry('Edit_Tag_Entry', tag)

def editTag():
    to_edit = app.getListBox('Tags')[0]
    to_save = app.getEntry('Edit_Tag_Entry')
    selected['Tags'][selected['Tags'].index(to_edit)] = to_save
    app.updateListBox('Tags', selected['Tags'])

def addTag():
    to_save = app.getEntry('Edit_Tag_Entry')
    selected['Tags'].append(to_save)
    app.updateListBox('Tags', selected['Tags'])

def saveName_Type():
    nd.update(selected, selected_nt, overwrite=True)

def updateCategory():
    cat = app.getOptionBox('Category')
    selected['Category'] = cat

def refreshTagData():
    global tag_data
    index = nd.__createIndex__(pkg_resources.resource_filename('void_scribe', 'data/Names/'))
    for key in index.keys():
        for tag in nd[key]['Tags']:
            if tag not in tag_data.keys():
                tag_data[tag] = []
            tag_data[tag].append(key)

def addTagFromList():
    tags = app.getListBox('Existing_Tags')
    if len(tags) == 0:
        return
    tag = tags[0]
    selected['Tags'].append(tag)
    app.updateListBox('Tags', selected['Tags'])
    refreshTagData()

def removeTagFromList():
    tag = app.getListBox('Tags')[0]
    selected['Tags'].remove(tag)
    app.updateListBox('Tags', selected['Tags'])
    refreshTagData()

app = gui(title='NamesTools')
nd = NamesDictionary()
categories = ['None', 'Creatures', 'Places', 'Things', 'Ideas']
selected = None
selected_nt = ""
tag_data = {}
refreshTagData()

# Create search label and entry box
app.addLabel('Select_Text', 'Select Name_Type')
app.addValidationEntry('Search_Name_Type')
app.setEntryDefault('Search_Name_Type', 'Search...')
app.addListBox('Name_Types', nd.keys())
app.setEntryChangeFunction('Search_Name_Type', update_Search)
app.setListBoxChangeFunction('Name_Types', moveToEntry)
app.setEntrySubmitFunction('Search_Name_Type', selectNameType)

# Create a box of all currently existing tags
app.addListBox('Existing_Tags', values=tag_data.keys(), column=1, row=2)
app.setListBoxChangeFunction('Existing_Tags', addTagFromList)

# Create selected box, category field
app.addLabel('Selected_Name_Type', 'Select a Name Type')
app.addOptionBox('Category', categories)
app.setOptionBoxSubmitFunction('Category', updateCategory)
app.addListBox('Tags', column=2, row=2)
app.addEntry('Edit_Tag_Entry', column=2)
app.setEntryDefault('Edit_Tag_Entry', 'Select A Tag To Edit')
app.setEntrySubmitFunction('Edit_Tag_Entry', addTag)

# Create edit and add buttons for tags
app.addButton('Add_Tag', addTag, column=2)
app.addButton('Edit_Tag', editTag, column=2)
app.addButton('Remove Tag', removeTagFromList, column=2)

# Create Data box for viewing

# Create Save Button
app.addButton('Save', saveName_Type)

# Launch app
app.go()