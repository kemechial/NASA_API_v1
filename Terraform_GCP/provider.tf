# Configure the region and project
provider "google" {
  project     = "api-project-269968866265" # Replace with your project ID
  region      = "us-central1"              # Replace with your desired region
  credentials = file("terraform-key.json")
}


