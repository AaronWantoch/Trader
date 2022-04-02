import matplotlib.pyplot as plt
import numpy as np
from MarketData import MarketData
from MarketCalculator import MarketCalculator
from TradingAgent import TradingAgent

class PresentationManager:
    def __init__(self, calculator, marketData, agent):
        self.calculator = calculator
        self.marketData = marketData
        self.agent = agent
        
    def present(self):
        fig = plt.gcf()
        fig.set_size_inches(15, 7.5, forward=True)

        self.actionsPlot()

        self.macdPlot()

        self.wealthPlot()

        plt.show()

    def wealthPlot(self):
        plt.subplot(313)
        plt.plot(self.marketData.day, self.agent.wealthByTime)
        plt.xticks(np.arange(0, len(self.marketData.day)+1, (len(self.marketData.day)+1)/5))
        plt.title('Wealth')
        plt.ylabel("Price")

    def macdPlot(self):
        plt.subplot(312)
        macdPlot=plt.plot(self.marketData.day, self.calculator.macd)
        signalPlot=plt.plot(self.marketData.day, self.calculator.signal)
        intersectionsMarked=plt.plot(np.array(self.marketData.day)[self.calculator.intersections], np.array(self.calculator.macd)[self.calculator.intersections], 'ro')
        plt.xticks(np.arange(0, len(self.marketData.day)+1, (len(self.marketData.day)+1)/5))
        plt.title('MACD')
        plt.ylabel("Value")
        plt.legend((macdPlot[0],signalPlot[0],intersectionsMarked[0]),("MACD","Signal","Intersections"))

    def actionsPlot(self):
        plt.subplot(311)
        plt.plot(self.marketData.day, self.marketData.data)
        plt.xticks(np.arange(0, len(self.marketData.day)+1, (len(self.marketData.day)+1)/5))
        plt.title('Price of actions')
        plt.ylabel("Price")
        

data = MarketData("data/acp_d.csv")
calculator = MarketCalculator(data)
agent = TradingAgent(calculator, data)
presentation = PresentationManager(calculator, data, agent)
presentation.present()
