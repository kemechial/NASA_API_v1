
# Create a Compute Engine instance named control-server
resource "google_compute_instance" "control-server" {
  name         = "control-vm2"   # Replace with your desired instance name
  machine_type = "e2-micro"      # Replace with your desired machine type
  zone         = "us-central1-b" # Replace with your desired zone

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts" # Using Ubuntu 22.04 LTS
    }
  }

  network_interface {
    network = "default" # Use the default network or create a custom one
    # Optional: Assign an external IP address
    access_config {
      # Ephemeral external IP
    }
  }

  service_account {
    email  = google_service_account.gke_sa.email
    scopes = ["cloud-platform"]
  }


  # Optional: Add metadata
  metadata = {
    foo = "bar"
    #startup-script = file("./startup.sh") # Use a local file
    ssh-keys = "kaanevran:${file("~/.ssh/gcp-vm-key.pub")}" # Use an SSH key
  }

  # Optional: Add tags
  tags = ["web", "http-server", "ssh-access"]

  provisioner "file" {
    source      = "startup.sh"
    destination = "/tmp/startup.sh"

    connection {
      type        = "ssh"
      user        = "kaanevran"               # Replace with the username for the VM
      private_key = file("~/.ssh/gcp-vm-key") # Path to your private SSH key
      host        = self.network_interface.0.access_config.0.nat_ip
    }
  }

  for_each = fileset("./yaml_files/", "*")

  provisioner "file" {
    source      = "./yaml_files/${each.value}"
    destination = "/tmp/${each.value}"

     connection {
      type        = "ssh"
      user        = "kaanevran"               # Replace with the username for the VM
      private_key = file("~/.ssh/gcp-vm-key") # Path to your private SSH key
      host        = self.network_interface.0.access_config.0.nat_ip
    }
  }


  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/startup.sh",
      #"sudo /tmp/startup.sh > /tmp/startup.log 2>&1"  # Redirect stderr to stdout
      "echo 'test'"

    ]

    connection {
      type        = "ssh"
      user        = "kaanevran"               # Replace with the username for the VM
      private_key = file("~/.ssh/gcp-vm-key") # Path to your private SSH key
      host        = self.network_interface.0.access_config.0.nat_ip
    }
  }

}


# Optional: Output the instance's external IP address
output "instance_external_ip" {
  value       = google_compute_instance.control-server.network_interface.0.access_config.0.nat_ip
  description = "The external IP address of the instance"
  sensitive   = false
}
