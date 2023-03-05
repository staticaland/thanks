"""
A simple example of using the OpenAI API to generate superhero names for animals.
"""
import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    """Main entry point of the app."""

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt("cat"),
        temperature=0.6,
    )

    print(response)


def generate_prompt(animal):
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

if __name__ == "__main__":
    main()