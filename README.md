# Street Intersection Finder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python script for finding streets that intersect with a target street in a given shapefile using Geopandas.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Search by Street Name](#Search-by-Street-Name)
- [Search by Geometry](#Search-by-Geometry-(Coordinates))
- [Acknowledgments](#acknowledgments)

## Description

The Street Intersection Finder is a Python script designed to simplify geospatial analysis by allowing users to identify streets that intersect with a target street within a given shapefile. It is particularly useful for urban planning, GIS, or any application where you need to find streets that share common boundaries.

The script utilizes the Geopandas library to work with geospatial data and offers two methods for selecting the target street: by name or by specifying its coordinates.

## Features

- Search for intersecting streets by street name or geometry.
- User-friendly command-line interface.
- Utilizes Geopandas for efficient geospatial operations.
- Easily customizable and extendable.

## Getting Started

### Prerequisites

Before using this script, you need to have the following prerequisites installed on your system:

- Python 3.x
- Geopandas
- Shapely

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/YourUsername/Street-Intersection-Finder.git

Navigate to the project directory:

```shell
    cd Street-Intersection-Finder
```
Install the required Python packages:
```shell
pip install geopandas shapely
```


## Usage

1. Run the script by executing python module4.py from the command line.

2. Follow the prompts to select your target street by either name (N) or geometry (G).

3. Enter the required information as requested.

4. The script will then display the names of streets that intersect with the target street.

## Examples

## Search by Street Name
```shell
Search by name (N) or geometry (G)? N
Enter the name of the target street: Main Street 
```
## Search by Geometry (Coordinates)

```shell
Search by name (N) or geometry (G)? G
Enter the X coordinate for the target street: 12.345
Enter the Y coordinate for the target street: 67.890
```

## Acknowledgments
1. Geopandas - For geospatial data manipulation.
2. Shapely - For geometric operations.

