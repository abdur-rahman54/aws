#!/bin/bash

# Variables
KEY_NAME="your-key-name"
SECURITY_GROUP_ID="sg-xxxxxxxx"
SUBNET_ID="subnet-xxxxxxxx"
DB_USERNAME="yourusername"
DB_PASSWORD="yourpassword"
DB_NAME="wordpressdb"
INSTANCE_TYPE="t2.micro"
AMI_ID="ami-xxxxxxxx"

# Launch EC2 instance
INSTANCE_ID=$(aws ec2 run-instances \
    --image-id $AMI_ID \
    --count 1 \
    --instance-type $INSTANCE_TYPE \
    --key-name $KEY_NAME \
    --security-group-ids $SECURITY_GROUP_ID \
    --subnet-id $SUBNET_ID \
    --query 'Instances[0].InstanceId' \
    --output text)

# Tag the instance (optional)
aws ec2 create-tags --resources $INSTANCE_ID --tags Key=Name,Value=WordPressServer

# Get the public IP of the instance
PUBLIC_IP=$(aws ec2 describe-instances \
    --instance-ids $INSTANCE_ID \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text)

# Wait until the instance is running
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# Create RDS instance
aws rds create-db-instance \
    --db-instance-identifier $DB_NAME \
    --db-instance-class db.t2.micro \
    --engine mysql \
    --allocated-storage 20 \
    --master-username $DB_USERNAME \
    --master-user-password $DB_PASSWORD \
    --backup-retention-period 3

# Wait for the RDS instance to be available
aws rds wait db-instance-available --db-instance-identifier $DB_NAME

# Get the RDS endpoint
RDS_ENDPOINT=$(aws rds describe-db-instances \
    --db-instance-identifier $DB_NAME \
    --query 'DBInstances[0].Endpoint.Address' \
    --output text)

# Connect to EC2 instance and install software
ssh -o StrictHostKeyChecking=no -i "$KEY_NAME.pem" ubuntu@$PUBLIC_IP << EOF
    sudo apt update
    sudo apt install -y apache2 php php-mysql libapache2-mod-php mysql-client
    sudo systemctl start apache2
    sudo systemctl enable apache2

    cd /var/www/html
    sudo wget https://wordpress.org/latest.tar.gz
    sudo tar -xvzf latest.tar.gz
    sudo mv wordpress/* .
    sudo rm -rf wordpress latest.tar.gz

    sudo cp wp-config-sample.php wp-config.php
    sudo sed -i "s/database_name_here/$DB_NAME/" wp-config.php
    sudo sed -i "s/username_here/$DB_USERNAME/" wp-config.php
    sudo sed -i "s/password_here/$DB_PASSWORD/" wp-config.php
    sudo sed -i "s/localhost/$RDS_ENDPOINT/" wp-config.php

    sudo chown -R www-data:www-data /var/www/html
    sudo chmod -R 755 /var/www/html
EOF

# Output the public IP
echo "WordPress is set up at http://$PUBLIC_IP"
