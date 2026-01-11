output "sns_topic_arn" {
  description = "ARN of the SNS topic for alerts"
  value       = aws_sns_topic.alerts.arn
}

output "dashboard_url" {
  description = "URL to access the CloudWatch dashboard"
  value       = "https://${var.aws_region}.console.aws.amazon.com/cloudwatch/home?region=${var.aws_region}#dashboards:name=${aws_cloudwatch_dashboard.main.dashboard_name}"
}

output "log_group_name" {
  description = "CloudWatch log group name"
  value       = aws_cloudwatch_log_group.app_logs.name
}

output "alarms_created" {
  description = "List of CloudWatch alarms created"
  value = [
    aws_cloudwatch_metric_alarm.high_cpu.alarm_name,
    aws_cloudwatch_metric_alarm.high_response_time.alarm_name,
    aws_cloudwatch_metric_alarm.error_rate.alarm_name,
    aws_cloudwatch_metric_alarm.log_errors.alarm_name
  ]
}