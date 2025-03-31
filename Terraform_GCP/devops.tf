resource "null_resource" "copy_files" {
  for_each = fileset("./yaml_files/", "*")

  provisioner "file" {
    source      = "./yaml_files/${each.value}"
    destination = "/path/to/destination/${each.value}"

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/key.pem")
      host        = aws_instance.example.public_ip
    }
  }
}