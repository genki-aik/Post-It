import csv, time
import os.path

filename = "test.txt"

def write(message):
    # Writes data into a file.
    note = {"note" : message}

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ["note"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not os.path.isfile(filename):
            # Only runs if file is new. We make sure we rewrite the head
            # whenever we wipe the data.
            writer.writeheader()

        writer.writerow(note)

def read(message):
    # Reads note with the most similar content to that
    # of the text imputted by the user.
    if message == None:
        with open(filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                message = ' '.join(row)

                if message != "note":
                    print(message)
                    time.sleep(0.5)
    pass

def wipe():
    with open(filename, "w") as f:
        f.write("note\n")

def to_string(array, start_index):
    result = ""
    for i in range(start_index, len(array)):
        result += array[i]

        if (len(array) - 1 != i):
            result += " "

    return result
