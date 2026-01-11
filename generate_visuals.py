import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_monitoring_architecture():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Colors
    aws_orange = '#FF9900'
    aws_blue = '#232F3E'
    light_blue = '#E8F4FD'
    green = '#4CAF50'
    red = '#F44336'
    
    # Title
    ax.text(0.5, 0.95, 'AWS CloudWatch Monitoring Architecture', 
            ha='center', va='center', fontsize=16, fontweight='bold',
            transform=ax.transAxes)
    
    # CloudWatch Dashboard
    dashboard = FancyBboxPatch((0.1, 0.7), 0.35, 0.2, 
                              boxstyle="round,pad=0.02", 
                              facecolor=light_blue, edgecolor=aws_blue, linewidth=2)
    ax.add_patch(dashboard)
    ax.text(0.275, 0.8, 'CloudWatch Dashboard\n"ApplicationMonitoring"', 
            ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Metrics widgets
    widgets = ['CPU Utilization', 'Response Time', 'Error Rates', 'Network I/O']
    for i, widget in enumerate(widgets):
        x = 0.12 + (i % 2) * 0.15
        y = 0.72 + (i // 2) * 0.06
        widget_box = patches.Rectangle((x, y), 0.12, 0.04, 
                                     facecolor='white', edgecolor=aws_blue)
        ax.add_patch(widget_box)
        ax.text(x + 0.06, y + 0.02, widget, ha='center', va='center', fontsize=8)
    
    # CloudWatch Alarms
    alarms_box = FancyBboxPatch((0.55, 0.7), 0.35, 0.2, 
                               boxstyle="round,pad=0.02", 
                               facecolor='#FFE6E6', edgecolor=red, linewidth=2)
    ax.add_patch(alarms_box)
    ax.text(0.725, 0.85, 'CloudWatch Alarms', 
            ha='center', va='center', fontsize=12, fontweight='bold')
    
    alarms = ['High CPU (>80%)', 'Response Time (>2s)', 'Error Rate (>10)', 'Log Errors (>5)']
    for i, alarm in enumerate(alarms):
        y = 0.82 - i * 0.025
        ax.text(0.57, y, f'• {alarm}', ha='left', va='center', fontsize=9)
    
    # SNS Topic
    sns_box = FancyBboxPatch((0.3, 0.45), 0.4, 0.15, 
                            boxstyle="round,pad=0.02", 
                            facecolor='#E8F5E8', edgecolor=green, linewidth=2)
    ax.add_patch(sns_box)
    ax.text(0.5, 0.55, 'SNS Topic\n"cloudwatch-alerts"', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(0.5, 0.48, 'Email Notifications', 
            ha='center', va='center', fontsize=9, style='italic')
    
    # Log Groups
    log_box = FancyBboxPatch((0.05, 0.25), 0.4, 0.15, 
                            boxstyle="round,pad=0.02", 
                            facecolor='#FFF8E1', edgecolor=aws_orange, linewidth=2)
    ax.add_patch(log_box)
    ax.text(0.25, 0.35, 'CloudWatch Log Groups', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(0.25, 0.3, '/aws/application/logs', 
            ha='center', va='center', fontsize=9, family='monospace')
    ax.text(0.25, 0.27, 'Retention: 14 days', 
            ha='center', va='center', fontsize=8, style='italic')
    
    # Sample Application
    app_box = FancyBboxPatch((0.55, 0.25), 0.35, 0.15, 
                            boxstyle="round,pad=0.02", 
                            facecolor=light_blue, edgecolor=aws_blue, linewidth=2)
    ax.add_patch(app_box)
    ax.text(0.725, 0.35, 'Sample Application', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    ax.text(0.725, 0.3, 'sample_app.py', 
            ha='center', va='center', fontsize=9, family='monospace')
    ax.text(0.725, 0.27, 'Generates metrics & logs', 
            ha='center', va='center', fontsize=8, style='italic')
    
    # Arrows
    # Dashboard to Alarms
    ax.annotate('', xy=(0.55, 0.8), xytext=(0.45, 0.8),
                arrowprops=dict(arrowstyle='->', lw=2, color=aws_blue))
    
    # Alarms to SNS
    ax.annotate('', xy=(0.5, 0.6), xytext=(0.725, 0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color=red))
    
    # App to Logs
    ax.annotate('', xy=(0.45, 0.32), xytext=(0.55, 0.32),
                arrowprops=dict(arrowstyle='->', lw=2, color=aws_orange))
    
    # Logs to Dashboard
    ax.annotate('', xy=(0.25, 0.7), xytext=(0.25, 0.4),
                arrowprops=dict(arrowstyle='->', lw=2, color=aws_orange))
    
    # Terraform deployment info
    terraform_box = FancyBboxPatch((0.1, 0.05), 0.8, 0.1, 
                                  boxstyle="round,pad=0.02", 
                                  facecolor='#F5F5F5', edgecolor='gray', linewidth=1)
    ax.add_patch(terraform_box)
    ax.text(0.5, 0.1, 'Deployed via Terraform Infrastructure as Code', 
            ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(0.5, 0.07, 'Run: deploy.bat (Windows) or ./deploy.sh (Linux/macOS)', 
            ha='center', va='center', fontsize=10, family='monospace')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('monitoring_architecture.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_dashboard_mockup():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('CloudWatch Dashboard - ApplicationMonitoring', fontsize=16, fontweight='bold')
    
    # CPU Utilization
    time = np.linspace(0, 24, 100)
    cpu_data = 30 + 20 * np.sin(time/4) + 10 * np.random.random(100)
    ax1.plot(time, cpu_data, color='#FF9900', linewidth=2)
    ax1.set_title('EC2 CPU Utilization (%)', fontweight='bold')
    ax1.set_ylabel('CPU %')
    ax1.set_xlabel('Time (hours)')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=80, color='red', linestyle='--', label='Alert Threshold')
    ax1.legend()
    
    # Response Time
    response_time = 0.5 + 0.3 * np.sin(time/3) + 0.2 * np.random.random(100)
    ax2.plot(time, response_time, color='#4CAF50', linewidth=2)
    ax2.set_title('Application Response Time (seconds)', fontweight='bold')
    ax2.set_ylabel('Response Time (s)')
    ax2.set_xlabel('Time (hours)')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=2, color='red', linestyle='--', label='Alert Threshold')
    ax2.legend()
    
    # Error Rates
    error_2xx = 85 + 10 * np.random.random(100)
    error_4xx = 10 + 5 * np.random.random(100)
    error_5xx = 2 + 3 * np.random.random(100)
    
    ax3.bar(range(len(error_2xx)), error_2xx, color='green', alpha=0.7, label='2xx Success')
    ax3.bar(range(len(error_4xx)), error_4xx, bottom=error_2xx, color='orange', alpha=0.7, label='4xx Client Error')
    ax3.bar(range(len(error_5xx)), error_5xx, bottom=error_2xx+error_4xx, color='red', alpha=0.7, label='5xx Server Error')
    ax3.set_title('HTTP Response Codes Distribution', fontweight='bold')
    ax3.set_ylabel('Request Count')
    ax3.set_xlabel('Time Intervals')
    ax3.legend()
    
    # Network I/O
    network_in = 50 + 30 * np.sin(time/2) + 20 * np.random.random(100)
    network_out = 40 + 25 * np.sin(time/2.5) + 15 * np.random.random(100)
    ax4.plot(time, network_in, color='blue', linewidth=2, label='Network In')
    ax4.plot(time, network_out, color='purple', linewidth=2, label='Network Out')
    ax4.set_title('Network Traffic (MB/s)', fontweight='bold')
    ax4.set_ylabel('Traffic (MB/s)')
    ax4.set_xlabel('Time (hours)')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig('dashboard_mockup.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_alert_flow():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Title
    ax.text(0.5, 0.95, 'CloudWatch Alert Flow', 
            ha='center', va='center', fontsize=16, fontweight='bold',
            transform=ax.transAxes)
    
    # Steps
    steps = [
        ('Metric Threshold\nBreached', 0.15, 0.8, '#FFE6E6'),
        ('CloudWatch Alarm\nTriggered', 0.15, 0.6, '#FF9900'),
        ('SNS Topic\nNotified', 0.15, 0.4, '#4CAF50'),
        ('Email Alert\nSent', 0.15, 0.2, '#2196F3')
    ]
    
    for i, (text, x, y, color) in enumerate(steps):
        # Step box
        step_box = FancyBboxPatch((x-0.08, y-0.08), 0.16, 0.16, 
                                 boxstyle="round,pad=0.02", 
                                 facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(step_box)
        ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold')
        
        # Step number
        circle = plt.Circle((x-0.12, y), 0.03, color='white', ec='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x-0.12, y, str(i+1), ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Arrow to next step
        if i < len(steps) - 1:
            ax.annotate('', xy=(x, y-0.12), xytext=(x, y-0.08),
                       arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    
    # Alert examples
    examples_box = FancyBboxPatch((0.4, 0.15), 0.55, 0.7, 
                                 boxstyle="round,pad=0.02", 
                                 facecolor='#F5F5F5', edgecolor='gray', linewidth=2)
    ax.add_patch(examples_box)
    
    ax.text(0.675, 0.8, 'Alert Examples', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    
    alerts = [
        'HIGH CPU: EC2 instance CPU > 80% for 10 minutes',
        'SLOW RESPONSE: App response time > 2 seconds',
        'ERROR SPIKE: >10 5xx errors in 5 minutes',
        'LOG ERRORS: >5 ERROR entries in application logs'
    ]
    
    for i, alert in enumerate(alerts):
        ax.text(0.42, 0.7 - i*0.1, alert, ha='left', va='center', fontsize=10)
    
    # Email notification mockup
    email_box = FancyBboxPatch((0.42, 0.2), 0.5, 0.15, 
                              boxstyle="round,pad=0.02", 
                              facecolor='white', edgecolor='blue', linewidth=2)
    ax.add_patch(email_box)
    
    ax.text(0.67, 0.32, 'Email Notification', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='blue')
    ax.text(0.44, 0.28, 'From: AWS CloudWatch <no-reply@sns.amazonaws.com>', 
            ha='left', va='center', fontsize=8, family='monospace')
    ax.text(0.44, 0.25, 'Subject: ALARM: "high-cpu-utilization"', 
            ha='left', va='center', fontsize=8, family='monospace')
    ax.text(0.44, 0.22, 'Alert triggered at 2024-01-15 14:30:00 UTC', 
            ha='left', va='center', fontsize=8, family='monospace')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('alert_flow.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("Generating monitoring architecture diagram...")
    create_monitoring_architecture()
    
    print("Generating dashboard mockup...")
    create_dashboard_mockup()
    
    print("Generating alert flow diagram...")
    create_alert_flow()
    
    print("All diagrams generated successfully!")
    print("Files created:")
    print("   - monitoring_architecture.png")
    print("   - dashboard_mockup.png") 
    print("   - alert_flow.png")