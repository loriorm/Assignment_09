#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# ormerodl, 2020-Sept-09, Add submenu
# ormerodl, 2020-Sept-09, update to add track
# ormerodl, 2020-Sept-09, update to display available tracks
# ormerodl, 2020-Sept-09, update to remove track
# ormerodl, 2020-Sept-09, 
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory loaded from file.')
        strYesNo = input('Would you like to continue and reload from file? [y/n]')
        if strYesNo.lower() == 'y':
            print('loading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'a':
                tplCdInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplCdInfo, lstOfCDObjects)
                IO.ScreenIO.show_tracks(lstOfCDObjects)
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks()
            elif strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                trk_idx = input('Which track would you like to remove?')
                cd.rmv_track(trk_idx)
            elif strChoice == 'x':
                break #return to main menu.
            continue # start loop back at top.
        continue  # start loop back at top.
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')