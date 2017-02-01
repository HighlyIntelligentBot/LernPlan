import datetime
import sys


infodate = datetime.date(2017, 2, 27)
tidate = datetime.date(2017, 3, 29)
mathdate = datetime.date(2017, 3, 1)
sysdate = datetime.date(2017, 3, 10)
today = datetime.date.today()


def remaining_time(exdate, today):
    """Returns the remaining time until the exam
    Args:
        exdate (date-object): The date of the exam
        today (date-object): Today's date

    Returns:
        remdays (int): Days left until the exam
    """
    remdays = exdate - today
    return remdays


def get_data(modname):
    """Gets the progress from the files saved in the folder. You can modify
        these files ("info todo.txt", "sys done.txt") to modify the topics
        and lectures.
    Args: modname (str): Name of the module

    Returns: lst1, lst2 (lists): First lists contains the topics that are
        to be done and the second list contains the done topics.
    """
    todolst = "_".join([modname, "todo.txt"])
    with open(todolst) as f:
        lst1 = f.read().splitlines()
    donelst = "_".join([modname, "done.txt"])
    with open(donelst) as g:
        lst2 = g.read().splitlines()
    return lst1, lst2


def main():
    print("Hallo!")
    print("Bitte wählen:")
    print("Verbleibende Tage Zeigen[V]")
    print("Verbleibenden [S]toff zeigen")
    print("Verlassen[Q]")
    # main Loop
    while True:
        inp = input('>')
        if inp == 'V' or inp == 'v':
            print("Welche Klausur?")
            print("ti, info, sys, mathe")
            print('Or [q] to quit')
            inex = input('>')
            if inex == 'ti':
                print(remaining_time(tidate, today))
            elif inex == 'info':
                print(remaining_time(infodate, today))
            elif inex == 'sys':
                print(remaining_time(sysdate, today))
            elif inex == 'mathe':
                print(remaining_time(mathdate, today))
            elif inex == 'q' or inex == 'Q':
                break
            else:
                print('Unzulaegisse Eingabe')
        elif inp == 'V info' or inp == 'v info':
            print(remaining_time(infodate, today))
        elif inp == 'V sys' or inp == 'v sys':
            print(remaining_time(sysdate, today))
        elif inp == 'V mathe' or inp == 'v mathe':
            print(remaining_time(mathedate, today))
        elif inp == 'V ti' or inp == 'v ti':
            print(remaining_time(tidate, today))
        elif inp == 'S' or 's':
            print("Welches Modul?")
            print("[i]nfo, [s]ysteme, [m]athe, [t]i")
            intop = input(">")
            if intop == "i":
                todo, done = get_data("info")
                print("TODO:")
                if len(todo) == 0:
                    print("Alles geschafft!")
                else:
                    for i in range(len(todo)):
                        print(str(i) + " " + todo[i])
                print("DONE:")
                if len(done) == 0:
                    print("Noch nichts geschafft!")
                else:
                    for i in range(len(done)):
                        print(str(i) + " " + done[i])
            elif intop == "s":
                todo, done = get_data("info")
                print("TODO:")
                if len(todo) == 0:
                    print("Alles geschafft!")
                else:
                    for i in range(len(todo)):
                        print(str(i) + " " + todo[i])
                print("DONE:")
                if len(done) == 0:
                    print("Noch nichts geschafft!")
                else:
                    for i in range(len(done)):
                        print(str(i) + " " + done[i])
            elif intop == "m":
                todo, done = get_data("info")
                print("TODO:")
                if len(todo) == 0:
                    print("Alles geschafft!")
                else:
                    for i in range(len(todo)):
                        print(str(i) + " " + todo[i])
                print("DONE:")
                if len(done) == 0:
                    print("Noch nichts geschafft!")
                else:
                    for i in range(len(done)):
                        print(str(i) + " " + done[i])
            elif intop == "t":
                todo, done = get_data("info")
                print("TODO:")
                if len(todo) == 0:
                    print("Alles geschafft!")
                else:
                    for i in range(len(todo)):
                        print(str(i) + " " + todo[i])
                print("DONE:")
                if len(done) == 0:
                    print("Noch nichts geschafft!")
                else:
                    for i in range(len(done)):
                        print(str(i) + " " + done[i])
            elif intop == 'q:':
                break
        elif inp == 'q' or inp == 'Q':
            sys.exit()
        else:
            print("Unzulässige Eingabe")

if __name__ == '__main__':
    main()
