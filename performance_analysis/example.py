from performances import PfAnalysis
from datetime import datetime
import pandas as pd
import FinanceDataReader as fdr

"""
     2000 ~ 삼성전자 & 코스피 : 종가 데이터로 일별 수익률 변환
 """
start_date = "2000-01-01"
end_date = "2021-02-28"

if __name__ == "__main__":

    s = fdr.DataReader("005930", start_date, end_date)
    k = fdr.DataReader("KS11", start_date, end_date)

    s_ret = s["Close"].pct_change().dropna()
    k_ret = k["Close"].pct_change().dropna()

    pf = PfAnalysis()
    average= pf.average(s_ret)
    cagr= pf.cagr(s_ret)
    stdev= pf.stdev(s_ret)
    downdev= pf.downdev(s_ret)
    updev= pf.updev(s_ret)
    covar= pf.covar(s_ret, k_ret)
    correl= pf.correl(s_ret, k_ret)
    skewness= pf.skewness(s_ret)
    kurtosis= pf.kurtosis(s_ret)
    drawdown= pf.drawdown(s_ret)
    max_drawdown= pf.max_drawdown(s_ret)
    drawdown_duration= pf.drawdown_duration(s_ret)
    max_drawdown_duration= pf.max_drawdown_duration(s_ret)
    VaR= pf.VaR(s_ret)
    sharpe_ratio= pf.sharpe_ratio(s_ret, 1)
    hit_ratio = pf.hit_ratio(s_ret)

    print(
        "average:\n", average, "\n",
        "cagr:\n", cagr, "\n",
        "stdev:\n", stdev, "\n",
        "downdev:\n", downdev, "\n",
        "updev:\n", updev, "\n",
        "covar:\n", covar, "\n",
        "correl:\n", correl, "\n",
        "skewness:\n", skewness, "\n",
        "kurtosis:\n", kurtosis, "\n",
        "drawdown:\n", drawdown, "\n",
        "max_drawdown:\n", max_drawdown, "\n",
        "drawdown_duration:\n", drawdown_duration, "\n",
        "max_drawdown_duration:\n", max_drawdown_duration, "\n",
        "VaR:\n", VaR, "\n",
        "sharpe_ratio:\n", sharpe_ratio, "\n",
        "hit_ratio:\n", hit_ratio, "\n")

    pf.cum_returns(s_ret, True)
    pf.monthly_hit_ratio(s_ret)


