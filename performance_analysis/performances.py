import pandas as pd
import numpy as np
from itertools import groupby, chain
import matplotlib.pyplot as plt
from pandas.tseries.offsets import MonthEnd, MonthBegin

"""
    performance analysis tool
    returns : 일별 수익률 dataframe
"""

class PfAnalysis:
    
    def __init__(self):
        self.annual = 252
    # core
    def average(self, returns): # 산술평균 수익률
        return  returns.mean()
    def cum_returns(self, returns, plot=False):
        result = (1+returns).prod()
        if plot:
            result.plot()
            plt.show()
        else:
            return result

    def cagr(self, returns): # 기하평균 수익률
        return (1+returns).prod() ** (self.annual/len(returns)) - 1
    def stdev(self, returns): # 표준편차( 변동성 )
        return returns.std() * np.sqrt(self.annual)
    def downdev(self, returns, target=0.0): # 목표 수익률 이하의 수익률에 대한 표준편차( 하방 risk )
        _returns = returns.copy()
        _returns.loc[_returns > target] = 0
        total = (_returns**2).sum()
        return np.sqrt(self.annual*total/len(_returns))
    def updev(self, returns, target=0.0): # 목표 수익률 이상의 수익률에 대한 표준편차( 하방 risk )
        _returns = returns.copy()
        _returns.loc[_returns < target] = 0
        total = (_returns**2).sum()
        return np.sqrt(self.annual*total/len(_returns))
    def covar(self, returns, benchmark): # 수익률 간 상관성
        return returns.cov(benchmark)
    def correl(self, returns, benchmark): # 수익률 간 상관계수
        return returns.corr(benchmark)

    # 전략의 테일 리스크 측정
    def skewness(self, returns): # 수익률 분포의 비대칭 정도
        return returns.skew()
    def kurtosis(self, returns): # 수익률 분포의 fat tail
        return returns.kurtosis()
    def drawdown(self, returns):
        cumulative = (1+returns).cumprod()
        highwatermark = cumulative.cummax()
        drawdown = (cumulative/highwatermark) - 1
        return drawdown
    def max_drawdown(self, returns):
        return np.min(self.drawdown(returns))
    def drawdown_duration(self, returns):
        drawdown = self.drawdown(returns)
        ddd = chain.from_iterable((np.arange(len(list(j)))+1) if i else [0]*len(list(j)) for i,j in groupby(drawdown!=0))
        ddd = pd.DataFrame(ddd)
        ddd.index = returns.index
        return ddd
    def max_drawdown_duration(self, returns):
        return np.max(self.drawdown_duration(returns))
    def VaR(self, returns, percentile=99): # sorted returns 중 하위 percentile
        return returns.quantile(1-percentile/100)

    # risk adjusted returns
    def sharpe_ratio(self, returns, benchmark):
        return self.average(returns-benchmark) / self.stdev(returns-benchmark)
    def hit_ratio(self, returns):
        return len(returns[returns>0])/len(returns) * 100
    def monthly_hit_ratio(self, returns):
        returns[returns>0] = 1
        returns[returns<0] = 0
        returns = pd.DataFrame(returns)
        group = returns.resample("M").sum()
        group['length'] = group.index.map(lambda x:  len(pd.date_range(x - MonthBegin(), x, freq='B')))
        return group["Close"]/group["length"]*100


if __name__ == "__main__":
    import FinanceDataReader as fdr
    s = fdr.DataReader("005930", "2000-01-01", "2021-02-28")
    s_ret = s["Close"].pct_change().dropna()
    pf = PfAnalysis()
    pf.monthly_hit_ratio(s_ret, True)


