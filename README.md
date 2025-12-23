# 🛰️ AETHER-SCAN
**AETHER-SCAN** is a lightweight, high-performance, and containerized network port scanner designed for security enthusiasts and DevOps engineers. Built with Python and optimized with Docker, it allows for rapid network mapping with banner grabbing and multi-threaded execution.

---

## 🚀 Key Features
* **Multi-Threaded Performance:** Scan hundreds of ports simultaneously using Python's `ThreadPoolExecutor`.
* **Banner Grabbing:** Automatically attempts to identify services running on open ports.
* **Dockerized Deployment:** Zero-dependency installation—run it anywhere that has Docker.
* **Persistent Logging:** Results are automatically saved as structured `JSON` files for later analysis.
* **Highly Configurable:** Control targets, port ranges, and speeds via environment variables.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have the following installed:
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Clone the Repository
```bash
git clone https://github.com/GarethMSheldon/aether-network-scan
cd aether-scan
