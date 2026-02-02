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
print(f"sales vs TV:\ncorr: {df_ad["Sales"].corr(df_ad["TV"])}")
print(f"cov: {df_ad['Sales'].cov(df_ad['TV'])}")


#2c
#The pearson correlation is relatively strong and the covariance is clearly positive.

#3
print(f"\nsales vs radio:\ncorr: {df_ad["Sales"].corr(df_ad["Radio"])}")
print(f"cov: {df_ad['Sales'].cov(df_ad['Radio'])}")

plt.scatter(df_ad["Radio"], df_ad["Sales"])
plt.xlabel("Radio")
plt.ylabel("Sales")
plt.title("Sales vs Radio")
plt.show()
#it seems to me that there is a small correlation between sales and radio, this however, is 
#not nearly as strong as with tv and sales. The scatterplot shows some form of linearity

print(f"\nsales vs newspaper:\ncorr: {df_ad["Sales"].corr(df_ad["Newspaper"])}")
print(f"cov: {df_ad['Sales'].cov(df_ad['Newspaper'])}")

plt.scatter(df_ad["Newspaper"], df_ad["Sales"])
plt.xlabel("Newspaper")
plt.ylabel("Sales")
plt.title("Sales vs Newspaper")
plt.show()
#There seems to be no correlation between sales and radio (or possibly a negative one)
#The pearson correlation is very small (around .2)


#4a
print(df_ad.describe())
#counts: The total ammount of data points
#mean: The sum of all values divided by the total number of all data points
#std: Standard deviation, the typical distance a datapoint is from the mean
#min: The minimum value in the data set
#25%: 25% of the data is <= this value
#50%: 50% of the data is <= this value
#75%: 75% of the data is <= this value
#max: The maximum value in the data set

#compute mean
mean = sum(df_ad["Sales"])/len(df_ad["Sales"])
print(f"mean: {mean}")

#compute std
std = np.sqrt(sum(np.pow(df_ad["Sales"] - mean, 2)) / (len(df_ad["Sales"]) - 1))
print(f"std: {std}")


#5a
df_median_mode = pd.DataFrame(columns=df_ad.columns, index=["median", "mode"])
df_median_mode.loc["median"] = [df_ad[col].median() for col in df_median_mode.columns]
df_median_mode.loc["mode"] = [df_ad[col].mode().iloc[0] for col in df_median_mode.columns]

print(df_median_mode)
#The median and mode seem to be somewhat proportional to the mean.


#5b
print(f"df.std() uses bessels correction: {std == df_ad['Sales'].std()}")