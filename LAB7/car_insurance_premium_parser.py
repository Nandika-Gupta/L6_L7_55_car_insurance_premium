
def normalize_registration(plate):
    """
    Removes spaces, dashes and dots from a registration number.
    Handles unexpected inputs without crashing.
    """
    if not isinstance(plate, str):
        return ""

    plate = plate.strip().upper()

    for ch in [' ', '-', '.']:
        plate = plate.replace(ch, '')

    return plate


def total_claim_amount(text):
    """
    Adds up valid claim amounts separated by semicolons.
    Invalid or empty entries are ignored.
    """
    if not isinstance(text, str) or not text.strip():
        return 0

    total = 0

    for amount in text.split(';'):
        try:
            value = int(amount.strip())

            if value >= 0:
                total += value

        except ValueError:
            continue

    return total


def driver_age(dob, current_year=2026):
    """
    Calculates age from a DD/MM/YYYY date of birth.
    Handles malformed or unexpected inputs.
    """
    if not isinstance(dob, str):
        return 0

    try:
        parts = dob.strip().split('/')

        if len(parts) != 3:
            return 0

        day, month, year = map(int, parts)

        from datetime import date

        birth_date = date(year, month, day)

        if birth_date > date(current_year, 12, 31):
            return 0

        return current_year - year

    except (ValueError, TypeError):
        return 0


def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    print("Normalized registration:", normalize_registration(value))

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    print("Total claimed:", total_claim_amount(value))

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    print("Driver age in 2026:", driver_age(value))


if __name__ == "__main__":
    main()
