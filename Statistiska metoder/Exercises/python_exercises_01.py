import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


#Exercise 1a

df_ad = pd.read_csv("Exercises\data\Advertising.csv", index_col=0)
print(f"head:\n{df_ad.head()}\n")
print(f"describe:\n{df_ad.describe()}\n")

df_ad['Sales'].hist(bins=15)
plt.title("Sales distribution")
plt.show()

df_ad['Sales'].hist(bins=15, cumulative=True)
plt.title("Sales ogive")
plt.show() #no known stochastic process, sales isnt like coin flips. We continue as if normal


#1b
#use (MLE) maximum-log-likelihood-estimation to find most likely distribution given the data
possible_distributions = {
    "normal": stats.norm,
    "lognormal": stats.lognorm,
    "gamma": stats.gamma,
    "Weibull": stats.weibull_min,
    "normal, skew": stats.skewnorm
}

MLE_distributions = {
    name: dist.fit(df_ad["Sales"]) 
    for name, dist in possible_distributions.items()
}

log_likelihoods = {
    name: np.sum(dist.logpdf(df_ad["Sales"], *MLE_distributions[name]))
    for name, dist in possible_distributions.items()
}

aic = {
    name: 2*len(MLE_distributions[name]) - 2 * log_likelihoods[name]
    for name in possible_distributions
}

for name, dist in aic.items():
    print(f"dist: {name}, aic_value: {dist}")

best_distribution = min(aic, key=aic.get)

x = np.linspace(df_ad["Sales"].min(), df_ad["Sales"].max(), 100)
plt.hist(df_ad["Sales"], bins=15, density=True, color='b')
plt.plot(x, possible_distributions[best_distribution].pdf(x, *MLE_distributions[best_distribution]), color='r')
plt.title("Attempt att fitting curve with MLE")
plt.show()


#1c
plt.boxplot(df_ad["Sales"], patch_artist=True, vert=False)
plt.title("Boxplot, sales")
plt.show()
#I much prefer histplots over boxplots since i believe they give a much more
#clear image of the distribution


#2a
plt.scatter(df_ad["TV"], df_ad["Sales"])
plt.xlabel("TV")
plt.ylabel("Sales")
plt.title("Sales vs TV")
plt.show()
#There is a clear trend upwards, it seems to start exponentially and then becoma linear


#2b
