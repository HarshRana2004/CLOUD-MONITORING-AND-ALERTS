#!/bin/bash

# Cloud Monitoring Setup Script
echo "Setting up AWS CloudWatch Monitoring..."

# Check if Terraform is installed
if ! command -v terraform &> /dev/null; then
    echo "Error: Terraform is not installed. Please install Terraform first."
    exit 1
fi

# Check if AWS CLI is configured
if ! aws sts get-caller-identity &> /dev/null; then
    echo "Error: AWS CLI is not configured. Please run 'aws configure' first."
    exit 1
fi

# Initialize Terraform
echo "Initializing Terraform..."
terraform init

# Validate Terraform configuration
echo "Validating Terraform configuration..."
terraform validate

# Plan the deployment
echo "Planning Terraform deployment..."
terraform plan

# Ask for confirmation
read -p "Do you want to apply these changes? (y/N): " confirm
if [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]]; then
    echo "Applying Terraform configuration..."
    terraform apply -auto-approve
    
    echo ""
    echo "✅ CloudWatch monitoring setup complete!"
    echo ""
    echo "📊 Dashboard URL:"
    terraform output dashboard_url
    echo ""
    echo "📧 SNS Topic ARN:"
    terraform output sns_topic_arn
    echo ""
    echo "📝 Log Group:"
    terraform output log_group_name
    echo ""
    echo "🚨 Alarms Created:"
    terraform output alarms_created
    echo ""
    echo "To test the monitoring:"
    echo "1. Install Python dependencies: pip install -r requirements.txt"
    echo "2. Run the sample application: python sample_app.py"
    echo "3. Check the CloudWatch dashboard for metrics"
else
    echo "Deployment cancelled."
fi