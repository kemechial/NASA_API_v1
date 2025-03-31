resource "google_compute_instance" "control-server" {
  name         = "gke-control"
  machine_type = "e2-micro"
  zone         = "us-central1-b"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  service_account {
    email  = google_service_account.gke_sa.email
    scopes = ["cloud-platform"]
  }

  metadata = {
    foo      = "bar"
    ssh-keys = "kaanevran:${file("~/.ssh/gcp-vm-key.pub")}"
  }

  tags = ["web", "http-server", "ssh-access"]

  provisioner "file" {
    source      = "startup.sh"
    destination = "/tmp/startup.sh"

    connection {
      type        = "ssh"
      user        = "kaanevran"
      private_key = file("~/.ssh/gcp-vm-key")
      host        = self.network_interface.0.access_config.0.nat_ip
    }
  }
}

resource "null_resource" "copy_yaml_files" {
  for_each = fileset("./yaml_files/", "*")

  provisioner "file" {
    source      = "./yaml_files/${each.value}"
    destination = "/tmp/${each.value}"

    connection {
      type        = "ssh"
      user        = "kaanevran"
      private_key = file("~/.ssh/gcp-vm-key")
      host        = google_compute_instance.control-server.network_interface.0.access_config.0.nat_ip
    }
  }

  depends_on = [google_compute_instance.control-server]
}

resource "null_resource" "run_startup_script" {
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/startup.sh",
      "sudo /tmp/startup.sh > /tmp/startup.log 2>&1"
    ]

    connection {
      type        = "ssh"
      user        = "kaanevran"
      private_key = file("~/.ssh/gcp-vm-key")
      host        = google_compute_instance.control-server.network_interface.0.access_config.0.nat_ip
    }
  }

  depends_on = [null_resource.copy_yaml_files]
}

output "instance_external_ip" {
  value       = google_compute_instance.control-server.network_interface.0.access_config.0.nat_ip
  description = "The external IP address of the instance"
  sensitive   = false
}