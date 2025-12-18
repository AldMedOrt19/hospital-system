provider "aws" {
  region = "us-east-1"
}

######################################
# Security Group
######################################

resource "aws_security_group" "hospital_sg" {
  name        = "hospital-sg"
  description = "Security group for Hospital System"

  # SSH
  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Frontend
  ingress {
    description = "Frontend Web"
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Backend APIs
  ingress {
    description = "Backend APIs"
    from_port   = 8000
    to_port     = 8004
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Salida total
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "hospital-sg"
  }
}

######################################
# EC2 Instance
######################################

resource "aws_instance" "hospital_ec2" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.hospital_sg.id]

  key_name = "hospital-key" # 🔑 Debe existir en AWS

  tags = {
    Name = "Hospital-System"
  }

  user_data = <<-EOF
    #!/bin/bash
    yum update -y

    # Instalar Docker
    amazon-linux-extras install docker -y
    systemctl start docker
    systemctl enable docker
    usermod -aG docker ec2-user

    # Instalar Docker Compose
    curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
      -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

    # Crear carpeta del proyecto
    mkdir -p /home/ec2-user/hospital-system
    chown ec2-user:ec2-user /home/ec2-user/hospital-system
  EOF
}
