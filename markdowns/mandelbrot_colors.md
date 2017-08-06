# Adding colors to the Mandelbrot Set

In order to add some colors, one could associate a color for each possible value of iterations.

In the following example, we are switching from RGB colors to HSV (hue, saturation, value) colors. This allows us to change the color easily by modifying only the hue.

@[Use of HSV colors]({"stubs": ["v3/plot.py", "v3/mandelbrot.py"], "command": "sh -c 'python3 v3/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

## Smooth coloring

In the previous example, you can see bands of color. To remove these bands, we can use a fractional escape count, also known as "normalized iteration count". The theory is a bit difficult, if you are interested in the mathematics, you should read this article entitled "[Renormalizing the Mandelbrot Escape](http://linas.org/art-gallery/escape/escape.html)".

The `mandelbrot` function must be modified to add to the result `1 - log(log2(abs(z)))` where `z` is the last computed value of the sequence (`abs(z) > 2`).

@[Smooth coloring]({"stubs": ["v4/mandelbrot.py", "v4/plot.py"], "command": "sh -c 'python3 v4/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

You can also increase the value of `MAX_ITER` to improve the rendering.

## Histogram coloring

In the previous codes, the colors are not equaly distributed. That's particularly true when `MAX_ITER` is high. To improve the situation, the number of pixels for each iteration number is counted up. For each iteration number, a color will be associated by giving a wider range of colors for iteration numbers that concerns more pixels.

@[Histogram and smooth coloring]({"stubs": ["v5/plot.py", "v5/mandelbrot.py"], "command": "sh -c 'python3 v5/plot.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})

And that's all for the Mandelbrot Set! And if you like the Mandelbrot Set, you'll love the Julia Sets!
