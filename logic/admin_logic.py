from core.pyba_logic import PybaLogic


class AdminLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getValidateAdmin(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user, password "
            + f"FROM kardex.admin;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
