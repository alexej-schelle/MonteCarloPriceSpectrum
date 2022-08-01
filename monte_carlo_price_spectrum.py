############################################################################################################################################################################
#                                                                                                                                                                          #     
#                                                                                                                                                                          #         
# -*- coding: utf-8 -*-                                                                                                                                                    #            
#                                                                                                                                                                          #             
#                                                                                                                                                                          #                 
############################################################################################################################################################################
#                                                                                                                                                                          # 
#                         This routine calculate a series of a most probable price spectrum in a game theory of purchase with possible prices defined by a certain price range [a, b]       #                                                                                                                                           #        																										 
#                                                                                                                                                                          #             
#  * :
# 
#   License Copyright:  Dr. A. Schelle, Bachschmidstr. 4, 87600 Kaufbeuren 
#   License Type :      MIT license (2022)
#   License Contact:    E-Mail : alexej.schelle@gmail.com
# 
#   ** : 
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
#   (the "Software" bec_symmetry_breaking.py), to deal in the Software without restriction, including without limitation the rights to use, 
#   copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
#   furnished to do so, subject to the following conditions:
# 
#   The above copyright notice (*) and this permission notice (**) shall be included in all copies or substantial portions of the Software.
# 
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
#   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#                                                                                                                                                                                           
#
#                                                                                                                                                                                   
################################################################################################################################################################################

import os
import sys
import math
import random
import numpy
import numpy as np
import pylab
import matplotlib.pyplot as plt
import operator

sigma = 1.0 # Absolute price uncertainty

N = 100 # Number of already registered reactions from trader (total number of trades)
M = 50 # Number of proposals from buyer (positive feedback)

price_start = 25.0*sigma # Start value of price sampling
price_sample = 0.0*sigma # Variable price sampling

price = [] # Collect possible prices

price_min = 25.0*sigma # Minimal price limit 
price_max = 500.0*sigma # Maximal price limit

L = 1000.0*sigma # Total price interval in units of sigma
interaction_scale = 0.25*(price_max - price_min) # Correlation scale in units of LS (prefactor is defined by trade volume and number of trades)

offset = 10.0 # Offset price value
accuracy = 0.1 # Accuracy of the sample

N_plus = 0 # Number of trades performed per realisation
N_start = 100 # Number of trades performed initially by trader (set to initial value)

number_of_iterations = 1000 # Count the number of iterations for the Monte-Carlo Algorithm
number_of_trades = 5 # Number of trades you wish to perform

number_of_accepted_trades = []
number_of_accepted_trades.append(0)

for n in range(0, number_of_iterations):

    N_plus = 0
    print n

    for m in range(0, M) : # Average over number of trades
    
        for l in range(0, N) : # Average over number of offers

            price_sample = random.uniform(offset + 0.5*sigma, -offset + L - 0.5*sigma) # Generate random price sample in the interval [0,L]

            if (operator.gt(min(float(N_start)/float(M),1.00),random.uniform(0, 1.00)) and math.fabs(price_sample - random.uniform(price_min, price_max)) < accuracy) : # Condition for trade acceptance

                if (math.fabs(price_start - price_sample) < interaction_scale) : # Condition to choose prices proposed by the buyer

                    price.append(float(price_sample)) # Append prices to array
                    price_start = price_sample # If price for trade is accepted, set start price to accepted trade price

                    N_plus = N_plus + 1 # Count accepted trades

    number_of_accepted_trades.append(N_plus)

x = ['']*number_of_trades
price_optimal = ['']*number_of_trades
occurences = ['']*number_of_iterations

for l in range(0, number_of_iterations):

    check_pass = 0
    occurences[l] = 0

    for k in range(0, number_of_trades):

        x[k] = random.uniform(price_min, price_max)

    for m in range(0, number_of_iterations):

        check_pass = 0

        for k in range(0, number_of_trades):
        
            if (float((math.fabs(x[k]) - float(price[number_of_accepted_trades[m] + k]))) < interaction_scale): check_pass = check_pass + 1    

        if (check_pass == number_of_trades):

            occurences[l] = occurences[l] + 1
            
result = np.argmax(occurences,axis=0)

for k in range(0, number_of_trades):

    price_optimal[k] = price[number_of_accepted_trades[result] + k]    

for l in range(number_of_trades) :
    
    print 'TOP ' + str(l) + ' price value : ' + str(price_optimal[l])

print ' '

plt.figure(1)
plt.hist(price_optimal, bins = 250, normed = True)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.xlabel('price', fontsize = 18)
plt.xlim([price_min, price_max])
plt.ylim([0, 0.1])
plt.savefig('/Users/dr.a.schelle/Desktop/Monte_Carlo_Price_Spectrum/fig_1.png')
