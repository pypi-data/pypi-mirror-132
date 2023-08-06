
History
=======

v0.4.0
------
* Separate out ``resample_ics`` and ``bias_correct_temps`` into two functions.

v0.3.1
------
* Remove unnecessary arg from ``bias_correct_temps_and_resample_ics``

v0.3.0
------
* Add ``project`` module with limited functionality.

v0.2.1
------
* Fix bug in ``resize_T`` function

v0.2
----
* Add ``calc_sl`` function

v0.1.2
------
* Fix bug where historical data SL covariance matrix was top-coded at 0 instead of bottom-coded
* Fix bug where historical data T0 was incorrectly calculated

v0.1.1
------
* Initial commit containing ``load_data_SESL``, ``calc_temp``, and ``calc_T0`` functions
