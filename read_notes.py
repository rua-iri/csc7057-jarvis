from time import strftime as dateStrf
from time import localtime
from os import listdir as lstDir



#function which will read the contents and date
#of each note in the notes directory
def process_notes(note_dir):
    notes_list = lstDir(note_dir)

    #counter for each iteration
    note_cnt = 1

    #string to hold all the data relating to the notes
    note_str = ""

    #loop through each note in the list
    for nte in notes_list:

        note_str += "Note " + str(note_cnt) + ", "

        #convert the unix timestamp into a human readable date
        lcl_t = localtime(int(nte[5:-4]))
        nte_date = dateStrf("%A %-d %B at %-I:%-M %p", lcl_t)

        note_str += nte_date + ", "

        #read the contents of each note
        with open((note_dir + "/" + nte), "r") as nte_file:
            #print(nte_file.readline())
            note_str += nte_file.readline() + ". . "

        #increment the counter each loop
        note_cnt += 1


    #if notes directory is empty
    if len(note_str)<1:
        note_str = "No notes currently available"


    return note_str
