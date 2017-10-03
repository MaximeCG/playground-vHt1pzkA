# Mandelbrot Set

te

The mandelbrot set is one of the most famous fractal, and it's very easy to draw. In this playground you will learn how to plot this:

![Mandelbrot Set](../cover.png)

## Definition

The mandelbrot set is defined by the set of complex numbers $`c`$ for which the complex numbers of the sequence $`z_n`$ remain bounded in absolute value. The sequence $`z_n`$ is defined by:

- $`z_0 = 0`$
- $`z_{n+1} = z_n^2 + c`$

As a reminder, the modulus of a complex number is its distance to 0. In Python, this is obtained using `abs(z)` where `z` is a complex number. We assume that the sequence $`z_n`$ is not bounded if the modulus of one of its terms is greater than 2.

A complex number ($`x + iy`$) can be represented on a complex plane. The real part of the complex number is represented by a displacement along the x-axis and the imaginary part by a displacement along the y-axis.

The visual representation of the mandelbrot set may be created by determining, for each point $`c`$ of a part of the complex plane, whether $`z_n`$ is bounded. The number of iterations to reach a modulus greater than 2 can be used to determine the color to use.

If still unclear, I recommend watching the great explanation of:

[Dr Holly Krieger from MIT](https://www.youtube.com/watch?v=NGMRB4O922I)

## Computation of the Terms of the Sequence

Let's define the function `mandelbrot` that will return the number of iterations needed to reach a modulus greater than 2. If the number of iterations is greater than `MAX_ITER`, stop and return `MAX_ITER`.

@[]({"stubs": ["v1/mandelbrot.py"], "command": "python3 v1/mandelbrot.py"})

## Plot of the Mandelbrot Set

Plotting the mandelbrot set is relatively simple:

- Iterate over all the pixels of your image
- Convert the coordinate of the pixel into a complex number of the complex plane
- Call the function `mandelbrot`
- If `mandelbrot` returns `MAX_ITER`, plot a black pixel, otherwise plot a pixel in a color that depends on the number of iterations returned by `mandelbrot`

This is called the "Escape time algorithm".

@[Black and white image]({"stubs": ["v2/plot.py", "v2/mandelbrot.py"], "command": "sh -c 'python3 v2/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

Feel free to change the plot window by changing the variables `RE_START`, `RE_END`, `IM_START` and `IM_END`. You can also change the espace radius or the value of `MAX_ITER`.

In the next section, we will add some colors to our draw.
