def get_user_words():
    """Collects words from the user for the Mad Libs game."""
    words = {
        "adjective": input("Enter an adjective:"),
        "animal": input("Enter an animal:"),
        "color": input("Enter a color:"),
        "place": input("Enter a place:"),
        "plural_noun": input("Enter a Plural Noun:"),
        "sound": input("Enter a sound:"),
        "verb": input("Enter a verb:"),
        "emotion": input("Enter an Emotion:"),
        "drink": input("Enter a drink:"),
        "verb2": input("Enter a verb2:"),
        "food": input("Enter a food:")
    }
    return words


def create_story(words):
    """Generates the story using the provided words."""
    story_template = f"""One day, a {words["adjective"]} {words["animal"]} wore a {words["color"]} hat and went to {words["place"]} with a bag full of {words["plural_noun"]}. It shouted "{words["sound"]}!" and started to {words["verb"]} on the table. Everyone was so {words["emotion"]} that they spilled their {words["drink"]}. Then the {words["animal"]} said, never forget the {words["verb2"]} before breakfast. And disappeared into a bowl of {words["food"]}."""
    return story_template


def main():
    """Main function to run the Mad Libs game."""
    print("Welcome to Alishba's Mad Libs Game!")
    print("Please provide the following words:")

    user_words = get_user_words()
    mad_libs_story = create_story(user_words)

    print("\nHere is Alishba's Mad Libs story:")
    print(mad_libs_story)


if __name__ == "__main__":
    main()