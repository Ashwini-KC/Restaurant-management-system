class Payment:
    def __init__(self,paymentId,billId):
        self.paymentId=paymentId
        self.billId=billId
    
    def isPaid():
        '''can be ignored for now 
        we ain't no fancy fuck
        '''
        pass

class Cash(Payment):
    def __init__(self, paymentId, billId):
        super().__init__(paymentId, billId)

class Card(Payment):
    def __init__(self, paymentId, billId):
        super().__init__(paymentId, billId)