# Taylor's Bubble Model

This package contains a model of a taylor's tube, i.e., a system where single bubbles, 
called taylor's bubbles, move up inside a tube filled with a specific liquid. This system
is designed to optimize the velocity of dissolution of gas in liquid , until the liquid gets 
completely saturated.

Github link: https://github.com/Borjapy/bubble_package

Physical variables' values have to be introduced using a python dictionary. Variables wich 
can be setted are: temperature (T), difusivity (D), radius of the tube (rc), average fluid 
velocity of the liquid-gas system (Utp), initial concentration (cs), equilibrium concentration 
(ceq), minimum value of z (zmin), maximum value of z (zmax), resolution of z-axis (zpoints), 
resolution of y-axis (ypoints), number of terms in developments (N), longitudinal lenght of gas phase
between bubbles (GSL) and lenght of bubbles without the caps (LSL). Furthermore, a parameter 
(idealgas) determine if the gas loss in the transfer is taken in account or despised ( see
example 3 for further information ).
  
The calculations avaiable in the model are:
 - Calculation of concentration profile in bubble and slug zone (note: the concentration profile
   of the bubble have to be calculated before slug, due to it is considered the first zone in the 
   cell). The result is calculated as two arrays, one for the wall-distance parameter and the other
   for the concentration, wich can be easily represented.
 - Calculation of kla. Kla is the main parameter utilized in quantifications of gas-liquid exchange 
   process. It is possible to calculate the bubble's cap contribution, the film between bubble and 
   wall contribution or the whole value.
 - Calculation of the whole column of bubbles (tube): simulation of gas transference in a tube 
   filled with gas bubbles. It shows the complete saturation in the gas when it get out of the tube. 
   Furthermore, it calculates the average relative concentration of gas in every slug.
   
The files contained in the package are:
 - oModel: contains the main object of the model, including main methods to main 
   calculations.
 - varsSetters: contains the hierarchical parent object of the main object, including
   the methods and variables utilized to manage the parameters of the simulation.
 - customErrors: contains extra errors utilized to control certain situations in the 
   simulations.
 - mFits: contains the methods to determine physic parameters (viscosity, density and surface
   tension) from temperature. It is done by fitting the temperature in experimental data.