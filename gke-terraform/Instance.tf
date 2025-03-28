resource "google_compute_instance" "control_vm" {
  name         = "control-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-b"

  boot_disk {
    initialize_params {
      image = "ubuntu-2204-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
    }
  }

  # Metadata for SSH key
  metadata = {
    ssh-keys = "your-username:${file("~/.ssh/id_rsa.pub")}"
  }

  # Service account configuration
  service_account {
    scopes = ["cloud-platform"]
  }

  # Provisioner to run the script remotely
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/scripts/create_gke_cluster.sh",
      "/tmp/scripts/create_gke_cluster.sh"
    ]

    connection {
      type        = "ssh"
      user        = "your-username"
      private_key = file("~/.ssh/id_rsa")
      host        = self.network_interface.0.access_config.0.nat_ip
    }
  }
}