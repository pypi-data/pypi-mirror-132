# Easy METAR
A simple python script that makes it easy for users to retrieve METAR information from the NWS website.

Essentially, this is a single function which accepts an airport and which data to return as the input. The function will return a string of the information the user requested or a string if an error occurred.

# Usage
getWeather('airport','desired-data')

Replace 'airport' with the desired airport identifier ex: 'kacy' for Atlantic city international airport. Replace 'desired-data' with the information from the METAR which you wish to retrieve

Options for 'desired-data' include:

* 'all' returns the entire METAR as a string

* 'dataAt' returns the date and time at which the function was called as a string

* 'location' returns the airport for which the METAR is issued as a string

* 'dateTime' returns the date and time for which the METAR is issued as a string

* 'wind' returns the wind component of the METAR as a string

* 'visibility' returns the visibility component of the METAR as a string

* 'skyCondition' returns the sky condition and cloud coverage component(s) of the METAR as a string

* 'TDPS' returns the temperature/dew point component of the METAR as a string

* 'Alt' returns the altimeter setting component of the METAR as a string

* 'RMK' returns the entire remarks section of the METAR as a string

Note: you must include the quotation marks when calling the function, it accepts two strings as arguments
