# ============================
# Telco Customer Churn Project
# ============================

# Default Docker Compose file
COMPOSE_FILE = docker/docker-compose.yml

# ============================
# 1️⃣ Build & Run
# ============================

build:
	@echo "🛠️  Building Docker images..."
	docker compose -f $(COMPOSE_FILE) build

up:
	@echo "🚀 Starting services..."
	docker compose -f $(COMPOSE_FILE) up -d

down:
	@echo "🧹 Stopping all containers..."
	docker compose -f $(COMPOSE_FILE) down

rebuild:
	@echo "🔁 Rebuilding containers..."
	docker compose -f $(COMPOSE_FILE) down
	docker compose -f $(COMPOSE_FILE) build --no-cache
	docker compose -f $(COMPOSE_FILE) up -d

# ============================
# 2️⃣ Logs & Debug
# ============================

logs-api:
	docker logs -f telco-api

logs-app:
	docker logs -f telco-app

# ============================
# 3️⃣ Cleanup
# ============================

clean:
	@echo "🧹 Removing Python cache files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "✅ All cache files removed."

# ============================
# 4️⃣ Local Run (optional)
# ============================

run-api:
	@echo "▶️ Running FastAPI locally..."
	uvicorn src.api.main:app --reload --port 8000

run-app:
	@echo "▶️ Running Streamlit locally..."
	streamlit run src/app/streamlit_app.py

# ============================
# Helper
# ============================

status:
	docker compose -f $(COMPOSE_FILE) ps
