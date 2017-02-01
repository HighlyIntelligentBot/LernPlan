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


def main():
    print("Hallo!")
    print("Bitte wählen:")
    print("Verbleibende Tage Zeigen[V]")
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
        elif inp == 'q' or inp == 'Q':
            sys.exit()
        else:
            print("Unzulässige Eingabe")

if __name__ == '__main__':
    main()
