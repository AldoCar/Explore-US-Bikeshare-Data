import time
import pandas as pd
import numpy as np

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
    
    """get user input for city (chicago, new york city, washington)."""
    
    city = input('Which city do you want to know the data for? (Chicago, New York City, Washington)\n').lower()
    
    if city in ['chicago', 'new york city', 'washington']:
        print('You have chosen to explore {} data! let\'s find out!'.format(city))
    else:      
        print('Ooops! There seems to be an error.\n')
        return get_filters()
        
        
        
            
    """get user input for month (all, january, february, ... , june)"""

    month = input('Do you want to skip month\'s filter? type (all) if you want no filter or press ENTER to continue and select the month filters.\n').lower()
    
    while month != 'all':
        month = input('Please write the month of which you want to know the data: January, February, March, April, May, or June\n').lower()
        
        if month not in ['january', 'february', 'march', 'april', 'may', 'june']:
            print('Ooops! There seems to be an error.\n')
        else:
            break
               
        

    """get user input for day of week (all, monday, tuesday, ... sunday)"""
    
    day = input('Do you want to skip day\'s filter? type (all) if you want no filter or press ENTER to continue\n').lower()
    
    while day != 'all':
        day = input("If you want to select a specific day type: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n").lower()
        
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('Ooops! There seems to be an error!\n')
        else:
            break
     


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    """filter by month"""
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    """filter by day"""
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """ display the most common month"""
    common_month = df['month'].mode()[0]
    print('The most common month is {}'.format(common_month))

    """display the most common day of week"""
    m_c_day_of_week = df['day_of_week'].mode()[0]
    print('Most common Day of Week is {}'.format(m_c_day_of_week))

    """display the most common start hour"""
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour is {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    """ Used stackoverflow and Practice problems to write the code"""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """display most commonly used start station"""
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station is {}'.format(Start_Station))

    """display most commonly used end station"""
    End_Station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station is {}'.format(End_Station))

    """display most frequent combination of start station and end station trip"""
    Start_End_Comb = df['Start Station'].str.cat(df['End Station'], sep = ', ')
    Frequent_start_end_Station = Start_End_Comb.value_counts().idxmax()
    print('Most frequest combination of start station and end station trip is:\n{}'.format(Frequent_start_end_Station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """display total travel time"""
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time is :{} seconds! To be clearer: {} minutes or {} hours or {} days!'.format(Total_Travel_Time, Total_Travel_Time/60, Total_Travel_Time/3600, Total_Travel_Time/86400))

    """display mean travel time"""
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time is: {} minutes'.format(Mean_Travel_Time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """Display counts of user types"""
    try:
        user_types = df['User Type'].value_counts()
        print('Users type:\n{}'.format(user_types))
    except KeyError:
        print('No user\'s data here')

    """Display counts of gender"""
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender Count:\n{}'.format(gender_count))
    except KeyError:
        print('No gender\'s data here.')
        

    """Display earliest, most recent, and most common year of birth"""
    try:
        Earliest_birth = np.min(df['Birth Year'])
        print('The earliest year of birth is {}'.format(Earliest_birth))
    except KeyError:
        print('No earliest year of birth\'s data here')
     
    try:
        Most_Recent = np.max(df['Birth Year'])
        print('The most recent year of birth is {}'.format(Most_Recent))
    except KeyError:
        print('No most recent year of birth data here')
        
    try:
        Most_Common = df['Birth Year'].value_counts().idxmax()
        print('The most common birth year is {}'.format(Most_Common))
    except KeyError:
        print('No most common year of birth data here')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    """I created a new function to display the first 5 rows and increase by another 5 rows each time the user requests it."""
    
def rows(df):
    check = input('Do you want to see more data? Type (y) or (n).\n').lower()
    n = 0
    
    while True:
        if check == 'y':
            print(df.head(n + 5))
            n += 5
            check = input('Do you want to see more data? Type (y) or (n).\n')
        else:
            break    
        
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rows(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()