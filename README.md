# rFFT-sample
Feature extraction and implementing discrete Fourier Transform for real input. These 2 files of scripts are part of my dissertation thesis.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [References](#references)
- [License](#license)

---
### Clone

- Clone this repo to your local machine using `https://github.com/Abtektas/rFFT-sample.git`

---
## Features

- Feature extraction for every channel of an audio source

- Implementing Hamming Window filter and rFFT

- Making chunks for an audio source

## Usage

- First of all, you have to change the whole `file-location` values to the location of your audio file.
- For splitting the audio file, you may use `splitter.py` and in that script, you have to declare your chunks name.
- In `rFFT.py` script, if you read carefully the comments you may change the customization for your project.

## References

- In `rFFT.py` script, I referenced oneChannel() function from **[this](https://stackoverflow.com/a/23154891)** post.
- About `splitter.py` script, I referenced @SciTechDude 's code from **[this](https://stackoverflow.com/a/36852393/6343126)** post.

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
