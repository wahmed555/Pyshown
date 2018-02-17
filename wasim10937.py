
import requests
import matplotlib.pyplot as plt

class graphing:
    def __init__(self,coinName,convertTo,datapoints):
        self.coinName = coinName
        self.convertTo = convertTo
        self.datapoints = datapoints
        self.price = []
        self.time = []
    def getDataFromServer(self):
        url = "https://min-api.cryptocompare.com/data/histohour?fsym="+self.coinName.upper()+"&tsym="+self.convertTo.upper()+"&limit="+self.datapoints+"&aggregate=3&e=CCCAGG"
        req = requests.get(url)
        self.Fulldata = req.json()['Data']
        for data in self.Fulldata:
            self.time.append(float(data['time']))
            self.price.append(float(data['close']))

    def plotGraph(self):
        plt.plot(self.time, self.price)
        plt.title('CHART OF '+self.coinName.upper() + 'VS USD ')
        plt.xlabel('Time in Seconds')
        plt.ylabel('Price in '+self.convertTo.upper()+ 'VS USD ')
        plt.show()

btc = graphing('btc','usd','70')
btc.getDataFromServer()
btc.plotGraph()
eth = graphing('eth','usd','70')
eth.getDataFromServer()
eth.plotGraph()
