variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "alert_email" {
  description = "Email address for CloudWatch alerts"
  type        = string
  default     = "admin@example.com"
}

variable "instance_id" {
  description = "EC2 instance ID to monitor"
  type        = string
  default     = "i-1234567890abcdef0"
}

variable "load_balancer_name" {
  description = "Application Load Balancer name"
  type        = string
  default     = "app/my-load-balancer/50dc6c495c0c9188"
}