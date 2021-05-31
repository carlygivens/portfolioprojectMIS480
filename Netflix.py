import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/carlygivens/Desktop/CSU Global/MIS480/MIS480 Portfolio Project/ViewingActivity.csv')

df = df.drop(['Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis = 1)

df['Start Time'] = pd.to_datetime(df['Start Time'], utc = True)

df = df.set_index('Start Time')

df.index = df.index.tz_convert('US/Eastern')

df = df.reset_index()

df['Duration'] = pd.to_timedelta(df['Duration'])

office = df[df['Title'].str.contains('The Office (U.S.)', regex = False)].copy()

office['weekday'] = office['Start Time'].dt.weekday
office['hour'] = office['Start Time'].dt.hour
office['year'] = office['Start Time'].dt.year


office['weekday'] = pd.Categorical(office['weekday'], categories = [0, 1, 2, 3, 4, 5, 6],
                                ordered = True)

office['year'] = pd.Categorical(office['year'], categories = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])

strangerthings = df[df['Title'].str.contains('Stranger Things:', regex = False)].copy()

strangerthings['weekday'] = strangerthings['Start Time'].dt.weekday
strangerthings['hour'] = strangerthings['Start Time'].dt.hour
strangerthings['year'] = strangerthings['Start Time'].dt.year


strangerthings['weekday'] = pd.Categorical(strangerthings['weekday'], categories = [0, 1, 2, 3, 4, 5, 6],
                                ordered = True)

strangerthings['year'] = pd.Categorical(strangerthings['year'], categories = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])

benstrangerthings = strangerthings[strangerthings['Profile Name'].str.contains('Ben', regex = False)].copy()

benstrangerthings_by_year = benstrangerthings['year'].value_counts()

benstrangerthings_by_year = benstrangerthings_by_year.sort_index()

jerestrangerthings = strangerthings[strangerthings['Profile Name'].str.contains('Jere', regex = False)].copy()

jerestrangerthings_by_year = jerestrangerthings['year'].value_counts()

jerestrangerthings_by_year = jerestrangerthings_by_year.sort_index()

breakingbad = df[df['Title'].str.contains('Breaking Bad:', regex = False)].copy()

breakingbad['weekday'] = breakingbad['Start Time'].dt.weekday
breakingbad['hour'] = breakingbad['Start Time'].dt.hour
breakingbad['year'] = breakingbad['Start Time'].dt.year


breakingbad['weekday'] = pd.Categorical(breakingbad['weekday'], categories = [0, 1, 2, 3, 4, 5, 6],
                                ordered = True)

breakingbad['year'] = pd.Categorical(breakingbad['year'], categories = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])

jerebreakingbad = breakingbad[breakingbad['Profile Name'].str.contains('Jere', regex = False)].copy()

jerebreakingbad_by_year = jerebreakingbad['year'].value_counts()

jerebreakingbad_by_year = jerebreakingbad_by_year.sort_index()

carlyoffice = office[office['Profile Name'].str.contains('Carly', regex = False)].copy()

benoffice = office[office['Profile Name'].str.contains('Ben', regex = False)].copy()

jereoffice = office[office['Profile Name'].str.contains('Jere', regex = False)].copy()


carlyoffice_by_year = carlyoffice['year'].value_counts()

carlyoffice_by_year = carlyoffice_by_year.sort_index()

benoffice_by_year = benoffice['year'].value_counts()

benoffice_by_year = benoffice_by_year.sort_index()

ax = jerestrangerthings_by_year.plot(x = 'year', y = 'Duration')
jerebreakingbad_by_year.plot(ax = ax, x = 'year', y = 'Duration')
plt.xlabel('Year')
plt.ylabel('Episode Started')
plt.title('Comparison of Stranger Things and Breaking Bad for one user')
plt.legend(['Stranger Things', 'Breaking Bad'])
plt.show()

ax = carlyoffice_by_year.plot(x = 'year', y = 'Duration')
benoffice_by_year.plot(ax = ax, x = 'year', y = 'Duration')
plt.xlabel('Year')
plt.ylabel('Episodes Started')
plt.title('The Office Comparison of two users')
plt.legend(['Carly', 'Ben'])
plt.show()

# carlyoffice_by_year.plot.line(x = 'year', y = 'Duration', figsize = (20, 10), title = 'Office Episodes Watched by Carly by Year')

# plt.show()

carlyoffice2017 = carlyoffice.loc[(carlyoffice['Start Time'] >= '01/01/2017') &
                                  (carlyoffice['Start Time'] < '12/31/2017')]




# office_by_day = office['weekday'].value_counts()

# office_by_day = office_by_day.sort_index()

# plt.rcParams.update({'font.size': 22})

# office_by_day.plot(kind = 'bar', figsize = (20, 10), title = 'Office Episodes Watched by Day')

# plt.show()

# carlyoffice2017 = office['weekday'].value_counts()

# carlyoffice2017 = carlyoffice2017.sort_index()

# plt.rcParams.update({'font.size': 18})

# carlyoffice2017.plot(kind = 'bar', figsize = (20, 10), title = 'Office Episodes Watched by Day (Carly, 2017)')

# plt.show()