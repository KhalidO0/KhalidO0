# Spline-Interpolation-
## Introduction:

In the mathematical field of numerical analysis, spline interpolation is a form of interpolation where the interpolant is a special 
type of piecewise polynomial called a spline. That is, instead of fitting a single, high-degree polynomial to all of the values at once, 
spline interpolation fits low-degree polynomials to small subsets of the values, for example, fitting nine cubic polynomials between each 
of the pairs of ten points, instead of fitting a single degree-ten polynomial to all of them. Spline interpolation is often preferred over 
polynomial interpolation because the interpolation error can be made small even when using low-degree polynomials for the spline.
Spline interpolation also avoids the problem of Runge's phenomenon, in which oscillation can occur between points when interpolating using 
high-degree polynomials. 


We wish to find each polynomial q i ( x ) {\displaystyle q_{i}(x)} {\displaystyle q_{i}(x)} given the points ( x 0 , y 0 ) {\displaystyle (x_{0},y_{0})} (x_0, y_0) through ( x n , y n ) {\displaystyle (x_{n},y_{n})} {\displaystyle (x_{n},y_{n})}. To do this, we will consider just a single piece of the curve, q ( x ) {\displaystyle q(x)} q(x), which will interpolate from ( x 1 , y 1 ) {\displaystyle (x_{1},y_{1})} (x_{1},y_{1}) to ( x 2 , y 2 ) {\displaystyle (x_{2},y_{2})} (x_{2},y_{2}). This piece will have slopes k 1 {\displaystyle k_{1}} k_{1} and k 2 {\displaystyle k_{2}} k_{2} at its endpoints. Or, more precisely,

    q ( x 1 ) = y 1 , {\displaystyle q(x_{1})=y_{1},} {\displaystyle q(x_{1})=y_{1},}
    q ( x 2 ) = y 2 , {\displaystyle q(x_{2})=y_{2},} {\displaystyle q(x_{2})=y_{2},}
    q ′ ( x 1 ) = k 1 , {\displaystyle q'(x_{1})=k_{1},} {\displaystyle q'(x_{1})=k_{1},}
    q ′ ( x 2 ) = k 2 . {\displaystyle q'(x_{2})=k_{2}.} {\displaystyle q'(x_{2})=k_{2}.}

The full equation q ( x ) {\displaystyle q(x)} q(x) can be written in the symmetrical form

    q ( x ) = ( 1 − t ( x ) ) y 1 + t ( x ) y 2 + t ( x ) ( 1 − t ( x ) ) ( ( 1 − t ( x ) ) a + t ( x ) b ) , {\displaystyle q(x)={\big (}1-t(x){\big )}\,y_{1}+t(x)\,y_{2}+t(x){\big (}1-t(x){\big )}{\Big (}{\big (}1-t(x){\big )}\,a+t(x)\,b{\Big )},} {\displaystyle q(x)={\big (}1-t(x){\big )}\,y_{1}+t(x)\,y_{2}+t(x){\big (}1-t(x){\big )}{\Big (}{\big (}1-t(x){\big )}\,a+t(x)\,b{\Big )},}
    	

     
    	

     
    	

     

     
    	

    (1)

where

    t ( x ) = x − x 1 x 2 − x 1 , {\displaystyle t(x)={\frac {x-x_{1}}{x_{2}-x_{1}}},} {\displaystyle t(x)={\frac {x-x_{1}}{x_{2}-x_{1}}},}
    	

     
    	

     
    	

     

     
