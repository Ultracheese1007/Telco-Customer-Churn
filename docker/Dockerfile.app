# docker/Dockerfile.app
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY ./src ./src
COPY ./models ./models
COPY ./reports ./reports
COPY ./data ./data

# Add /app to Python path so "src" can be imported
ENV PYTHONPATH="/app"

# Expose Streamlit default port
EXPOSE 8501

# Launch Streamlit app
CMD ["streamlit", "run", "src/app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
