Software
========

|clear-float|

.. image:: https://www.esa.int/var/esa/storage/images/science_exploration/space_science/euclid/24495561-6-eng-GB/Euclid_pillars.png
   :alt: Linx
   :width: 20%
   :align: right
   :target: https://www.esa.int/Science_Exploration/Space_Science/Euclid

Euclid Science Ground Segment
-----------------------------

As a member of the Euclid Science Ground Segment development group, I have been developping software for eight years.
To my knowledge, I have contributed to all of the Euclid Processing Functions but MER.
Here is a summary of my main contributions.

LE1-VIS
   The Level 1 pipeline (LE1) transforms the raw Euclid telemetry into data products usable by downstream pipelines: images and metadata.
   In other words, every Euclid image ever published or processed has been produced by LE1,
   including `Early Realease Observations <https://www.esa.int/Science_Exploration/Space_Science/Euclid/Euclid_s_first_images_the_dazzling_edge_of_darkness>`_
   and `the 208-Gigapixel glimpse <https://www.youtube.com/watch?v=86ZCsUfgLRQ>`_.
   I have implemented the storage class for the telemetry of the VIS instrument and worked on the overall design.
   After more than a year of operations, and 80,000 images produced, not a single bug has been found!

SIM
   As the name implies, the simulation pipeline (SIM) generates simulated images for the Euclid mission.
   It includes simulators of Euclid instruments VIS and NISP, as well as the external surveys used by Euclid.
   My main contribution in terms of software development is the test data management tool,
   which connects on-the-fly to computing centers to feed unit tests with distributed data sets.
   It has been integrated into `Elements <https://github.com/astrorama/Elements>`_.

SIR, SPE
   The near-infrared spectroscopy pipeline (SIR) extract galaxy spectra from the spectro-images of Euclid,
   and then the redshifts are estimated by the spectral features pipeline (SPE).
   I have designed the FITS-based interface between SIR and SPE, and implemented EL_SpectrumLib, the associated I/O library.

SHE
   In order to map dark matter using week-lensing, the shear pipeline (SHE) estimates shape parameters of galaxies.
   It relies on a modelling of the telescope and VIS instrument (the PSF model) with unprecedented precision.
   CNES delivers one of the calibration pipelines which estimate the PSF model.
   I have focused on the computational performance optimization, integration and automation of this pipeline.

On System side, I have been deeply involved in the design, prototyping and testing of the orchestrator (COORS).
I have specified and contributed to the design of the Profiling Database, which stores systematic pipeline profiling metrics.
I have also co-led the System-wide integration test campaigns known as Scientific Challenges,
and developed many automated testing tools for the Euclid Archive System (EAS), for the Infrastructure Abstraction Layer (IAL), for the Common Tools,
as well as for the pipelines themselves.

|clear-float|

.. image:: https://raw.githubusercontent.com/kabasset/azulero/v0.1.0/azul.png
   :alt: Azul
   :width: 20%
   :align: right
   :target: https://github.com/kabasset/azulero

Azul
----

Azul is a package aimed at streamlining the production of Public Outreach data based on Euclid scientific products.
It provides tools for finding, downloading and fusing images produced by MER, as well as generating pan-and-zoom videos.

Public images (data releases) can be processed by anyone outside the consortium.
For example, the image below is produced with::

   pip install azulero
   azul retrieve 102159776
   azul process 102159776

.. figure:: https://raw.githubusercontent.com/kabasset/azulero/develop/UGC11116.jpg
   :alt: UGC11116
   :width: 100%
   :align: center
   :target: https://github.com/kabasset/azulero

   Color image of UGC11116 produced with Azul from public Euclid Q1 data.
   
   Credit: ESA Euclid / Euclid Consortium / NASA / Q1-2025 / Antoine Basset (CNES)

|clear-float|

.. image:: https://raw.githubusercontent.com/kabasset/Linx/develop/doc/diagrams/logo_square.svg
   :alt: Linx
   :width: 20%
   :align: right
   :target: https://github.com/kabasset/Linx

Linx
----

Linx is a C++ multidimensional image processing library focused on ease of use and performance protability.
Image processing pipelines written with Linx can run on a variety of infrastructures, including HTC, HPC and GPU farms.

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

|clear-float|

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

|clear-float|

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

.. |clear-float| raw:: html

   <div style="clear: both"></div>
