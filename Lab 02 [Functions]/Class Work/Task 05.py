

#Task 5
def number_of_days(total_days):
    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30
    print(f'{years} years, {months} months and {days} days')
input_days=int(input())
number_of_days(input_days)