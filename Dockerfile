# Use Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 8080

# Set environment variables
ENV PORT=8080

# Run the Flask app
CMD ["python", "FlaskApp.py"]

