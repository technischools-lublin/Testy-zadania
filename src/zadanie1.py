def sum_numbers_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            text = file.read().strip()  # Usuwanie białych znaków z początku i końca
            if not text:
                return 0  # Jeśli plik jest pusty, zwracamy 0
            total_sum = 0
            numbers = text.split(";")
            for num in numbers:
                num = num.strip()  # Usuwanie białych znaków z liczby
                if not num:
                    continue  # Pomijanie pustych elementów
                num = int(num)
                if num < -10 or num > 10:
                    raise ValueError("Number out of range.")  # Rzucenie błędu, jeśli liczba jest ujemna
                total_sum += num
            return total_sum
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    except ValueError:
        raise ValueError("Invalid value found in the file.")
    except Exception as e:
        raise e

print(sum_numbers_from_file("file.txt"))
