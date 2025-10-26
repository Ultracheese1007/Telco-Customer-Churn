# ============================
# Telco Customer Churn Project
# ============================

# Default Docker Compose file
COMPOSE_FILE := docker/docker-compose.yml

# ============================
# 0️⃣ Environment Check
# ============================

.PHONY: check
check:
	@command -v docker >/dev/null 2>&1 || (echo "❌ Docker not found. Please install Docker." && exit 1)
	@command -v docker compose >/dev/null 2>&1 || (echo "❌ Docker Compose plugin not found." && exit 1)
	@echo "✅ Environment check passed."

# ============================
# 1️⃣ Build & Run
# ============================

build: check
	@echo "🛠️  Building Docker images..."
	docker compose -f $(COMPOSE_FILE) build

up: check
	@echo "🚀 Starting services..."
	docker compose -f $(COMPOSE_FILE) up -d
	@echo "✅ All services are running. Use 'make status' to view container status."

down:
	@echo "🧹 Stopping all containers..."
	docker compose -f $(COMPOSE_FILE) down

rebuild: check
	@echo "🔁 Rebuilding containers from scratch..."
	docker compose -f $(COMPOSE_FILE) down
	docker compose -f $(COMPOSE_FILE) build --no-cache
	docker compose -f $(COMPOSE_FILE) up -d
	@echo "🧼 Cleaning dangling images..."
	docker image prune -f

# ============================
# 2️⃣ Logs & Debug
# ============================

logs-api:
	@echo "📜 Viewing FastAPI logs..."
	docker logs -f telco-api

logs-app:
	@echo "📜 Viewing Streamlit logs..."
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

clean-all: clean
	@echo "🧽 Removing all stopped containers and dangling images..."
	docker container prune -f
	docker image prune -f
	docker volume prune -f
	@echo "✅ System cleaned."

# ============================
# 4️⃣ Local Run (optional)
# ============================

run-api:
	@echo "▶️ Running FastAPI locally on http://localhost:8000 ..."
	uvicorn src.api.main:app --reload --port 8000

run-app:
	@echo "▶️ Running Streamlit locally on http://localhost:8501 ..."
	streamlit run src/app/streamlit_app.py

# ============================
# 5️⃣ Helper
# ============================

status:
	@echo "📦 Container status:"
	docker compose -f $(COMPOSE_FILE) ps
