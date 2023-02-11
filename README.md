# visualize_cron

Turning your crontab into a graph to help you identify any overlapping jobs and also find gaps between scheduled jobs.

## Requirements
croniter==1.3.8
pandas==1.5.3
plotly==5.13.0

## How to
1\. Add extra parameters to your cron job description lines separated by `/` :  
```
# title / number of iterations a day / execution time in minutes
```
Example below will result in 5 unique jobs taking 1 minute to run each day
```
# Copy file from A to B / 5 / 1
0 5,6,7,8,9 * * * /script.sh
```
2\. Export your cron jobs to a .txt file  
3\. Run the script specifying the path to the cron txt file as an argument
```
python3 visualize_cron.py --file cron.txt
```
4\. Open up the result .html file to view the graph

## Example
The following input crontab
```
#Job A / 1 / 10
20 9 * * 1-5 <cron job command>
#Job A / 1 / 10
25 11 * * 1-5 <cron job command>
#Job A / 4 / 10
55 13,14,16,18 * * 1-5 <cron job command>

#Job B / 1 / 30
0 8 * * * <cron job command>

#Job C / 1 / 5
10 9 * * 1-5 <cron job command>
#Job C / 1 / 5
25 11 * * 1-5 <cron job command>
#Job C / 4 / 5
55 13,14,16,18 * * 1-5 <cron job command>

#Job D / 1 / 15
10 6 * * 1-5 <cron job command>
#Job D / 1 / 15
25 7 * * 1-5 <cron job command>
#Job D / 4 / 15
52 8,9,10,12 * * 1-5 <cron job command>
```

will result in a graph looking like this  
![alt text](https://github.com/DTLP/visualize_cron/blob/main/example.png?raw=true)
