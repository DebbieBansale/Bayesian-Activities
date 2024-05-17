# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:15:41 2024

@author: Carlos Mondejar
"""

import scipy as sp

unnormalized_posterior = likelihood_out * uniform_dist
plt.plot(mu, unnormalized_posterior)
plt.xlabel("$/mu$ in meters")
plt.ylabel("Unnormalized Posterior")
plt.show()