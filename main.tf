terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# SNS Topic for alerts
resource "aws_sns_topic" "alerts" {
  name = "cloudwatch-alerts"
}

# SNS Topic Subscription
resource "aws_sns_topic_subscription" "email_alerts" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = var.alert_email
}

# CloudWatch Dashboard
resource "aws_cloudwatch_dashboard" "main" {
  dashboard_name = "ApplicationMonitoring"

  dashboard_body = jsonencode({
    widgets = [
      {
        type   = "metric"
        x      = 0
        y      = 0
        width  = 12
        height = 6

        properties = {
          metrics = [
            ["AWS/EC2", "CPUUtilization"],
            ["AWS/ApplicationELB", "RequestCount"],
            ["AWS/ApplicationELB", "TargetResponseTime"],
            ["AWS/RDS", "CPUUtilization"],
            ["AWS/RDS", "DatabaseConnections"]
          ]
          view    = "timeSeries"
          stacked = false
          region  = var.aws_region
          title   = "Application Performance Metrics"
          period  = 300
        }
      },
      {
        type   = "metric"
        x      = 0
        y      = 6
        width  = 6
        height = 6

        properties = {
          metrics = [
            ["AWS/EC2", "CPUUtilization"],
            [".", "NetworkIn"],
            [".", "NetworkOut"]
          ]
          view   = "timeSeries"
          region = var.aws_region
          title  = "EC2 Instance Metrics"
          period = 300
        }
      },
      {
        type   = "metric"
        x      = 6
        y      = 6
        width  = 6
        height = 6

        properties = {
          metrics = [
            ["AWS/ApplicationELB", "HTTPCode_Target_2XX_Count"],
            [".", "HTTPCode_Target_4XX_Count"],
            [".", "HTTPCode_Target_5XX_Count"]
          ]
          view   = "timeSeries"
          region = var.aws_region
          title  = "Load Balancer Response Codes"
          period = 300
        }
      }
    ]
  })
}

# CloudWatch Alarms
resource "aws_cloudwatch_metric_alarm" "high_cpu" {
  alarm_name          = "high-cpu-utilization"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "300"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "This metric monitors ec2 cpu utilization"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    InstanceId = var.instance_id
  }
}

resource "aws_cloudwatch_metric_alarm" "high_response_time" {
  alarm_name          = "high-response-time"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "TargetResponseTime"
  namespace           = "AWS/ApplicationELB"
  period              = "300"
  statistic           = "Average"
  threshold           = "2"
  alarm_description   = "This metric monitors application response time"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    LoadBalancer = var.load_balancer_name
  }
}

resource "aws_cloudwatch_metric_alarm" "error_rate" {
  alarm_name          = "high-error-rate"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "HTTPCode_Target_5XX_Count"
  namespace           = "AWS/ApplicationELB"
  period              = "300"
  statistic           = "Sum"
  threshold           = "10"
  alarm_description   = "This metric monitors 5xx error rate"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    LoadBalancer = var.load_balancer_name
  }
}

# Custom CloudWatch Log Group
resource "aws_cloudwatch_log_group" "app_logs" {
  name              = "/aws/application/logs"
  retention_in_days = 14
}

# CloudWatch Log Metric Filter
resource "aws_cloudwatch_log_metric_filter" "error_count" {
  name           = "ErrorCount"
  log_group_name = aws_cloudwatch_log_group.app_logs.name
  pattern        = "ERROR"

  metric_transformation {
    name      = "ErrorCount"
    namespace = "Application/Logs"
    value     = "1"
  }
}

# Alarm for log errors
resource "aws_cloudwatch_metric_alarm" "log_errors" {
  alarm_name          = "application-log-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "1"
  metric_name         = "ErrorCount"
  namespace           = "Application/Logs"
  period              = "300"
  statistic           = "Sum"
  threshold           = "5"
  alarm_description   = "This metric monitors application log errors"
  alarm_actions       = [aws_sns_topic.alerts.arn]
  treat_missing_data  = "notBreaching"
}