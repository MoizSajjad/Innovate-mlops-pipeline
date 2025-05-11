# Base Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy minimal dependency file for API
COPY requirements-api.txt .

# Install only essential dependencies
RUN pip install --upgrade pip && pip install -r requirements-api.txt

# Copy entire project into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/api/app.py"]
