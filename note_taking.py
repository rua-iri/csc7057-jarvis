import time

#function for writing notes and storing them in a folder where they can be viewed online
def write_note(note_data):
    #title set by default to the current timestamp
    note_title = "note-" + str(int(time.time()))

    #check that note_data is not empty before writing to file
    if len(note_data)>0:
        #write the note's contents to a file
        with open("./notes/"+note_title+".txt", "w") as new_note:
            new_note.write(note_data)
