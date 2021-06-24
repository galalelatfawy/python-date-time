def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days equals to: {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

#
# user_input = input("Hey user, enter number of days and conversion unit!\n")
# days_and_unit = user_input.split(":")
# days_unit_dic = {"days": days_and_unit[0], "unit": days_and_unit[1]}
# print(days_unit_dic)
# user_input_number = int(days_unit_dic["days"])
# user_input_unit = days_unit_dic["unit"]
# print(f"{user_input_number} and {user_input_unit}")
# out = days_to_units(user_input_number, days_unit_dic["unit"])
# print(out)
##############


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")
