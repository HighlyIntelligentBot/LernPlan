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
    todofname = "_".join([modname, "todo.txt"])
    with open(todofname) as f:
        todolst = f.read().splitlines()
    donefname = "_".join([modname, "done.txt"])
    with open(donefname) as g:
        donelst = g.read().splitlines()
    return todolst, donelst


def change_data(modname, num, undo=False):
    """Transfers a topic from TODO to DONE or the other way around.
        Also writes the new lists into the save files.
        Args:
         modname (str): Name of the module which topic should be changed.
         num (int): Number of the topic shich should be transferred
         undo (bool): Direction of the transfer. If checked the topic gets
                     copied from DONE to TODO.
        Returns:
         lst1 (list): The new TODO list and its topics
         lst2 (list):The new DONE list and its topics
    """
    if undo is False:
        todolst, donelst = get_data(modname)
        donelst.append(todolst[num])
        del todolst[num]
        todofname = "_".join([modname, "todo.txt"])
        donefname = "_".join([modname, "done.txt"])
        with open(todofname, "w") as f:
            f.write("\n".join(todolst))
        with open(donefname, "w") as g:
            g.write("\n".join(donelst))
    elif undo is True:
        todolst, donelst = get_data(modname)
        todolst.append(donelst[num])
        del donelst[num]
        todofname = "_".join([modname, "todo.txt"])
        donefname = "_".join([modname, "done.txt"])
        with open(todofname, "w") as f:
            for i in range(len(todolst)):
                f.write("\n".join(todolst))
        with open(donefname, "w") as g:
            for n in range(len(donelst)):
                g.write("\n".join(donelst))



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
            while True:
                print("Welche Klausur?")
                print("ti, info, sys, mathe")
                print('Or [q] to quit')
                inex = input('>')
                if inex == 'ti':
                    print("=============")
                    print(remaining_time(tidate, today).days)
                    lst1, lst2 = get_data('ti')
                    stamtag = len(lst1)/int(remaining_time(tidate, today).days)
                    print("TODO: %f Vorlesungen pro Tag" % (stamtag))
                    print("=============")
                elif inex == 'info':
                    print("=============")
                    print(remaining_time(infodate, today).days)
                    lst1, lst2 = get_data('info')
                    stamtag = len(lst1)/int(remaining_time(infodate, today).days)
                    print("TODO: %f Vorlesungen pro Tag" % (stamtag))
                    print("=============")
                elif inex == 'sys':
                    print("=============")
                    print(remaining_time(sysdate, today).days)
                    lst1, lst2 = get_data('sys')
                    stamtag = len(lst1)/int(remaining_time(sysdate, today).days)
                    print("TODO: %f Vorlesungen pro Tag" % (stamtag))
                    print("=============")
                elif inex == 'mathe':
                    print("=============")
                    print(remaining_time(mathdate, today).days)
                    lst1, lst2 = get_data('mathe')
                    stamtag = len(lst1)/int(remaining_time(mathdate, today).days)
                    print("TODO: %f Vorlesungen pro Tag" % (stamtag))
                    print("=============")
                elif inex == 'q' or inex == 'Q':
                    break
                else:
                    print('Unzulaegisse Eingabe')
        elif inp == 'V info' or inp == 'v info':
            print("=============")
            print(remaining_time(infodate, today).days)
            lst1, lst2 = get_data('info')
            stamtag = len(lst1)/int(remaining_time(infodate, today).days)
            print("TODO: %f Vorlesungen pro Tag" % (stamtag))
            print("=============")
        elif inp == 'V sys' or inp == 'v sys':
            print("=============")
            print(remaining_time(sysdate, today).days)
            lst1, lst2 = get_data('sys')
            stamtag = len(lst1)/int(remaining_time(sysdate, today).days)
            print("TODO: %f Vorlesungen pro Tag" % (stamtag))
            print("=============")
        elif inp == 'V mathe' or inp == 'v mathe':
            print("=============")
            print(remaining_time(mathdate, today).days)
            lst1, lst2 = get_data('mathe')
            stamtag = len(lst1)/int(remaining_time(mathdate, today).days)
            print("TODO: %f Vorlesungen pro Tag" % (stamtag))
            print("=============")
        elif inp == 'V ti' or inp == 'v ti':
            print("=============")
            print(remaining_time(tidate, today).days)
            lst1, lst2 = get_data('ti')
            stamtag = len(lst1)/int(remaining_time(tidate, today).days)
            print("TODO: %f Vorlesungen pro Tag" % (stamtag))
            print("=============")
        elif inp == 'S' or inp == 's':
            while True:
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
                    print("Vorlesungen abhaken?[j/n/u]")
                    inpchck = input("[j/n/u]>")
                    if inpchck == "j" or inpchck == "J":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("info", int(inpnum))
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
                    elif inpchck == "n" or inpchck == "N":
                        break
                    elif inpchck == "u" or inpchck == "U":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("info", int(inpnum), undo=True)
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
                    todo, done = get_data("sys")
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
                    print("Vorlesungen abhaken?[j/n/u]")
                    inpchck = input("[j/n/u]>")
                    if inpchck == "j" or inpchck == "J":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("sys", int(inpnum))
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
                    elif inpchck == "n" or inpchck == "N":
                        break
                    elif inpchck == "u" or inpchck == "U":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("sys", int(inpnum), undo=True)
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
                    todo, done = get_data("mathe")
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
                    print("Vorlesungen abhaken?[j/n/u]")
                    inpchck = input("[j/n/u]>")
                    if inpchck == "j" or inpchck == "J":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("mathe", int(inpnum))
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
                    elif inpchck == "n" or inpchck == "N":
                        break
                    elif inpchck == "u" or inpchck == "U":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("mathe", int(inpnum))
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
                    todo, done = get_data("ti")
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
                    print("Vorlesungen abhaken?[j/n/u]")
                    inpchck = input("[j/n/u]>")
                    if inpchck == "j" or inpchck == "J":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("ti", int(inpnum))
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
                    elif inpchck == "n" or inpchck == "N":
                        break
                    elif inpchck == "u" or inpchck == "U":
                        print("Welche?")
                        inpnum = input(">")
                        change_data("ti", int(inpnum))
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
                elif intop == 'q' or intop == "Q":
                    break
                else:
                    print("Unzulaessige Eingabe")
        elif inp == 'q' or inp == 'Q':
            break
            sys.exit()
        else:
            print("Unzulässige Eingabe")


if __name__ == '__main__':
    main()
