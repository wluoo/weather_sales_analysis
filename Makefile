# Setup virtual environment
setup:
	python -m venv venv
	. venv/bin/activate && \
	python -m pip install -r requirements.txt

# Run script to extract historical weather data for each sales date
extract-weather-data:
	python scripts/extract_historical_weather_data.py

# Run script to get current weather data and add to BigQuery
update-weather:
	python scripts/update_weather.py

# Variables
PROJECT_ID = deft-approach-459711-g2
REGION = australia-southeast1
REPOSITORY = weather-updates
VERSION = v1.0.2
IMAGE = $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(REPOSITORY)/weather-update:$(VERSION)
SA_NAME = weather-update-sa
SA_EMAIL = $(SA_NAME)@$(PROJECT_ID).iam.gserviceaccount.com

# Build the Docker image
build:
	docker buildx build \
		--platform linux/amd64 \
		--progress=plain \
		--no-cache \
		--pull \
		--file Dockerfile \
		--tag=$(IMAGE) .

# Push the Docker image to Artifact Registry
push:
	docker push $(IMAGE)

# Build and push
build-and-push: build push

.PHONY: build push all

# Create and configure service account
create-sa:
	gcloud iam service-accounts create $(SA_NAME) \
		--display-name="Weather Update Service Account" \
		--description="Service account for weather update Cloud Run job"
	gcloud projects add-iam-policy-binding $(PROJECT_ID) \
		--member="serviceAccount:$(SA_EMAIL)" \
		--role="roles/run.invoker"
	gcloud projects add-iam-policy-binding $(PROJECT_ID) \
		--member="serviceAccount:$(SA_EMAIL)" \
		--role="roles/secretmanager.secretAccessor"
	gcloud projects add-iam-policy-binding $(PROJECT_ID) \
		--member="serviceAccount:$(SA_EMAIL)" \
		--role="roles/bigquery.dataEditor"

# Create cloud run job
create-job:
	gcloud run jobs create daily-weather-update \
		--image $(IMAGE) \
		--region="australia-southeast1" \
		--service-account="$(SA_EMAIL)"

# Execute cloud run job
execute-job:
	gcloud run jobs execute daily-weather-update

# Create cloud scheduler job
create-scheduler:
	gcloud scheduler jobs create http daily-weather-update-trigger \
		--schedule="0 6 * * *" \
		--time-zone="Australia/Melbourne" \
		--uri="https://$(REGION)-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/$(PROJECT_ID)/jobs/daily-weather-update:run" \
		--http-method=POST \
		--oauth-service-account-email="$(SA_EMAIL)" \
		--oauth-token-scope="https://www.googleapis.com/auth/cloud-platform" \
		--location="australia-southeast1"

.PHONY: build push all create-job execute-job create-scheduler create-sa

