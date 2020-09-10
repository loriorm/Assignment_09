#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# ormerodl, 2020-Sept-09, add select_cd code
# ormerodl, 2020-Sept-09, add add_track code
# ormerodl, 2020-Sept-09, gave the Exceptions final words
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an integer. Now I must die.')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        try:
            cd_idx = int(cd_idx)
        except ValueError as e:
            print('Nice try, that\'s not an integer. Try again.')
            print(e.__doc__)
        for row in table:
            if row in table:
                if row.cd_id == cd_idx:
                    return row
            raise Exception('Sorry that CD/Album does not exist. I\'m going to crash now.')
            
    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """
        trkPos, trkTitle, trkLength = track_info
        try:
            trkPos = int(trkPos)
        except:
            raise Exception('Position must be an integer. You\'ve killed me once again')
        track = DC.Track(trkPos, trkTitle, trkLength)
        cd.add_track(track)



