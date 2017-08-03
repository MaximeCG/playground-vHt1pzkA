# Mandelbrot Set

The mandelbrot set is one of the most famous fractal. It is defined by the set of complex numbers $`c`$ for which the complex numbers of the sequence $`z_n`$ remain bounded in absolute value. The sequence $`z_n`$ is defined by:

- $`z_0 = 0`$
- $`z_{n+1} = z_n^2 + c`$

A complex number ($`x + iy`$) can be represented on a complex plane. The real part of the complex number is represented by a displacement along the x-axis and the imaginary part by a displacement along the y-axis.

As a reminder, the modulus of a complex number is its distance to 0. In Python, this is obtained using `abs(z)` where `z` is a complex number. Usually, we assume that the sequence $`z_n`$ is bounded if its modulus is lower than 2.

The visual representation of the mandelbrot set may be created by determining, for each point $`c`$ of a part of the complex plane, whether $`z_n`$ is bounded. The number of iterations to reach a modulus greater than 2 can be used to determine the color to use.

For more details, I recommend watching the great explanation of Dr Holly Krieger from MIT: https://www.youtube.com/watch?v=NGMRB4O922I

# Computing the terms of the sequence

Let's define the function `mandelbrot` that will return the number of iterations needed to reach a modulus greater than 2. If the number of iterations is greater than `MAX_ITER`, stop and return `MAX_ITER`.

@[]({"stubs": ["v1/mandelbrot.py"], "command": "python3 v1/mandelbrot.py"})

# Plotting the mandelbrot set

@[]({"stubs": ["v2/plot.py", "v2/mandelbrot.py"], "command": "sh -c 'python3 v2/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

@[]({"stubs": ["v3/plot.py", "v3/mandelbrot.py"], "command": "sh -c 'python3 v3/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

@[]({"stubs": ["v4/plot.py", "v4/mandelbrot.py"], "command": "sh -c 'python3 v4/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})
