# playwrite official image for python 
FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Chromium for Playwright 
RUN playwright install chromium

# Copy all app files
COPY . .

# Expose port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
