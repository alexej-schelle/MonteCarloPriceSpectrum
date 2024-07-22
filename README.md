# MonteCarloPriceSpectrum

The routine calculates a discrete Monte Carlo spectrum of most probable prices (within a defined sample size) in a game theory of retail trade and purchase of a product in a given overcountable price range [a,b] with certain price start value s (agreed between trader and buyer) and attractive (static) price interaction force (experienced by the buyer), assuming a Poisson trade event distribution. 

The resulting discrete Monte Carlo price spectrum with maximal price sum can be applied to numerically approximate an optimal trading strategy (Nash equilibrium) for efficient trading within the range of the given sample size for a multiplayer game.  

For installation, please replace the path '/path-to-figure/' with your installation path in line 173 of this code.

-1- :
 
  License Copyright:  Dr. A. Schelle, Bachschmidstr. 4, 87600 Kaufbeuren 
  License Type :      MIT license (2023)
  License Contact:    E-Mail : alexej.schelle@gmail.com
 
-2- : 

  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
  (the "Software" bec_symmetry_breaking.py), to deal in the Software without restriction, including without limitation the rights to use, 
  copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
  furnished to do so, subject to the following conditions:
 
  The above copyright notice -1- and this permission notice -2- shall be included in all copies or substantial portions of the Software.
 
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER       DEALINGS IN THE SOFTWARE.

-3- : Free support is provided per email at alexej.schelle@gmail.com. 
   
-4- : For more explicit consulting and discussions, please schedule a meeting at https://calendly.com/alexej-schelle/.  

Note : Please note that, besides that the Python routine works well, a rigorous mathematical proof for the approach to approximate a multiplayer Nash equilibrium is so far still missing.
