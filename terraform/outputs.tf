output "ec2_ip" {
  value = aws_instance.hospital_ec2.public_ip
}
