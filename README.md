# Cloud Monitoring and Alerts

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: HARSH RANA

*INTERN ID*: CTIS1777

*DOMAIN*: CLOUD COMPUTING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

##TASK DESCRIPTION

This project sets up comprehensive monitoring for cloud-based applications using AWS CloudWatch, including configured alerts and a dashboard showcasing key metrics.

## 🏗️ Architecture

- **CloudWatch Dashboard**: Visual metrics display for application performance
- **CloudWatch Alarms**: Automated alerts for critical thresholds
- **SNS Topics**: Email notifications for alerts
- **Log Groups**: Centralized application logging
- **Custom Metrics**: Application-specific monitoring

## 📋 Prerequisites

1. **AWS CLI** configured with appropriate credentials
2. **Terraform** installed (v1.0+)
3. **Python 3.7+** (for sample application)
4. Valid AWS account with CloudWatch permissions

## 🚀 Quick Setup

### Windows
```cmd
deploy.bat
```

### Linux/macOS
```bash
chmod +x deploy.sh
./deploy.sh
```

### Manual Setup
```bash
# Initialize Terraform
terraform init

# Review planned changes
terraform plan

# Apply configuration
terraform apply
```

## 📊 Monitoring Components

### Dashboard Metrics
- **EC2 CPU Utilization**: Server performance monitoring
- **Load Balancer Metrics**: Request count and response times
- **HTTP Response Codes**: Error rate tracking
- **Network Traffic**: Inbound/outbound data flow
- **Database Connections**: RDS monitoring

### Configured Alarms
1. **High CPU Utilization** (>80% for 10 minutes)
2. **High Response Time** (>2 seconds for 10 minutes)
3. **Error Rate** (>10 5xx errors in 5 minutes)
4. **Application Log Errors** (>5 ERROR logs in 5 minutes)

<img width="1917" height="927" alt="Image" src="https://github.com/user-attachments/assets/a4f9fa4f-6eb0-472c-ad9e-908f60d7fd4d" />
<br>
<img width="1916" height="940" alt="Image" src="https://github.com/user-attachments/assets/befe265f-e1b6-4998-b6f4-0f56abf1eb3c" />
<br>
<img width="1914" height="933" alt="Image" src="https://github.com/user-attachments/assets/d85a122d-9a85-4955-90be-b94697e23edb" />

### Alert Notifications
- Email notifications via SNS
- Configurable recipient addresses
- Immediate alert delivery

## 🧪 Testing the Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run sample application**:
   ```bash
   python sample_app.py
   ```

3. **View metrics**:
   - Access CloudWatch dashboard via AWS Console
   - Monitor real-time metrics and logs
   - Test alert triggers

## ⚙️ Configuration

### Variables (variables.tf)
- `aws_region`: AWS region for resources
- `alert_email`: Email for notifications
- `instance_id`: EC2 instance to monitor
- `load_balancer_name`: ALB identifier

### Customization
```hcl
# Example: Update alert thresholds
resource "aws_cloudwatch_metric_alarm" "high_cpu" {
  threshold = "90"  # Change from 80% to 90%
}
```

## 📈 Metrics Collected

### AWS Native Metrics
- EC2: CPU, Network, Disk I/O
- ALB: Request count, response times, error rates
- RDS: CPU, connections, read/write IOPS

### Custom Application Metrics
- Processing time per request
- Request success/failure rates
- Memory utilization
- Custom business metrics

## 🔧 Maintenance

### View Resources
```bash
terraform show
```

### Update Configuration
```bash
terraform plan
terraform apply
```

### Cleanup
```bash
terraform destroy
```

## 📝 Log Analysis

Logs are centralized in CloudWatch Log Groups:
- **Log Group**: `/aws/application/logs`
- **Retention**: 14 days
- **Metric Filters**: Automatic error detection

## 🚨 Alert Management

### SNS Topic Configuration
- Topic: `cloudwatch-alerts`
- Protocol: Email
- Endpoint: Configurable email address

### Alarm States
- **OK**: Metric within normal range
- **ALARM**: Threshold breached
- **INSUFFICIENT_DATA**: Not enough data points

## 🔒 Security Considerations

- IAM roles with minimal required permissions
- Encrypted SNS topics
- VPC endpoint support for private subnets
- Log data retention policies

## 📊 Cost Optimization

- 14-day log retention to control costs
- Efficient metric collection intervals
- Consolidated dashboard views
- Targeted alarm configurations

## 🛠️ Troubleshooting

### Common Issues
1. **AWS credentials not configured**
   ```bash
   aws configure
   ```

2. **Terraform state conflicts**
   ```bash
   terraform refresh
   ```

3. **SNS subscription not confirmed**
   - Check email for confirmation link
   - Verify email address in variables

### Monitoring Health
- Check alarm states in CloudWatch console
- Verify SNS topic subscriptions
- Test log delivery with sample application

## 📚 Additional Resources

- [AWS CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [CloudWatch Best Practices](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html)
