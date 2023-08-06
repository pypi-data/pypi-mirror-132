# autobahn-api

Use this tool to fetch data (roadworks, parking_area) from the Autobahn API provided by [https://bund.dev/](https://bund.dev/). You can find the API documentation [here](https://autobahn.api.bund.dev/).

## Requirements

* Python 3.8+
* requests

To run tests install **pytest**:

    pip3 install pytest # Linux, macOS
    pip install pytest  # Windows

## Install

    pip3 install autobahn-api # Linux, macOS
    pip install autobahn-api  # Windows

## Usage

Use `-r` followed by the Autobahn ID to show all roadworks:

    autobahn-api -r A1

Use `-p` followed by the Autobahn ID to show all parking areas:

    autobahn-api -p A1

## Changelog

see [CHANGELOG.md](https://github.com/niftycode/autobahn-api/blob/main/Changelog.md)
