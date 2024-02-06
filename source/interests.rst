Interests
=========

Software Efficiency
-------------------

My main focus in software development is on profiling, optimization and parallelization,
aiming at better *efficiency*.

Ambitious space missions rely more and more on Big Data processing, not to speak about multi-mission and multi-messenger studies.
In parallel, computing center resources are growing fast and open the door to greedy algorithms like AI and MCMC.
More data and more intensive methods means *much* more computation.

At the same time, increasing energy costs and climate change advocate for a more frugal information technology, among others.
Greener infrastructures are being studied and implemented already, but they represent a small part of the mission-level processing budget.

Developers generally measure computational *performance* by profiling well-known metrics like CPU time, RAM usage or IO waits.
Recent and future Big Data space missions like Swot, Euclid or Lisa involve huge ground segments
built on numerous and large computing centers, where hundreds of pipelines, possibly made of thousands of jobs each, are run daily.
In these cases, the individual wall time or memory consumption of a job has a very limited impact on the overall performance.

By contrast, metrics related to adaptability, scalability or CPU caching are directly related to the information throughput and infrastructure sizing,
which are the actual two top-level points of interest.
These metrics have in common that they relate to a ratio between the resources effectively used and the provided resources.
This is what I term *efficiency*.
Put another way, performance-oriented design aims at delivering a given result as fast as possible with unlimited resources,
while efficiency-oriented design aims at delivering as many results as possible in a given (longer) time with limited resources.
Efficiency is a key factor for both better performance and greener IT, and is fundamental in the frame of Big Data systems.

Elegant APIs
------------

C++ is known to be a verbose language full of boilerplate.
Modern C++, i.e. since 2011, enables metaprogramming, and should be seen as a brand new language.
It changes the way software is designed, e.g. thanks to mixins and compile-time computation,
and the way interfaces are designed, e.g. through parameter forwarding and duck typing.
Among others, briliant examples of such elegant APIs include the C++20 ranges library, Eigen or  Niels Lohmann's Json library.

All in all, Modern C++ gives an opportunity to write more performant sorfware with simpler interfaces.
This is also true for more recent languages like Rust, which simplify the library development wrt. C++.

As a developer of several C++ libraries, I like to deliver APIs which yield readable user code.
Although the underlying design is generally complex, the user-level interfaces must feel natural.
A few examples are displayed in :doc:`software`, many more are available in my libraries documentations.


Events Detection and Estimation
-------------------------------

As a PhD student with Inria (team Serpico), I have worked on the detection and estimation of dynamic events in image sequences.
I focused on fluorescence microscopy image sequences and videos of crowded scenes.

Spot Detection
   To quantitatively analyze dynamic phenomena such as the aforementioned membrane dynamics,
   subcellular particles of interest have to be accurately detected.
   In 2014, we proposed ATLAS, a method enabling the segmentation of vesicles in fluorescence microscopy images.
   The segmentation stage amounts to thresholding the Laplacian of Gaussian (LoG) of the image.
   The optimal LoG scale is automatically selected in a scale-space framework,
   and the threshold is locally deduced from a user-specified probability of false alarm.

Membrane Dynamics
   Assessing the dynamics of plasma membrane events in live cell fluorescence microscopy is of paramount interest to understand cell mechanisms.
   In collaboration with UMR144, we develop methods to detect vesicle fusion events,
   and then estimate the associated dynamics in image sequences of total internal reflection fluorescence microscopy (TIRFM).
   Various dynamic models (including translation, diffusion and dissociation) are tested to classify the dynamics of each detected event.

Crowd Motion Analysis
   Assessing crowd behaviors from videos is a difficult task while of interest in many applications.
   We have defined a novel approach, which identifies, from two successive frames only, crowd behaviors expressed by simple image motion patterns.
   It relies on the estimation of a collection of sub-affine motion models in the image,
   a local motion classification based on a penalized likelihood criterion, and a regularization stage involving inhibition and reinforcement factors.
   Relying on this motion descriptor, we have also developed an original and simple method for recovering the dominant paths followed by people in the observed scene.
   We are now working on the on-line detection and localization of abnormal behaviors in videos of crowded scenes.

CanSat
------

During my engineering school years, I have developed, built and flown a dozen CanSats in various competitions,
as the lead of ISAE's team, BudStar.

A CanSat is can-sized drone, which is fully autonomous and completes scientific missions.
The CanSat is launched from a rocket or captive balloon at a height of a few hundred to a few thousand feet.
Then, it must autonomously reach a ground target while probing the atmosphere and sending measurements to a ground station.

Five of our CanSat were presented at international events.
Here is a brief overview of the team background.

.. table::
   :width: 100%
   :widths: 20 80

   ==== ====
   BudStar achievements
   =========
   2009 1st Open CanSat Competition at C'Space, DGAEM, Biscarosse
   \    BudStar wins the first French competition, which is organized by the CNES and Planète Sciences.
   2010 2nd International CanSat Competition, Universidad Politécnica de Madrid
   \    LEEM and UPM organize the biggest CanSat competition in Europe.
        Fifteen nationalities are present.
        BudStar receives the gold medal.
   2010 Toulouse Space Show, Centre de Congrès Pierre Baudis, Toulouse
   \    As the laureate of the French competition, BudStar is invited by the CNES to present French CanSat activies at the show.
   2010 2nd Open CanSat Competition at C'Space, DGAEM, Biscarosse
   \    BudStar introduces the first rover CanSat fitted in the volume of a can.
        It is able to head on grass by applying different torques to two wheels.
   2011 3rd Open CanSat Competition at C'Space, DGAEM, Biscarosse
   \    Laureate of the competition organized by the CNES and Planète Sciences.
   2012 Soyuz-CanSat launch at C'Space, DGAEM, Biscarosse
   \    A dummy CanSat is launched from a Soyuz replica built by students of the Univeristy of Samara, Russia.
        The rocket makes a nominal flight and perfectly releases the CanSat.
        Both descend side-by-side under their respective parachute and land without being harmed.
   2012 ISAE Prize, ISAE, Toulouse
   \    The Soyuz-CanSat project is awarded by the ISAE Prize. 
   ==== ====

Basset
------

Bassets are sausage-shaped dogs with oversized dangling leathers
-- not to be confused with the proud and tufted ears of the lynx.
The most distinctive feature of a basset is definitely the shortness of its legs,
which gave its name to the species (*basset* litteraly means short-legged in French).
Combining the two features means it should be fairly easy for a basset to step on its own ears.
