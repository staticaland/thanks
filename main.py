"""
A simple example of using the OpenAI API to generate superhero names for animals.
"""
import os
import sys
import argparse

import configargparse
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def main(opts: argparse.Namespace):
    """
    Main entry point of the app.

    Args:
        opts: A Namespace object containing the parsed command-line arguments.

    Returns:
        None

    Raises:
        Any exceptions that occur during execution.

    This function generates a text prompt based on the specified animal, and uses OpenAI's text-davinci-003
    model to generate a response. The generated response is printed to the console.
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(opts.animal),
        temperature=0.6,
    )

    print(response)


def generate_prompt(animal: str) -> str:
    """
    Generate a prompt for suggesting superhero names for an animal.

    :param animal: A string representing the name of the animal.
    :return: A string with a prompt for suggesting animal superhero names.
    """

    return f"""Suggest three names for an animal that is a superhero.

    Animal: Cat
    Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
    Animal: Dog
    Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
    Animal: {animal.capitalize()}
    Names:"""


def get_options() -> argparse.Namespace:
    """
    Parses the command line arguments and returns the options as an argparse.Namespace object.

    :return: An argparse.Namespace object containing the parsed command line arguments.
    """

    p = configargparse.ArgParser(default_config_files=["~/.thanks"])

    p.add(
        "-a",
        "--animal",
        help="which animal",
        type=str,
        default="giraffe",
        choices=["cat", "dog", "giraffe"],
    )

    return p.parse_args()


if __name__ == "__main__":
    opts = get_options()

    main(opts)
