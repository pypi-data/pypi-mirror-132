# autobahn-api

Use this tool to fetch data (roadworks, parking_area) from the Autobahn API provided by [https://bund.dev/](https://bund.dev/). You can find the API documentation [here](https://autobahn.api.bund.dev/).

## Requirements

* Python 3.7+
* requests

To run tests install **pytest**:

    pip3 install pytest # Linux, macOS
    pip install pytest  # Windows

## Install

    pip3 install autobahn-api # Linux, macOS
    pip install autobahn-api  # Windows

## Usage

Show all roadworks for Autobahn A1:

    autobahn-api -r A1

Show all parking areas for Autobahn A1:

    autobahn-api -p A1

## Changelog

see [CHANGELOG.md](https://github.com/niftycode/autobahn-api/blob/main/Changelog.md)
