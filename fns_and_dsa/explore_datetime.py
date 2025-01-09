from datetime import datetime, timedelta

def display_current_datetime():
    print(f"Current date and time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    new_datetime = datetime.now() + timedelta(days=number_of_days)
    print(f'Future date: {new_datetime.strftime("%Y-%m-%d %H:%M:%S")}')

current_datetime = display_current_datetime()
future_date = calculate_future_date()