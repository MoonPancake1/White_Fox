class price_error():

    def __init__(self, price, message="Минимальная цена больше, чем максимальная цена"):
        self.price = price
        self.message = message
        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)
        