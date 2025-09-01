import inquirer

def get_location_type():
    questions = [
        inquirer.List(
            "location type",
            message="Select one of the options to see weather",
            choices=["My location", "Custom location"],
        ),
    ]

    answers = inquirer.prompt(questions)

    if answers is not None:
        return answers["location type"]

    return "My location"


def get_user_input():
    questions = [
        inquirer.Text(
            "city",
            message="Enter the city name",
        )
    ]

    answers = inquirer.prompt(questions)

    if answers is not None:
        return answers["city"]

    return None
