import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ('chicago', 'new york city', 'washington')
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the name of the city to analyze (chicago, new york city, washington) : ").lower()
    while city not in cities:
        print("Enter a Valid Name!!")
        city = input("Enter the name of the city to analyze (chicago, new york city, washington) : ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        "Enter the name of the month to filter by, or all to apply no month filter (all, january, february, ... , june) : ").lower()
    while month not in months:
        print("Enter a Valid Name!!")
        month = input(
            "Enter the name of the month to filter by, or all to apply no month filter (all, january, february, ... , june) : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Enter the name of the day of week to filter by, or all to apply no day filter (all, monday, tuesday, ... sunday) : ").lower()
    while day not in days:
        print("Enter a Valid Name!!")
        day = input(
            "Enter the name of the day of week to filter by, or all to apply no day filter (all, monday, tuesday, ... sunday) : ").lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month : ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week : ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour : ", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station : ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station : ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    Max = df.groupby(['Start Station', 'End Station']).count().max()[0]
    data = df.groupby(['Start Station', 'End Station']).count().reset_index()
    start_Station = data[data["User Type"] == Max]["Start Station"].values[0]
    end_Station = data[data["User Type"] == Max]["End Station"].values[0]
    print("The most most frequent combination of start station and end station trip : \nStart Station : ",start_Station, "\nEnd Station : ", end_Station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time : ", df["Trip Duration"].sum())
    # TO DO: display mean travel time
    print("The mean travel time : ", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types :")
    userTypes = df['User Type'].value_counts()
    for userType in userTypes.index:
        print(userType, ":", userTypes[userType])

    # TO DO: Display counts of gender
    try:
        print("The counts of gender :")
        genderTypes = df['Gender'].value_counts()
        for genderType in genderTypes.index:
            print(genderType, ":", genderTypes[genderType])
    except:
        print("No Gender Data!!!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth :",df["Birth Year"].min())
        print("The most recent year of birth :", df["Birth Year"].max())
        print("The most common year of birth :", df["Birth Year"].mode()[0])
    except:
        print("No Birth Year Data!!!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_five_lines(df,start):
    """This Function Displays Five Lines of Raw Data of bikeshare users."""
    print('\nShowing Five Lines Of Users Data...\n')
    start_time = time.time()
    print(df.iloc[start:start+5])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        choice = input("Do you want to see the time stats of {} (Yes/No) : ".format(city)).lower()
        while choice not in ['yes','no']:
            print("Enter a Valid Input!!!")
            choice = input("Do you want to see the time stats of {} (Yes/No) : ".format(city)).lower()
        if choice == 'yes': time_stats(df)
        choice = input("Do you want to see the station stats of {} (Yes/No) : ".format(city)).lower()
        while choice not in ['yes', 'no']:
            print("Enter a Valid Input!!!")
            choice = input("Do you want to see the station stats of {} (Yes/No) : ".format(city)).lower()
        if choice == 'yes': station_stats(df)
        choice = input("Do you want to see the trip duration stats of {} (Yes/No) : ".format(city)).lower()
        while choice not in ['yes', 'no']:
            print("Enter a Valid Input!!!")
            choice = input("Do you want to see the trip duration stats of {} (Yes/No) : ".format(city)).lower()
        if choice == 'yes': trip_duration_stats(df)
        choice = input("Do you want to see the user stats of {} (Yes/No) : ".format(city)).lower()
        while choice not in ['yes', 'no']:
            print("Enter a Valid Input!!!")
            choice = input("Do you want to see the user stats of {} (Yes/No) : ".format(city)).lower()
        if choice == 'yes': user_stats(df)
        start = 0
        while True:
            if start == 0:
                choice = input("Do you want to see 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
                while choice not in ['yes', 'no']:
                    print("Enter a Valid Input!!!")
                    choice = input("Do you want to see 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
            else:
                choice = input("Do you want to see another 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
                while choice not in ['yes', 'no']:
                    print("Enter a Valid Input!!!")
                    choice = input("Do you want to see another 5 lines of raw data of {} (Yes/No) : ".format(city)).lower()
            if choice == 'yes':
                display_five_lines(df, start)
                start += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("You're Welcome!!".center(50,'-'))
            break


if __name__ == "__main__":
    main()