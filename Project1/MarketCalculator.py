from MarketData import MarketData
import numpy as np

class MarketCalculator:
    def __init__(self, data) -> None:
        self.macd = []
        self.signal = []
        self.data = data.data
        self.calculateMACD()
        self.calculateSignal()
        self.intersections = np.argwhere(np.diff(np.sign(np.array(self.signal) - np.array(self.macd)))).flatten()

    def calculateEMA(self,ofWhat, N, current):
        x=0
        y=0
        if N>current:
            N=current
        a=2/(N+1)
        factor=1 #will be multiplied by (1 − α)
        for i in range(current, current-N-1,-1):
            x+=factor*ofWhat[i]
            y+=factor
            factor*=(1-a)
        return x/y
    def calculateMACD(self):
        for i in range(0,len(self.data)):
            self.macd.append(self.calculateEMA(self.data, 12, i) - self.calculateEMA(self.data, 26, i))
    def calculateSignal(self):
        for i in range(0,len(self.macd)):
            self.signal.append(self.calculateEMA(self.macd, 9, i))
