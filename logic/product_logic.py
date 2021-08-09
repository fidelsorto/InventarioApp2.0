from core.pyba_logic import PybaLogic


class ProductLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertProduct(self, sku, productName, quantity, price, size, color, category , photo):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `kardex`.`products` "
            + "(`id_product`,`sku`,`product_name`,`quantity`,`price`,`size`,`color`,`category`,`photo`) "
            + f"VALUES(0,'{sku}','{product_name}','{quantity}','{price}','{size}','{color}','{category}','{photo}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    
    def obtainQuantity(self, id):
        database = self.createDatabaseObj()
        sql = (
            "SELECT Quantity "
            + f"FROM kardex.products where id_product = '{id}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def updateProduct(self, id, quantity):
        database = self.createDatabaseObj()
        actual = self.obtainQuantity(id)
        sql = (
            "UPDATE `kardex`.`products` "
            + f"set quantity = {actual + quantity}"
            )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteProduct(self, id):
        database = self.createDatabaseObj()
        sql = (
            "DELETE FROM kardex.products"
            + f"where id_product = {id}"
        )