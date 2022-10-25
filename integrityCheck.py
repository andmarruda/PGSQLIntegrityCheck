# -*- coding: utf-8 -*-
from pgInfos import sqls

class integrityCheck:
    __availableSide = ['left', 'right']

    def __init__(self, dbLeft, dbRight):
        self.__dbLeft = sqls(**dbLeft)
        self.__dbRight = sqls(**dbRight)

    def __checkMissingSide(self, side, left, right):
        if not(side.lower() in type(self).__availableSide):
            return []

        missing = []
        if side.lower() == 'right':
            for c in left:
                not(c in right) and missing.append(c)
        else:
            for c in right:
                not(c in left) and missing.append(c)

        return missing

    def missingView(self, side):
        lviews = self.__dbLeft.getAllPGClass(['v'])
        rviews = self.__dbRight.getAllPGClass(['v'])
        return self.checkMissingSide(side, lviews, rviews)

    def missingMaterializedView(self, side):
        lmviews = self.__dbLeft.getAllPGClass(['m'])
        rmviews = self.__dbRight.getAllPGClass(['m'])
        return self.checkMissingSide(side, lmviews, rmviews)

    def missingTables(self, side):
        ltable = self.__dbLeft.getAllPGClass(['r', 't', 'f', 'p'])
        rtable = self.__dbRight.getAllPGClass(['r', 't', 'f', 'p'])
        return self.checkMissingSide(side, ltable, rtable)

    def searchNotMatchRows(self):
        infos = {
            'NotInRight': [],
            'RowsNotEqual': [],
            'NotInLeft': [],
            'OK': []
        }
        lrows = self.__dbLeft.pgClassWithRowCount()
        rrows = self.__dbRight.pgClassWithRowCount()
        right = rrows

        for c in lrows:
            if not (c in rrows):
                infos['NotInRight'].append(c)
                continue
            elif lrows[c] != rrows[c]:
                infos['RowsNotEqual'].append(c)
            else:
                infos['OK'].append(c)

            del right[c]

        for c in right:
            if not (c in lrows):
                infos['NotInLeft'].append(c)

        return infos
