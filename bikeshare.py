

import time
import pandas as pd
import numpy as np


# In[2]:


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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city='bla'
    while city != 'Chicago'  and city !=  'New York City' and city != 'Washington':
        city = input('\nFor which of the following cities do you want to see the data? Chicago, New York City or Washington?\n')
        if city != 'Chicago'  and city !=  'New York City' and city != 'Washington':
            print("Your input was not a valid one. Please use one of the given options!\n")


    # get user input for month (all, january, february, ... , june)
    month="a"
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input('\nFor which month do you want to see the data? You can choose between the following options: all, january, february, march, april may and june?\n')
        if month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            print("Your input was not a valid one. Please use one of the given options!\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day="a"
    while day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
        day = input('\nFor which month do you want to see the data? Possible options are: all, monday, tuesday, wednesday, thursday, friday, saturday and sunday?\n')
        if day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
            print("Your input was not a valid one. Please use one of the given options!\n")

    print('-'*40)
    return city, month, day

# In[3]:


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
    city=city.lower().replace(" ", "_")

    filename=city+'.csv'
    df=pd.read_csv(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

   # if month!="all":
   #     df=df.filter(items=month)
   # if day!="all":
   #     df=df.filter(items=day)


    return df


# In[ ]:





# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    t = df['Start Station'].value_counts().head(1).index.tolist()[0]
    s = df['Start Station'].value_counts().head(1)
    s = s.values[0]
    print("Most Commonly Start Station is {} with {} counts.".format(t, s))

    # display most commonly used end station
    t = df['End Station'].value_counts().head(1).index.tolist()[0]
    s = df['End Station'].value_counts().head(1)
    s = s.values[0]
    print("Most Commonly End Station is {} with {} counts.".format(t, s))

    # display most frequent combination of start station and end station trip
    dummy=df.groupby(["Start Station", "End Station"]).size()
    s=dummy.sort_values(ascending=False).head(1)
    print('Most frequent combination started in  {} and ended in {}. It was used {} times.' .format(s.index.tolist()[0][0],s.index.tolist()[0][1],s.head(1).tolist()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:





# In[7]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    r=df['User Type'].value_counts()
    s=r.head(2).index.tolist()[0]
    t=r.values[0]
    print("One user type is {} with {} counts.".format(s,t))
    s=r.head(2).index.tolist()[1]
    t=r.values[1]
    print("The other user type is {} with {} counts.".format(s,t))

    # Display counts of gender
    try:
        r=df['Gender'].value_counts()
        s=r.head(2).index.tolist()[0]
        t=r.values[0]
        print("There are {} users which are {}.".format(t,s.lower()))
        s=r.head(2).index.tolist()[1]
        t=r.values[1]
        print("There are {} users which are {}.".format(t,s.lower()))
    except:
        print("There are no gender information provided for this city.")

    # Display earliest, most recent, and most common year of birth
    try:
        s = df['Birth Year'].min()
        print("The earliest year of birth is {}.".format(int(s)))

        s = df['Birth Year'].max()
        print("The most recent year of birth is {}.".format(int(s)))

        s = df['Birth Year'].value_counts().head(1).index.tolist()[0]
        print("The most common year of birth is {}.".format(int(s)))
    except:
        print("There are no information about the birth year provided for this city.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    s = pd.to_timedelta(str(df['Trip Duration'].sum())+'s')
    print("Total Travel Time: {}.".format(s))

    # display mean travel time
    s = pd.to_timedelta(str(df['Trip Duration'].mean())+'s')

    print("Mean Travel Time: {}.".format(s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)






# In[9]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        df=df.drop(columns=['month','day_of_week','hour'])
        more_data="bla"
        while more_data!="no":
            print(df.sample(n=5))
            more_data=input('\nDo you like to see more raw data? Enter yes or no.\n')


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
