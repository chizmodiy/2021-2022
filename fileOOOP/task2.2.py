import datetime
from datetime import date
import datetime as dt


class Abonent():
    def __init__(self, tariff, DateOfCreation_Y_M_D, EndDate_Y_M_D, SubscriptionFee: float, CostPerMinute: float):
        self.tariff = tariff
        self.DateOfCreation_Y_M_D = DateOfCreation_Y_M_D
        self.EndDate_Y_M_D = EndDate_Y_M_D
        self.SubscriptionFee = SubscriptionFee
        self.CostPerMinute = CostPerMinute

    def ShowInfoAbAbonent(self):
        # Виведення занальної інформації для наглядності
        info = {'Tariff name': f'{self.tariff}',
                'Date of creation': f'{self.DateOfCreation_Y_M_D}',
                'End date': f'{self.EndDate_Y_M_D}',
                'Subscription fee': f'{self.SubscriptionFee} UAH',
                'The cost of a minute': f"{self.CostPerMinute} UAH"}
        for x, y in info.items():
            print(f'{x} - {y}')
# Визначення часу до кінця дії тарифу
    def TimeBeforeTheEndTariff(self):
        SRAVNIT = datetime.datetime.now()
        today = f"{date.today()}"
        last = self.EndDate_Y_M_D
        today, last = today.split('-'), last.split('-')
        a1 = datetime.date(int(today[0]), int(today[1]), int(today[2]))
        a2 = datetime.date(int(last[0]), int(last[1]), int(last[2]))
        a3 = a2 - a1
        a3 = str(a3)
        # Якщо вказана початкова дата вже пройшла то виконується
        if SRAVNIT > datetime.datetime(int(last[0]), int(last[1]), int(last[2])):
            return 'Enter the correct date'
        else:
            # Дата що вказується є вірною
            result = a3.split()[0]
            return f'There are {result} days left until the end of the tariff'
# Визначення вартості звінка за вказаною тривалістю
    def TheCostOfTheCallPerMinute(self, duration: int):
        return f'For {duration} minutes will have to pay {float(self.CostPerMinute * duration)} UAH'
# Визначення суми сплаченої абонплати між вказаними датами
    def AmountBetweenDates(self, first_date_Y_M_D, last_date_Y_M_D):
        def months_between(date1, date2):
            if date1 > date2:
                date1, date2 = date2, date1
            m1 = date1.year * 12 + date1.month
            m2 = date2.year * 12 + date2.month
            months = m2 - m1
            if date1.day > date2.day:
                months -= 1
            elif date1.day == date2.day:
                seconds1 = date1.hour * 3600 + date1.minute + date1.second
                seconds2 = date2.hour * 3600 + date2.minute + date2.second
                if seconds1 > seconds2:
                    months -= 1
            return months

        date1 = dt.datetime.strptime(f'{first_date_Y_M_D} 12:00:00', '%Y-%m-%d %H:%M:%S')
        date2 = dt.datetime.strptime(f'{last_date_Y_M_D} 12:00:00', '%Y-%m-%d %X')
        x = months_between(date1, date2)
        return f'Within these ({first_date_Y_M_D} and {last_date_Y_M_D}) dates you paid {x * self.SubscriptionFee} UAH'

# Виконання класу
if __name__ == '__main__':
    x = Abonent('Vodafon++', '2022-01-16', '2022-01-31', 85, 0.22)
    x.ShowInfoAbAbonent()
    print('1)'+x.TimeBeforeTheEndTariff()+'\n')
    print('2)'+x.TheCostOfTheCallPerMinute(20)+'\n')
    print('3)'+x.AmountBetweenDates('2021-09-12', '2021-01-12')+'\n')
