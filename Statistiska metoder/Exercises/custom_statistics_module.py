import numpy as np


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