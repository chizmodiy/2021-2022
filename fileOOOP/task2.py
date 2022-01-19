import datetime

class Abonent():
    def __init__(self, tariff, DateOfCreation_D_M_Y, EndDate_D_M_Y, SubscriptionFee:float, CostPerMinute:float):
        self.tariff = tariff
        self.DateOfCreation_D_M_Y = DateOfCreation_D_M_Y
        self.EndDate_D_M_Y = EndDate_D_M_Y
        self.SubscriptionFee = SubscriptionFee
        self.CostPerMinute = CostPerMinute

    def ShowInfoAbAbonent(self):
        info = {'Назва тарифу':f'{self.tariff}',
                'Дата створення':f'{self.DateOfCreation_D_M_Y}',
                'Дата закінчення':f'{self.EndDate_D_M_Y}',
                'Абонплата':self.SubscriptionFee,
                'Вартість хвилини':self.CostPerMinute}
        for x,y in info.items():
            print(f'{x} - {y}')
    def TimeBeforeTheEndTariff(self):
        pass
    def TheCostOfTheCallPerMinute(self,time:int):
        return f'For {time} minutes will have to pay {float(self.CostPerMinute * time)}'
    def AmountBetweenDates(self):
        pass


x = Abonent('Назва тарифу','16.01.2022','31.01.2022',85,0.22)
x.ShowInfoAbAbonent()
