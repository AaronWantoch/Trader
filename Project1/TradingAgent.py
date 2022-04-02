import matplotlib.pyplot as plt
import numpy as np
from MarketData import MarketData
from MarketCalculator import MarketCalculator
from math import floor


class TradingAgent:
    def __init__(self, calculator, marketData, startingMoney=1000):
        self.calculator = calculator
        self.marketData = marketData
        self.money = startingMoney
        self.actions = 0
        self.wealthByTime = []
        self.trade()

    def trade(self):
        buying = True
        for i in range(0,len(self.marketData.day)):
            if i in self.calculator.intersections:
                if buying:
                    self.buy(i)
                    buying=False
                else:
                    self.sell(i)
                    buying=True
            self.wealthByTime.append(self.actions*self.marketData.data[i] + self.money)
                

    def buy(self, currentIndex):
        actionsToBuy = floor(self.money/self.marketData.data[currentIndex])
        self.actions += actionsToBuy
        self.money -= actionsToBuy*self.marketData.data[currentIndex]
    def sell(self, currentIndex):
        self.money += self.actions*self.marketData.data[currentIndex]
        self.actions = 0

data = MarketData("data/acp_d.csv")
calculator = MarketCalculator(data)
agent = TradingAgent(calculator, data)

