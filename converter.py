"""Конвертер величин: довжина, вага, температура, валюта."""

# Коефіцієнти до базової одиниці (метр, кілограм)
LENGTH = {
    "мм": 0.001,
    "см": 0.01,
    "м": 1,
    "км": 1000,
    "дюйм": 0.0254,
    "фут": 0.3048,
    "миля": 1609.344,
}

WEIGHT = {
    "г": 0.001,
    "кг": 1,
    "т": 1000,
    "унція": 0.028349523,
    "фунт": 0.45359237,
}

TEMPERATURES = ("C", "F", "K")


def convert_linear(value, from_unit, to_unit, table):
    """Конвертація через базову одиницю."""
    return value * table[from_unit] / table[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Конвертація температури через градуси Цельсія."""
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15


def convert_currency(value, rate):
    """Валюта: курс вводить користувач (щоб не залежати від інтернету)."""
    return value * rate


def ask_number(prompt):
    """Просить число, поки користувач не введе правильно."""
    while True:
        text = input(prompt).replace(",", ".")
        try:
            return float(text)
        except ValueError:
            print("Це не число, спробуй ще раз.")


def ask_unit(prompt, options):
    """Просить одиницю зі списку."""
    while True:
        unit = input(f"{prompt} ({', '.join(options)}): ").strip()
        if unit in options:
            return unit
        print("Такої одиниці немає, спробуй ще раз.")


def run_table_converter(table, name):
    print(f"\n--- {name} ---")
    value = ask_number("Число: ")
    from_unit = ask_unit("З", list(table))
    to_unit = ask_unit("У", list(table))
    result = convert_linear(value, from_unit, to_unit, table)
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")


def run_temperature():
    print("\n--- Температура ---")
    value = ask_number("Число: ")
    from_unit = ask_unit("З", TEMPERATURES)
    to_unit = ask_unit("У", TEMPERATURES)
    result = convert_temperature(value, from_unit, to_unit)
    print(f"{value} °{from_unit} = {result:.2f} °{to_unit}")


def run_currency():
    print("\n--- Валюта ---")
    value = ask_number("Сума: ")
    rate = ask_number("Курс (скільки одиниць нової валюти за 1 стару): ")
    result = convert_currency(value, rate)
    print(f"Результат: {result:.2f}")


def main():
    actions = {
        "1": ("Довжина", lambda: run_table_converter(LENGTH, "Довжина")),
        "2": ("Вага", lambda: run_table_converter(WEIGHT, "Вага")),
        "3": ("Температура", run_temperature),
        "4": ("Валюта", run_currency),
    }

    print("=== Конвертер величин ===")
    while True:
        print("\nМеню:")
        for key, (title, _) in actions.items():
            print(f"{key}. {title}")
        print("0. Вихід")

        choice = input("Твій вибір: ").strip()
        if choice == "0":
            print("До зустрічі!")
            break
        if choice in actions:
            actions[choice][1]()
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()
