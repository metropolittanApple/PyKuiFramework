from pyKui_Alt_F4_studios.imports import *
from pyKui_Alt_F4_studios.variables import *

class rule:
    def removeList():
        ### Removes item in rulesArg1 and rulesArg2

        rulesArg1.reverse()
        rulesArg1.pop(1)
        rulesArg1.reverse()

        rulesArg2.reverse()
        rulesArg2.pop(1)
        rulesArg2.reverse()

    def get():
        ### Prints the list of commands that you used

        print(rulesArg1)
        print(rulesArg2)

    def set(arg1 = "", arg2 = ""):
        ### Sets rule for program

        global minWindowSizeAllowed, autoResizeWhen00, allowMoreWindows, autoFLimit, fpsLimit

        try:
            rulesArg1.append(str(arg1))
            rulesArg2.append(str(arg2))

            if (arg1 == "min window size" or arg1 == "mws1" or arg1 == "minimum window size"):
                minWindowSizeAllowed = bool(arg2)

            elif (arg1 == "auto resize when 00" or arg1 == "arw001"):
                autoResizeWhen00 = bool(arg2)

            elif (arg1 == "allow more windows" or arg1 == "amw1" or arg1 == "more than 1 window"):
                allowMoreWindows = bool(arg2)

            elif (arg1 == "auto tick"):
                autoFLimit = bool(arg2)

            elif (arg1 == "no fps limit" or arg1 == "nfl1"):
                fpsLimit = bool(arg2)
            
            else:
                print(Fore.RED + "Unknown command for arg1")

                rule.removeList()

        except Exception as E:
            print(Fore.RED + "ERROR:", E)

        print(Fore.RESET + "")
