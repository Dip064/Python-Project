# ==============================
# UNIT CONVERTER PROJECT
# ==============================

conversion_data = {

    # ---------------- LENGTH ----------------

    "length": {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1, # standard value
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34,
        "NM": 1852,
        "mil": 0.0000254
    },

    # ---------------- AREA ----------------

    "area": {
        "cm2": 0.0001,
        "m2": 1, # standard value
        "ft2": 0.092903,
        "in2": 0.00064516,
        "a": 100,
        "ha": 10000,
        "ac": 4046.86
    },

    # ---------------- VOLUME ----------------

    "volume": {
        "mL": 0.001,
        "L": 1, # standard value
        "cc": 0.001,
        "m3": 1000,
        "in3": 0.0163871,
        "ft3": 28.3168,
        "gal": 3.78541
    },

    # ---------------- MASS ----------------

    "mass": {
        "g": 1, # standard value
        "kg": 1000,
        "t": 1000000,
        "lb": 453.592,
        "oz": 28.3495
    },

    # ---------------- DATA ----------------

    "data": {
        "bit": 1, # standard value
        "B": 8,
        "KB": 8000,
        "KiB": 8192,
        "MB": 8000000,
        "MiB": 8388608,
        "GB": 8000000000,
        "GiB": 8589934592,
        "TB": 8000000000000,
        "TiB": 8796093022208
    },

    # ---------------- SPEED ----------------

    "speed": {
        "m/s": 1, # standard value
        "m/h": 0.000277778,
        "km/s": 1000,
        "km/h": 0.277778,
        "in/s": 0.0254,
        "in/h": 0.00000705556,
        "ft/s": 0.3048,
        "ft/h": 0.0000846667,
        "mi/s": 1609.34,
        "mi/h": 0.44704,
        "kn": 0.514444
    },

    # ---------------- TIME ----------------

    "time": {
        "ms": 0.001,
        "s": 1, # standard value
        "min": 60,
        "h": 3600,
        "d": 86400,
        "wk": 604800
    }
}


# ==============================
# TEMPERATURE CONVERSION
# ==============================

def convert_temperature(value, from_unit, to_unit):

    # Convert to Celsius first

    if from_unit == "celsius":
        c = value

    elif from_unit == "fahrenheit":
        c = (value - 32) * 5 / 9

    elif from_unit == "kelvin":
        c = value - 273.15

    else:
        return None

    # Convert from Celsius to target

    if to_unit == "celsius":
        return c

    elif to_unit == "fahrenheit":
        return (c * 9 / 5) + 32

    elif to_unit == "kelvin":
        return c + 273.15


# ==============================
# MAIN PROGRAM
# ==============================

print("===================================")
print("       UNIT CONVERTER")
print("===================================")

while True:

    print("\nAvailable Categories:\n")

    for category in conversion_data:
        print("-", category)

    print("- temperature")

    category = input("\nEnter category: ").lower()

    # ==========================
    # TEMPERATURE
    # ==========================

    if category == "temperature":

        temp_units = ["celsius", "fahrenheit", "kelvin"]

        print("\nAvailable Units:")

        for unit in temp_units:
            print(unit)

        from_unit = input("\nConvert from: ").lower()
        to_unit = input("Convert to: ").lower()

        if from_unit not in temp_units or to_unit not in temp_units:
            print("Invalid unit!")
            continue

        try:
            value = float(input("Enter value: "))

        except ValueError:
            print("Invalid number!")
            continue

        result = convert_temperature(value, from_unit, to_unit)

        print(f"\nResult: {result:.4f} {to_unit}")

    # ==========================
    # OTHER CATEGORIES
    # ==========================

    elif category in conversion_data:

        units = conversion_data[category]

        print("\nAvailable Units:\n")

        for unit in units:
            print(unit)

        from_unit = input("\nConvert from: ")
        to_unit = input("Convert to: ")

        if from_unit not in units or to_unit not in units:
            print("Invalid units!")
            continue

        try:
            value = float(input("Enter value: "))

        except ValueError:
            print("Invalid number!")
            continue

        # Conversion Formula

        result = (
            value
            * units[from_unit]
            / units[to_unit]
        )

        print(f"\nResult: {result:.6f} {to_unit}")

    else:
        print("Invalid category!")
        continue

    # ==========================
    # REPLAY SYSTEM
    # ==========================

    while True:

        again = input("\nDo another conversion? (y/n): ").lower()

        if again == "y":
            break

        elif again == "n":
            print("\nThanks for using Unit Converter!")
            exit()

        else:
            print("Invalid input!")
