class Ticket():
    def __init__(self, weekend=False, chile=False):
        self.ticket_price = 100

        if weekend:
            self.price = 1.2
        else:
            self.price = 1

        if chile:
            self.discount = 0.5
        else:
            self.discount = 1
    
    def count_price(self, num):
        return self.ticket_price * self.price * self.discount * num


if __name__ == '__main__':
    Rimm = Ticket(weekend=True)
    print(Rimm.count_price(5))