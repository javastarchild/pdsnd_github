# poc: javastarchild@gmail.com
import time
import pandas as pd
import numpy as np

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    not_done = True
    while not_done:
        city = input("Please enter a city to explore: ")
        city = city.lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Not a valid city name. Please enter a valid city name")
        else:
            not_done = False
    # TO DO: get user input for month (all, january, february, ... , june)
    not_done = True
    while not_done:
        month = input("Please enter a month to explore or \"all\": ")
        month = month.lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'july','august','september','october','november','december','all']:
            print("Not a valid month name. Please enter a valid month or \"all\": ")
        else:
            not_done = False
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    not_done = True
    while not_done:
        day = input("Please enter a day of week to explore or \"all\": ")
        day = day.lower()
        if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            print("Not a valid day of week. Please enter a valid day or \"all\": ")
        else:
            not_done = False

    print('-'*40)
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
    
    # load data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] =  pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = [ dt.month for dt in df['Start Time'] ]
    df['day_of_week'] = [ dt.day for dt in df['Start Time'] ]  
    df['hour'] = [ dt.hour for dt in df['Start Time'] ]  


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february','march','april','may','june','july','august','september','october','november','december']
        month = months.index(month) + 1
   
        # filter by month to create the new dataframe
        df = df[df['month']==month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day)
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    # find the most popular hour
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day)

    # TO DO: display the most common start hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print("The most commonly used start station: {} \n".format(most_common_start))

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print("The most commonly used end station: {} \n".format(most_common_end))


    # TO DO: display most frequent combination of start station and end station trip
    df['Start/End Stations'] = df['Start Station'] + "/" + df['End Station']
    most_common_start_end = df['Start/End Stations'].mode()[0]
    print("The most commonly used start/end station trip: {} \n".format(most_common_start_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("The total travel time: {} \n".format(travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: {} \n".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df.groupby(['User Type'])['User Type'].count()
    print("The counts of user types: \n{} \n".format(count_user_types))

    # TO DO: Display counts of gender
    count_gender = df.groupby(['Gender'])['Gender'].count()
    print("The counts of gender: \n{} \n".format(count_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    sorted_yob = sorted(df.groupby(['Birth Year'])['Birth Year'])
    earlist_yob = sorted_yob[0][0]
    most_recent_yob = sorted_yob[-1][0]
    most_common_yob = df['Birth Year'].mode()[0]
    print("The earliest year of birth is {} \n".format(earlist_yob))
    print("The most recent year of birth is {} \n".format(most_recent_yob))
    print("The most common year of birth is {} \n".format(most_common_yob))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        
        keepon = input('\nWould you like to see more data? Enter yes or no.\n')
        if keepon.lower() == 'yes':
            cls()
        else:
            break
        
        station_stats(df)
        
        keepon = input('\nWould you like to see more data? Enter yes or no.\n')
        if keepon.lower() == 'yes':
            cls()
        else:
            break
            
        trip_duration_stats(df)
        
        keepon = input('\nWould you like to see more data? Enter yes or no.\n')
        if keepon.lower() == 'yes':
            cls()
        else:
            break
            
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
