This project is a web-based Markdown to PDF converter application. It allows users to:

Upload or write Markdown content directly in the browser

Preview the formatted HTML version

Convert the content into a styled PDF using a chosen theme

The application is built using Python and Flask on the backend, and uses marked.js for rendering Markdown in the browser. The PDF generation is handled via WeasyPrint.

To ensure portability, scalability, and automation, the project is containerized with Docker, deployed to Google Kubernetes Engine (GKE), and uses GitHub Actions for CI/CD workflows.

2. Technology Stack

Backend

Python 3.11: Core programming language

Flask: Lightweight web framework

WeasyPrint: For generating PDFs from HTML/CSS

Frontend

HTML5 & CSS3: UI structure and styling

JavaScript + marked.js: Markdown parsing and preview rendering

DevOps & Infrastructure

Docker: For packaging the application

GitHub Actions: CI/CD automation pipeline

Google Cloud Platform:

Artifact Registry: Docker image storage

GKE (Google Kubernetes Engine): Hosting the application

Cloud Build: Image building & deployment via triggers


3. Local Development Setup

Step 1: Clone the Repository

git clone https://github.com/your-username/md2pdf-converter.git
cd md2pdf-converter

Step 2: Set Up Virtual Environment

python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run the Application

python app.py

Visit http://localhost:5000 in your browser.

4. Docker Setup

Step 1: Build Docker Image

docker build -t md2pdf-app .

Step 2: Run Docker Container

docker run -p 5000:5000 md2pdf-app

This exposes the application locally via Docker.

5. Kubernetes Deployment on Google Cloud

Step 1: Enable GCP Services

Enable GKE, Artifact Registry, and Cloud Build APIs

Step 2: Create a Kubernetes Cluster

6. GitHub Actions CI/CD Pipeline

Goal:

Automatically build, push Docker image, and deploy to GKE on every push to main branch.

Workflow Structure (.github/workflows/deploy.yml):

Checkout code

Set up gcloud CLI

Authenticate using service account

Build & push Docker image

Deploy to GKE

Required Secret:

GCP_SA_KEY: JSON key of GCP service account encoded in base64 and added to GitHub Secrets



8. Markdown Table Rendering

The app supports Markdown tables using marked.js but rendering tables into PDFs requires additional CSS styling.

Enhancements for PDF compatibility:

Add border-collapse and table-layout styling in PDF CSS

Avoid using text-only ASCII table syntax (|---| style)

9. Improvements and Future Work

Store generated PDFs for users

Add login/authentication and history

Theme editor for PDF

Support exporting to DOCX

10. Summary

This project demonstrates full-stack web app development combined with DevOps best practices:

Responsive Markdown UI

Dynamic PDF rendering

Cloud-native deployment with Kubernetes

CI/CD automation

