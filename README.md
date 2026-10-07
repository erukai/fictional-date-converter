# Fictional Date Converter
A simple Python tool that converts Earth date to your fictional world date _(and vice versa)_. Useful for fantasy worldbuilding, games, or creative projects.

If you're an author or a game developer who is making a fantasy story of another world and wants to improve the immersion and worldbuilding by creating a custom calendar system, this tool will gladly help you.

This tool can benefit you if:
- you have a fictional world with its own calendar system, and you need to get the equivalent Earth date from a fictional date.
- you need to get the equivalent fictional date from an Earth date

You can use this tool for fun, simply to cure your curiosity, or actual worldbuilding. Whether you're building a detailed fictional world, running a role‑playing campaign, or simply wondering how your fantasy calendar lines up with Earth's, this converter makes it easy to explore those connections. Even if your story doesn't require strict timekeeping, having a consistent system can add depth, realism, and immersion to your worldbuilding.

However, this tool also has its own limitations:

- the tool uses a proleptic Gregorian calendar for the Earth date.
    - <sub>Historically, the Western world uses the Julian calendar for over a millenium until it was replaced with the Gregorian calendar in 1582 CE, which skipped 13 days. The proleptic Gregorian Calendar is a modern concept that assumes the Gregorian Calendar has always been used.<sub>

- this tool expects the user to already have a calendar system prepared before using the tool.
    - <sub>This includes things like _"days in a month"_, "days in a year", "months in a year"<sub>
    - <sub>If you need to create a calendar system, you can use this tool instead:<sub>

- the user must configure the `date_config.toml` file to their calendar system _(including leap year system, if any)_.
    - <sub>Before running the main file _(`main.py`)_, the user must configure the `date_config.toml` file which contains values related to the user's calendar system.<sub>
    - <sub>A calendar is only an approximate of a tropical year, and having leap years is an attempt to fix the mismatch between the calendar and the seasons. Adding leap years to your calendar system increases the immersion and realism of your world.<sub>


This tool is designed to be executed in a Command Line Inteface. For those who prefer a more user-friendly approach, visit this site: