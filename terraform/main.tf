provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "hospital_ec2" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  tags = {
    Name = "Hospital-System"
  }
}
