Software
========

.. image:: https://raw.githubusercontent.com/kabasset/Linx/develop/doc/diagrams/logo_square.svg
   :alt: Linx
   :width: 20%
   :align: right
   :target: https://github.com/kabasset/Linx

Linx
----

Linx is a multidimensional image processing library focused on ease of use and which interfaces seamlessly with the standard C++ library.
For performance and extensibility, it relies heavily on template metaprogramming.

Here is a comparison with NumPy.
Simple array instantiations and operations are performed:

.. code-block:: py

   x = np.linspace(-1, 1, 100)
   f = np.exp(x)
   a = np.ones((2, 3), dtype=int)
   b = np.random.default_rng().random((2, 3))
   c = b - a

Linx:

.. code-block:: cpp

   auto x = Linx::Sequence<double>(100).linspace(-1, 1);
   auto f = exp(x);
   auto a = Linx::Raster<int>({3, 2}).fill(1);
   auto b = Linx::random<double>({3, 2});
   auto c = b - a;

https://github.com/kabasset/Linx


.. image:: https://raw.githubusercontent.com/CNES/EleFits/develop/doc/diagrams/out/elefits_square.svg
   :alt: EleFits
   :width: 20%
   :align: right
   :target: https://github.com/CNES/EleFits

EleFits
-------

EleFits is a modern C++ package to read and write FITS files which focuses on safety, user-friendliness, and performance.
At some point, the ND array implementation of EleFits should be droped in favor of Linx.

Here is a comparison with CFITSIO.
A single-image FITS file is created from a 2D array (``(width, height) -> data``) and a keyword record (``keyword, value, comment``):

.. code-block:: cpp

   long shape[] = { width, height };
   int status = 0;
   fitsfile* fits = nullptr;
   fits_create_file(&fits, filename.c_str(), &status);
   fits_create_img(fits, SHORT_IMG, 2, shape, &status);
   fits_write_key(fits, TDOUBLE, name.c_str(), &value, comment.c_str(), &status);
   fits_write_img(fits, TSHORT, 1, width * height, data, &status);

EleFits:

.. code-block:: cpp

   Fits::SifFile fits(filename, Fits::FileMode::CREATE);
   fits.header().write(keyword, value, "", comment);
   fits.raster().write(makeRaster(data, width, height));

https://github.com/CNES/EleFits


.. image:: https://raw.githubusercontent.com/kabasset/Splider/develop/doc/diagrams/logo_square.svg
   :alt: Splider
   :width: 20%
   :align: right
   :target: https://github.com/kabasset/Splider

Splider
-------

Splider is a cubic spline interpolation library where a spline is a list of components (intervals, knots and arguments), which each hold their cache.
This separation yields huge speed-ups wrt. classical libraries in some cases.

Here is a comparison with GSL, where an input set of knots (``u -> v``) is interpolated at a set of positions (``x``):

.. code-block:: cpp

   gsl_interp_accel* acc = gsl_interp_accel_alloc();
   gsl_spline* spline = gsl_spline_alloc(gsl_interp_cspline, u.size());
   gsl_spline_init(spline, u.data(), v.data(), u.size());
   std::vector<double> y;
   for (const auto& e : x) {
      y.push_back(gsl_spline_eval(spline, e, acc));
   }
   gsl_interp_accel_free(acc);
   gsl_spline_free(spline);

Splider:

.. code-block:: cpp

   const auto build = Spline::builder(u);
   auto spline = build.spline(v);
   auto y = spline(x);

https://github.com/kabasset/Splider
