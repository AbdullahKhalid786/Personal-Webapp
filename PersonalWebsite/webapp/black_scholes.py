import numpy as np
from scipy.stats import norm

class BlackScholes:
    def __init__(self, S, K, T, r, sigma):
        self.S = S  # Current stock price
        self.K = K  # Strike price
        self.T = T  # Time to expiration (in years)
        self.r = r  # Risk-free interest rate
        self.sigma = sigma  # Volatility of the stock

    def d1(self):
        return (np.log(self.S / self.K) + (self.r + self.sigma ** 2 / 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)

    def black_scholes_call(self):
        call_price = (self.S * norm.cdf(self.d1()) - 
                       self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2()))
        return call_price

    def black_scholes_put(self):
        put_price = (self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2()) - 
                     self.S * norm.cdf(-self.d1()))
        return put_price

    def delta_call(self):
        return norm.cdf(self.d1())
    
    def delta_put(self):
        return -norm.cdf(-self.d1())
    
    def gamma(self):
        return norm.pdf(self.d1()) / (self.S * self.sigma * np.sqrt(self.T))
    
    def vega(self):
        return self.S * np.sqrt(self.T) * norm.pdf(self.d1())
    
    def theta_call(self):
        p1 = -self.S * norm.pdf(self.d1()) * self.sigma / (2 * np.sqrt(self.T))
        p2 = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2())
        return p1 - p2

    def theta_put(self):
        p1 = -self.S * norm.pdf(self.d1()) * self.sigma / (2 * np.sqrt(self.T))
        p2 = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2())
        return p1 + p2

    def rho_call(self):
        return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.d2())

    def rho_put(self):
        return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-self.d2())
