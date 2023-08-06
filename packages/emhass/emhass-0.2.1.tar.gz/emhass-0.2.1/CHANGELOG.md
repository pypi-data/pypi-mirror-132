# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2021-12-22
### Fixed
- Cleaned unittest implementation
### Added
- Added support to choose the methods for weather and load forecast from configuration file.
- Added new load cost and power production price forecasts, mainly allowing the user to load a CSV file with their own forecast.

## [0.2.0] - 2021-10-14
### Fixed
- Fixed tests to pass with latest changes on passing path and logger arguments.
- Updated requirements for PVLib and Protobuf.
- Removed unnecessary use of abstract classes.
- Fixed test_optimization bad setup.
- Fixed logger integration in classes
- Updated documentation
### Added
- Implemented typing for compatibility with Python4
- Implemented different types of cost functions

## [0.1.5] - 2021-09-22
### Fixed
- Fix a recurrent previous bug when using get_loc. The correct default behavior when using get_loc is changed from backfill to ffill.

## [0.1.4] - 2021-09-18
### Fixed
- Fixed a bug when publish-data and reading the CSV file, the index was not correctly defined, so there was a bug when applying pandas get_loc.
### Added
- Added a global requirements.txt file for pip install.

## [0.1.3] - 2021-09-17
### Fixed
- Fixed packaging and configuration for readthedocs.

## [0.1.2] - 2021-09-17
### Fixed
- Modified the cost function equation signs for more clarity. Now the LP is fixed to maximize a profit given by the revenues from selling PV to the grind minus the energy cost of consumed energy.
- Fixed a deprecation warning from PVLib when retrieving results from the ModelChain object. Now using modelchain.results.ac.

## [0.1.1] - 2021-09-17
### Fixed
- Fixed sign error in cost function.
- Change publish_data get_loc behavior from nearest to backfill.
- Changed and updated behavior of the logger. It is constructed and integrated directly in the main function of the command_line.py file. It now writes to a log file by default.
- Fixed some typos and errors in the documentation.

## [0.1.0] - 2021-09-12
### Added
- Added the first public repository for this project.

[0.1.0]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.0
[0.1.1]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.1
[0.1.2]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.2
[0.1.3]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.3
[0.1.4]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.4
[0.1.5]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.5
[0.2.0]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.0
