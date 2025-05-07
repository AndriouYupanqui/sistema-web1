class Producto:
    def __init__(self, id, nombre, precio, img) -> None:
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.img = img

    @staticmethod
    def get_all(conn):
        sql = "SELECT * FROM products;"
        cursor = conn.cursor()
        datos = cursor.execute(sql)
        products = []
        for row in datos.fetchall():
            products.append(

                Producto(row[0], row[1], row[2], row[3], )
            )
        return products