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


def enter_height():
    min_height = 2

    user_height = float(input("Enter your height in metres:"))

    user_difference = round(float(min_height - user_height), 3)

    print("You are {:0.2f} metres short of {} metres".format(user_difference, min_height))


def calc_journey():
    distance = int(input("What is the distance of your journey in kilometres?\n"))
    speed = int(
        input("How fast would you like to travel im km/hour? (Keep in mind you need arrive safe at the destination\n"))
    fuel_distance = int(input("How much does your car run using one litre of gasoline?\n"))
    fuel_cost = int(input("How much does 1 litre os gasoline cost?\n"))

    full_journey = distance / speed
    full_cost = (distance / fuel_distance) * fuel_cost
    print("Your journey will take {} hours and will cost {} euros".format(full_journey, full_cost))


def week_hours():
    paid_per_hour = 19.45
    overtime_rate = 1.5
    user_hours = int(input("How many do you normally work every week?\n"))
    user_overtime = int(input("How many hours did you worked overtime?\n"))

    normal_pay = user_hours * paid_per_hour
    total_overtime = user_overtime * (paid_per_hour *  overtime_rate)
    gross_pay = normal_pay + total_overtime

    print("Your normal wages is {} and you are being paid more {} for overtime work".format(normal_pay, total_overtime))
    print("Your gross pay is", gross_pay)