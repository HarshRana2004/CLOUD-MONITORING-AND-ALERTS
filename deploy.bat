@echo off
echo Setting up AWS CloudWatch Monitoring...

REM Check if Terraform is installed
terraform version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Terraform is not installed. Please install Terraform first.
    exit /b 1
)

REM Check if AWS CLI is configured
aws sts get-caller-identity >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: AWS CLI is not configured. Please run 'aws configure' first.
    exit /b 1
)

REM Initialize Terraform
echo Initializing Terraform...
terraform init

REM Validate Terraform configuration
echo Validating Terraform configuration...
terraform validate

REM Plan the deployment
echo Planning Terraform deployment...
terraform plan

REM Ask for confirmation
set /p confirm="Do you want to apply these changes? (y/N): "
if /i "%confirm%"=="y" (
    echo Applying Terraform configuration...
    terraform apply -auto-approve
    
    echo.
    echo ✅ CloudWatch monitoring setup complete!
    echo.
    echo 📊 Dashboard URL:
    terraform output dashboard_url
    echo.
    echo 📧 SNS Topic ARN:
    terraform output sns_topic_arn
    echo.
    echo 📝 Log Group:
    terraform output log_group_name
    echo.
    echo 🚨 Alarms Created:
    terraform output alarms_created
    echo.
    echo To test the monitoring:
    echo 1. Install Python dependencies: pip install -r requirements.txt
    echo 2. Run the sample application: python sample_app.py
    echo 3. Check the CloudWatch dashboard for metrics
) else (
    echo Deployment cancelled.
)

pause