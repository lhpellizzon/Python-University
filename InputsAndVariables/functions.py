def get_data():
    user_age = input('What is your age?\n')
    print(user_age, 'is very young. At', user_age, 'should you even be out?\n')


def get_user_input():
    user_country = input('What country are you from?\n')
    print('What is you name?')
    user_name = input()
    print('What is your age?')
    user_age = input()
    print('Welcome', user_name, 'aged', user_age, 'from', user_country)


def get_user_data_and_show_types():
    user_age = input('What is your age?\n')
    week_salary = input('How much you earn per week?\n')
    pps_number = input('What is your PPS number?\n')
    user_age_type = type(user_age)
    week_salary_type = type(week_salary)
    pps_number_type = type(pps_number)

    print('Your Age:', user_age, 'Input Type:', user_age_type)
    print('Your Week Salary:', week_salary, 'Input Type:', week_salary_type)
    print('Your PPSN:', pps_number, 'Input Type:', pps_number_type)


def add_wow():
    placeholder = 'Wow.'
    user_hobby = input('What is your hobby?\n')
    user_address = input('What is your home address?\n')

    print(placeholder, user_hobby, 'is really interesting. You live in', user_address)


def enterHeight ():
    min_height = 2

    user_height = float(input("Enter your height in metres:"))

    user_difference = round(float(min_height - user_height), 3)

    print("You are {:0.2f} metres short of {} metres".format(user_difference, min_height))

