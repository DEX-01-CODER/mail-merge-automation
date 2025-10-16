from pathlib import Path
from datetime import date

# Default placeholders
PLACEHOLDERS = {
    "[name]": None,
    "[date]": str(date.today()),
    "[event]": "Special Event"
}


def generate_letters(names_path, template_path, output_dir, extra_data=None):
    """
    Generate personalized letters by replacing placeholders in a template.
    Supports multiple placeholders like [name], [date], [event].
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    names_file = Path(names_path)
    template_file = Path(template_path)

    # Read and clean data
    names = [n.strip() for n in names_file.read_text(encoding="utf-8").splitlines() if n.strip()]
    letter_template = template_file.read_text(encoding="utf-8")

    # Merge any extra placeholders
    placeholders = PLACEHOLDERS.copy()
    if extra_data:
        placeholders.update(extra_data)

    for name in names:
        placeholders["[name]"] = name
        personalized_letter = letter_template

        for key, value in placeholders.items():
            if value:
                personalized_letter = personalized_letter.replace(key, value)

        output_file = output_dir / f"Letter_to_{name}.txt"
        output_file.write_text(personalized_letter, encoding="utf-8")

    print(f"✅ Letters generated successfully in: {output_dir.resolve()}")


def main():
    base_path = Path(__file__).parent
    names_path = base_path / "Input" / "Names" / "invited_names.txt"
    template_path = base_path / "Input" / "Letters" / "starting_letter.txt"
    output_dir = base_path / "Output" / "ReadyToSend"

    # You can add custom event/date placeholders if needed
    extra_data = {"[event]": "Python Study Group Meetup"}
    generate_letters(names_path, template_path, output_dir, extra_data)


if __name__ == "__main__":
    main()












