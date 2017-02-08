import datetime
import time
import sys

infodate = datetime.date(2017, 2, 27)
tidate = datetime.date(2017, 3, 29)
mathdate = datetime.date(2017, 3, 1)
sysdate = datetime.date(2017, 3, 10)
today = datetime.date.fromtimestamp(time.time())


def date_to_str(date):
    return "%d.%d.%d" % (date.day, date.month, date.year)


def remaining_time(exdate):
    """Returns the remaining time until the exam in days, the date of the exam
    and todays date.

    Args:
        exdate (int): 0 for info, 1 for TI, 2 for math, 3 for systems

    Returns:
        todaystr (str): String representation of todays date
        [exam]datestr (str): String representation of the exam date
        remdays (int): Days left until the exam
    """
    todaystr = date_to_str(today)
    infodatestr = date_to_str(infodate)
    tidatestr = date_to_str(tidate)
    mathdatestr = date_to_str(mathdate)
    sysdatestr = date_to_str(sysdate)
    if exdate == 0:
        remdays = infodate - today
        return todaystr, infodatestr, remdays.days
    elif exdate == 1:
        remdays = tidate - today
        return todaystr, tidatestr, remdays.days
    elif exdate == 2:
        remdays = mathdate - today
        return todaystr, mathdatestr, remdays.days
    elif exdate == 3:
        remdays = sysdate - today
        return todaystr, sysdatestr, remdays.days
    else:
        print("ERROR: EXDATE")
        return None


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
            f.write("\n".join(todolst))
        with open(donefname, "w") as g:
            g.write("\n".join(donelst))


#######################################################################
#---------------------------------------------------------------------#
#--------If you're looking for the old program:-----------------------#
#--------It was moved to the branch "OldVersion"----------------------#
#---------------------------------------------------------------------#
#--------But this one is better...------------------------------------#
#---------------------------------------------------------------------#
#---------------------------------------------------------------------#
#--------...it has ALL the graphics-----------------------------------#
#---------------------------------------------------------------------#
#######################################################################
