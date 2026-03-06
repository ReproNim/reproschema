# Monitor Study Progress

Track participant engagement and protocol performance in real-time.

## Goal

Gain insights into data collection progress and identify issues early.

## Prerequisites

- Deployed protocol
- Access to server logs or database

## Metrics to Track

### 1. Participation Metrics

#### Completion Rates
```python
import pandas as pd

# Load responses
df = pd.read_json('responses.json')

# Calculate completion rate
total_invited = len(df['participant_id'].unique())
completed = len(df[df['status'] == 'completed'])
completion_rate = (completed / total_invited) * 100

print(f"Completion Rate: {completion_rate:.2f}%")
```

#### Drop-off Points
```python
# Identify where participants stop
drop_off = df.groupby('activity')['participant_id'].count()
drop_off.plot(kind='bar')
plt.title('Participant Drop-off by Activity')
plt.show()
```

#### Time to Complete
```python
# Calculate time spent
df['duration'] = pd.to_datetime(df['end_time']) - pd.to_datetime(df['start_time'])
avg_duration = df['duration'].mean()

print(f"Average completion time: {avg_duration}")
```

### 2. Data Quality Metrics

#### Missing Data
```python
# Identify missing responses
missing_by_item = df.isnull().sum()
missing_by_item.plot(kind='bar')
plt.title('Missing Responses by Item')
plt.show()
```

#### Response Distribution
```python
# Check for abnormal patterns
response_counts = df['response_value'].value_counts()
print(response_counts)
```

#### Validation Errors
```python
# Track failed validations
validation_errors = df[df['validation_error'] == True]
error_rate = len(validation_errors) / len(df) * 100

print(f"Validation error rate: {error_rate:.2f}%")
```

### 3. System Performance Metrics

#### Response Time
```bash
# Monitor API response times
awk '{print $NF}' /var/log/nginx/access.log | sort -n | tail -10
```

#### Error Rates
```bash
# Count errors in logs
grep "ERROR" /var/log/application.log | wc -l
```

#### Storage Usage
```bash
# Check database size
du -sh /var/lib/postgresql/data/

# Check file storage
du -sh /path/to/uploads/
```

## Monitoring Tools

### 1. Built-in Dashboard

#### Reproschema-server Admin Panel
```bash
# Access admin interface
https://your-server.com/admin
```

Features:
- Real-time participant counts
- Response statistics
- System health indicators

### 2. Custom Dashboard

#### Python Dashboard
```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Study Dashboard'),
    dcc.Graph(id='completion-rate'),
    dcc.Graph(id='drop-off-points')
])

@app.callback(
    dash.dependencies.Output('completion-rate', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_completion(n):
    # Fetch latest data
    df = pd.read_json('responses.json')
    completion = len(df[df['status'] == 'completed']) / len(df) * 100

    fig = px.pie(values=[completion, 100-completion],
                  names=['Completed', 'In Progress'])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```

### 3. Grafana Dashboard

#### Setup
```bash
# Install Grafana
docker run -d -p 3000:3000 grafana/grafana

# Configure data source (PostgreSQL)
# Add dashboard panels for metrics
```

#### Panels to Include
- Total responses over time
- Completion rate
- Error rate
- Response time
- Storage usage

### 4. Monitoring Services

#### Uptime Monitoring
```bash
# Use uptime robot or similar
# Configure to check:
# - Server uptime
# - API endpoints
# - Database connectivity
```

#### Log Aggregation
```bash
# ELK Stack (Elasticsearch, Logstash, Kibana)
# or
# Sentry for error tracking
```

## Alerts

### Email Alerts

#### Setup
```python
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'alerts@your-domain.com'
    msg['To'] = 'admin@your-domain.com'

    with smtplib.SMTP('smtp.your-domain.com') as server:
        server.send_message(msg)
```

#### Alert Conditions
```python
# Check completion rate
if completion_rate < 50:
    send_alert(
        'Low Completion Rate',
        f'Completion rate dropped to {completion_rate:.2f}%'
    )

# Check error rate
if error_rate > 5:
    send_alert(
        'High Error Rate',
        f'Validation error rate is {error_rate:.2f}%'
    )

# Check server status
if not check_server_health():
    send_alert(
        'Server Down',
        'Server is not responding'
    )
```

### Slack/Teams Alerts

```python
import requests

def send_slack_alert(message):
    webhook_url = 'YOUR_SLACK_WEBHOOK'
    payload = {'text': message}
    requests.post(webhook_url, json=payload)

# Use in monitoring script
if error_rate > 5:
    send_slack_alert(f'⚠️ High error rate: {error_rate:.2f}%')
```

## Automated Monitoring

### Cron Jobs

```bash
# crontab -e

# Check every hour
0 * * * * /path/to/monitor.py --check-completion
30 * * * * /path/to/monitor.py --check-errors

# Daily summary
0 8 * * * /path/to/monitor.py --daily-report
```

### Monitoring Script

```python
#!/usr/bin/env python3
# monitor.py - Automated monitoring script

import pandas as pd
import smtplib
from datetime import datetime

def check_completion_rate():
    df = pd.read_json('responses.json')
    completed = len(df[df['status'] == 'completed'])
    total = len(df['participant_id'].unique())
    rate = (completed / total) * 100

    if rate < 50:
        send_alert('Low Completion Rate', f'Rate: {rate:.2f}%')

def check_errors():
    df = pd.read_json('responses.json')
    errors = len(df[df['validation_error'] == True])
    total = len(df)
    rate = (errors / total) * 100

    if rate > 5:
        send_alert('High Error Rate', f'Rate: {rate:.2f}%')

def daily_report():
    df = pd.read_json('responses.json')
    report = f"""
    Daily Report - {datetime.now().date()}
    Total Participants: {len(df['participant_id'].unique())}
    Completed: {len(df[df['status'] == 'completed'])}
    In Progress: {len(df[df['status'] == 'in_progress'])}
    Completion Rate: {(len(df[df['status'] == 'completed']) / len(df['participant_id'].unique())) * 100:.2f}%
    """
    send_alert('Daily Report', report)

if __name__ == '__main__':
    import sys
    command = sys.argv[1]

    if command == '--check-completion':
        check_completion_rate()
    elif command == '--check-errors':
        check_errors()
    elif command == '--daily-report':
        daily_report()
```

## Performance Optimization

### Database Optimization

```sql
-- Index frequently queried fields
CREATE INDEX idx_participant_id ON responses(participant_id);
CREATE INDEX idx_status ON responses(status);
CREATE INDEX idx_timestamp ON responses(timestamp);
```

### Caching

```python
# Cache dashboard data
from functools import lru_cache

@lru_cache(maxsize=128)
def get_completion_rate():
    df = pd.read_json('responses.json')
    completed = len(df[df['status'] == 'completed'])
    total = len(df['participant_id'].unique())
    return (completed / total) * 100
```

## Troubleshooting

### No Responses
- Check data endpoint configuration
- Verify CORS settings
- Review browser console for errors

### High Error Rate
- Check validation rules
- Review error logs
- Test with sample data

### Slow Performance
- Add database indexes
- Optimize queries
- Consider pagination
- Scale server resources

## Best Practices

1. **Monitor continuously**: Set up real-time monitoring
2. **Alert appropriately**: Don't spam with alerts
3. **Review regularly**: Check metrics weekly
4. **Document trends**: Keep historical data
5. **Act on insights**: Use data to improve protocol

## Next Steps

- [Set up automated backups](backup-strategies.md)
- [Review performance data](analyzing-data.md)
