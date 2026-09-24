import art
import json

class InvalidOperationError(Exception):
    pass

def show_history(history):
    if not history:
        print("No history available")
        return

    for operation in history:
        print(f"{operation['first_number']} "
              f"{operation['operation']} "
              f"{operation['second_number']} = "
              f"{operation['result']}")

def record_operation(history,**kwargs):
    history.append(kwargs)

def calculator(*args,**kwargs):
    if kwargs["decision"] == "+":
        return args[0] + args[1]
    elif kwargs["decision"] == "-":
        return args[0] - args[1]
    elif kwargs["decision"] == "*":
        return args[0] * args[1]
    elif kwargs["decision"] == "/":
        if args[1] == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return args[0] / args[1]
    elif kwargs["decision"] == "%":
        if args[1] == 0:
            raise ZeroDivisionError("Mod by zero is not allowed")
        return args[0] % args[1]
    elif kwargs["decision"] == "**":
        return args[0] ** args[1]
    raise InvalidOperationError(f"{kwargs['decision']} is not a valid operation")

print(art.logo)
print(art.title)
print("Operations:\nadd (+)\nsubtract (-)\nmultiply (*)\ndivision (/)\nmod (%)\npower (**)")
operating = True
result = None
history = []

try:
    with open("history.json", "r") as file:
        history = json.load(file)

except FileNotFoundError:
    history = []

except json.JSONDecodeError:
    history = []

while operating:
    if result is None:
        try:
            first_number = float(input("Please enter a number: "))
            decision = input("Please enter an operation: ").strip()
            second_number = float(input("Please enter a number: "))

            result = calculator(
                first_number,
                second_number,
                decision = decision
            )

        except ValueError:
            print("Please enter a valid number")

        except ZeroDivisionError as error:
            print(f"Error occurred: {error}")

        except InvalidOperationError as error:
            print(error)

        else:
            print(f"The result of the operation is {result}")
            record_operation(history,
                             first_number=first_number,
                             operation=decision,
                             second_number=second_number,
                             result=result)

    else:
        choice = input(f"Would you like to keep operating with {result}? (y/n/q/h): ").strip().lower()

        if choice not in ("y", "n", "q", "h"):
            print("Please enter 'y' or 'n' or 'q' or 'h'")
            continue

        elif choice == "q":
            operating = False
            print("Calculator has been stopped")
            with open("history.json", "w") as file:
                json.dump(history, file, indent=4)

        elif choice == "h":
            show_history(history)

        elif choice == "y":
            try:
                first_number = result
                decision = input("Please enter an operation: ").strip()
                second_number = float(input("Please enter a number: "))

                result = calculator(
                        first_number,
                    second_number,
                    decision = decision
                )

            except ValueError:
                print("Please enter a valid number")

            except ZeroDivisionError as error:
                print(f"Error occurred: {error}")

            except InvalidOperationError as error:
                print(error)

            else:
                print(f"The result of the operation is {result}")
                record_operation(history,
                                 first_number=first_number,
                                 operation=decision,
                                 second_number=second_number,
                                 result=result)

        else:
            result = None