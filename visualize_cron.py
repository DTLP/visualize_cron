import plotly.express as px
import plotly
import pandas as pd
from croniter import croniter
from datetime import datetime, timedelta
import argparse

# Input file argument
parser = argparse.ArgumentParser()
parser.add_argument(
    '--file',
    dest='input_file',
    type=str,
    required=True
    )
args = parser.parse_args()

# Set graph start date to this week's monday 00:00:00
now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
monday = now - timedelta(days = now.weekday())

jobs_list = [] # Each unique job will be stored here

# Save content cron.txt into variable
with open(args.input_file) as f:
    cron = f.readlines()

# Loop through each crontab line
for line in cron:
    # Skip empty lines
    if line[0] == '\n':
        continue
    # Process title lines
    elif line[0] == '#':
        # Split title line into columns
        info = line.split('/')
        # Assign each column to variable
        job_title = info[0]
        job_repeat_times = info[1]
        job_length = info[2]
    # Process job command lines
    else:
        # Split line into columns
        job = line.split(' ')
        # Assign cron time schedule to variable
        cron_schedule = ' '.join([job[0], job[1], job[2], job[3], job[4]])
        # Turn cron schedule string into croniter object
        cron = croniter(cron_schedule, monday)

        # Calculate the Start and End time for each job
        for iteration in range(int(job_repeat_times)):
            job_start = cron.get_next(datetime)
            job_end = job_start + timedelta(minutes=int(job_length))

            # Save job into the list
            job_dict = {'Task':job_title, 'Start':job_start, 'Finish':job_end, 'Resource':job_title}
            jobs_list.append(job_dict)

# Create pandas object using a list of all cron jobs
df = pd.DataFrame(jobs_list)
# Assign columns to variables
tasks = df['Task']
start = df['Start']
finish = df['Finish']

# Create Gannt Chart
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource")
# Update visualisation settings
fig.update_layout(
    font_size=18
    )

# Export the graph
plotly.offline.plot(fig, filename=args.input_file+'.html')
