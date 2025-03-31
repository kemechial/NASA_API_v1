# Create the service account
resource "google_service_account" "gke_sa" {
  account_id   = "gke-service-account-3562"
  display_name = "GKE Service Account"
}

# Grant GKE Admin role (Allows creating and managing clusters)
resource "google_project_iam_member" "gke_sa_admin" {
  project = "api-project-269968866265"
  role    = "roles/container.admin"
  member  = "serviceAccount:${google_service_account.gke_sa.email}"
}

# Grant Compute Admin role (Allows managing infrastructure for GKE clusters)
resource "google_project_iam_member" "gke_sa_compute_admin" {
  project = "api-project-269968866265"
  role    = "roles/compute.admin"
  member  = "serviceAccount:${google_service_account.gke_sa.email}"
}

# Grant IAM Service Account User role (Allows assuming the service account)
resource "google_project_iam_member" "gke_sa_iam_user" {
  project = "api-project-269968866265"
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.gke_sa.email}"
}

# Grant Workload Identity User role (Required if using GKE Workload Identity)
resource "google_project_iam_member" "gke_sa_wi" {
  project = "api-project-269968866265"
  role    = "roles/iam.workloadIdentityUser"
  member  = "serviceAccount:${google_service_account.gke_sa.email}"
}

# Grant Container Developer role (Allows deploying services inside GKE)
resource "google_project_iam_member" "gke_sa_k8s_dev" {
  project = "api-project-269968866265"
  role    = "roles/container.developer"
  member  = "serviceAccount:${google_service_account.gke_sa.email}"
}
