from core.pyba_logic import PybaLogic


class ProductLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertProduct(self, Sku, ProductName, Quantity, Price, Talla, Color, Category , foto):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `kardex`.`Products` "
            + "(`id_Product`,`Sku`,`ProductName`,`Quantity`,`Price`,`Talla`,`color`,`Category`,`foto`) "
            + f"VALUES(0,'{Sku}','{ProductName}','{Quantity}','{Price}','{Talla}','{Color}','{Category}','{foto}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getClientByEmail(self, clientEmail):
        database = self.createDatabaseObj()
        sql = (
            "SELECT name, email, password, salt "
            + f"FROM panpanbd.clients where email like '{clientEmail}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
