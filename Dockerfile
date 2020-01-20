# Define base image
FROM python:3.7-slim-buster

# Install necessary Python packages
RUN pip install -U nilearn matplotlib

# Copy function from "host" to image
COPY compute_tsnr.py /src/compute_tsnr.py

# Define command to run when calling "docker run {hub}/mr-tsnr:{tag}"
ENTRYPOINT ["python", "/src/compute_tsnr.py"]