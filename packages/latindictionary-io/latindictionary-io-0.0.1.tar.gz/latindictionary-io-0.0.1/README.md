# latindictionary-io API Client

 - API documentation: https://latindictionary.io/docs/api
 - API version: 1.0.0

## Installation

Install package

```sh
pip install latindictionary-io
```

## Getting Started

``` python
import latindictionary_io

# setup the api client
dictionary = latindictionary_io.Client()

# parse words
print(dictionary.analyze_word('canis'))

# get word usage examples from anchient latin texts
print(dictionary.get_concordance('canis'))

# get english definition
print(dictionary.get_definition('canis'))

# get the word of the day from a specified date
print(dictionary.get_word_of_the_day('2022-01-01'))
```