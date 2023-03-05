# Thanks

This project is a simple example of using the OpenAI API to generate superhero names for animals. The script takes an animal as input, generates a prompt for suggesting superhero names for that animal, and uses OpenAI's text-davinci-003 model to generate a response. The generated response is printed to the console.

## Installation

Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use the superhero name generator, run the `main.py` script with the following command:

`python main.py [-h] [-a {cat,dog,giraffe}]`

The `-a` argument is optional and specifies the animal for which to generate superhero names. The default is `giraffe`.

## Configuration

The OpenAI API key is stored in the `OPENAI_API_KEY` environment variable. Make sure to set this variable to your API key before running the script.