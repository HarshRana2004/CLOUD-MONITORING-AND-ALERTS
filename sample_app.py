import boto3
import json
import time
import random
from datetime import datetime

class CloudWatchLogger:
    def __init__(self, log_group_name, log_stream_name, region='us-east-1'):
        self.client = boto3.client('logs', region_name=region)
        self.log_group_name = log_group_name
        self.log_stream_name = log_stream_name
        self.sequence_token = None
        
        # Create log stream if it doesn't exist
        try:
            self.client.create_log_stream(
                logGroupName=log_group_name,
                logStreamName=log_stream_name
            )
        except self.client.exceptions.ResourceAlreadyExistsException:
            pass
    
    def log(self, level, message):
        timestamp = int(time.time() * 1000)
        log_event = {
            'timestamp': timestamp,
            'message': f"[{level}] {datetime.now().isoformat()} - {message}"
        }
        
        try:
            if self.sequence_token:
                response = self.client.put_log_events(
                    logGroupName=self.log_group_name,
                    logStreamName=self.log_stream_name,
                    logEvents=[log_event],
                    sequenceToken=self.sequence_token
                )
            else:
                response = self.client.put_log_events(
                    logGroupName=self.log_group_name,
                    logStreamName=self.log_stream_name,
                    logEvents=[log_event]
                )
            
            self.sequence_token = response.get('nextSequenceToken')
        except Exception as e:
            print(f"Failed to send log: {e}")

class SampleApplication:
    def __init__(self):
        self.logger = CloudWatchLogger(
            log_group_name='/aws/application/logs',
            log_stream_name=f'app-instance-{int(time.time())}'
        )
        self.cloudwatch = boto3.client('cloudwatch')
    
    def send_custom_metric(self, metric_name, value, unit='Count'):
        """Send custom metrics to CloudWatch"""
        try:
            self.cloudwatch.put_metric_data(
                Namespace='Application/Custom',
                MetricData=[
                    {
                        'MetricName': metric_name,
                        'Value': value,
                        'Unit': unit,
                        'Timestamp': datetime.utcnow()
                    }
                ]
            )
            self.logger.log('INFO', f'Sent metric {metric_name}: {value}')
        except Exception as e:
            self.logger.log('ERROR', f'Failed to send metric: {e}')
    
    def simulate_workload(self):
        """Simulate application workload with metrics and logs"""
        self.logger.log('INFO', 'Application started')
        
        for i in range(100):
            # Simulate processing time
            processing_time = random.uniform(0.1, 2.0)
            time.sleep(processing_time)
            
            # Send processing time metric
            self.send_custom_metric('ProcessingTime', processing_time * 1000, 'Milliseconds')
            
            # Simulate request count
            request_count = random.randint(1, 10)
            self.send_custom_metric('RequestCount', request_count)
            
            # Simulate occasional errors
            if random.random() < 0.1:  # 10% error rate
                self.logger.log('ERROR', f'Processing failed for request {i}')
                self.send_custom_metric('ErrorCount', 1)
            else:
                self.logger.log('INFO', f'Successfully processed request {i}')
                self.send_custom_metric('SuccessCount', 1)
            
            # Simulate memory usage
            memory_usage = random.uniform(30, 90)
            self.send_custom_metric('MemoryUtilization', memory_usage, 'Percent')
            
            print(f"Processed request {i+1}/100")
        
        self.logger.log('INFO', 'Application completed')

if __name__ == "__main__":
    app = SampleApplication()
    app.simulate_workload()