import numpy as np
import matplotlib.pyplot as plt


def get_confidence_interval(mu: float, confidence_value: float, std_error: float) -> tuple:
    return (
        mu - confidence_value * std_error,
        mu + confidence_value * std_error
    )

def get_mean(sample_list: list):
    return sum(sample_list)/len(sample_list)

def get_standard_error(sigma: float, sample_list: list):
    return sigma / np.sqrt(len(sample_list))

def get_sample_variance(sample_list: list, sample_mean: float):
    variance = 0
    for x in sample_list:
        variance += np.square(x - sample_mean)
    return variance / (len(sample_list) - 1)


#1a
samples = [
    .645, .654, .640, .627, .626, .649, .629, .631, .643, .633, .646, .630, .634, 
    .631, .651, .659, .638, .645, .655, .624, .658, .658, .658, .647, .665
]

sigma_1 = .01
confidence_95 = 1.96
confidence_99 = 2.575
sample_mu = get_mean(samples)
standard_error = get_standard_error(sigma_1, samples)

#1b
mu_95_confidence = get_confidence_interval(sample_mu, confidence_95, standard_error)

print(f"1a: Sample mean: {sample_mu}")
print(f"1b: True mean is in the range {mu_95_confidence[0]} -> {mu_95_confidence[1]} with a confidence of 95%")


#1c
#a 90% confidence interval would be shorter than a 95% interval.

#1d
#a 99& confidence interval would be much longer then a 95% interval

mu_99_confidence = get_confidence_interval(sample_mu, confidence_99, standard_error)

print(f"1d: 99% confidence interval for the true mean is {mu_99_confidence[0]} -> {mu_99_confidence[1]}\n")


#2a

days = [
    16, 12, 14, 16, 13, 9, 15, 7, 20, 19, 11, 14, 9, 13, 11, 3, 8, 21, 16, 16, 
    12, 16,14, 20, 7, 14, 18, 13, 11, 16, 18, 16, 11, 13, 14, 16, 15, 15
]

sigma_2 = 4
days_mu = get_mean(days)
standard_error_days = get_standard_error(sigma_2, days)
confidence_interval_days = get_confidence_interval(days_mu, confidence_95, standard_error_days)

plt.hist(days, bins=15)
plt.xlabel("Days before peak radiation symptoms take hold")
plt.show()
#2a: The histplot does not clearly show a normal distribution, a normal with heavy skew is possible.

print(f"2b: Mean days until peak symptoms: {days_mu}")
print(f"2c: Confidence interval of mu = {days_mu}: {confidence_interval_days[0]} -> {confidence_interval_days[1]}\n")
#2c: finding out the true mean is 17 ould be slightly suprising but not completely unexpected.


#3a
acid = [
    52.7, 43.9, 41.7, 71.5, 47.6, 55.1, 62.2, 56.5, 33.4, 61.8, 54.3, 50.0, 
    45.3, 63.4, 53.9, 65.5, 66.6, 70.0, 52.4, 38.6, 46.1, 44.4, 60.7, 56.4
]

acid_sample_mu = get_mean(acid)
acid_variance = get_sample_variance(acid, acid_sample_mu)
acid_deviation = np.sqrt(acid_variance)
acid_standard_error = get_standard_error(acid_deviation, acid)
confidence_interval_acid = get_confidence_interval(acid_sample_mu, confidence_95, acid_standard_error)

print(f"3a:\nSample mean: {acid_sample_mu}\nSample variance: {acid_variance}\nSample deviation: {acid_deviation}")
print(f"3b: 95% confidence interval to sample mean = {acid_sample_mu}: {confidence_interval_acid[0]} -> {confidence_interval_acid[1]}")

#3c
#Yes absolutely! There isnt a single value in the sample even near the national average.