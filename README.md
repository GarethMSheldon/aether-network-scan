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
```

# 3. Configure Your Scan
Edit the `.env` file to set your **target** and **speed**:

* **SCAN_TARGET**=scanme.nmap.org
* **SCAN_PORTS**=20-1000
* **SCAN_TIMEOUT**=0.8
* **MAX_THREADS**=100

# 🛡️ Ethical Hacking Warning

* AETHER-SCAN is intended for educational purposes and authorized security testing only.
* Scanning networks you do not have explicit permission to test is illegal and unethical.
* Use this tool responsibly.

---

# 📄 License

Distributed under the MIT License. See LICENSE for more information.

---

# 📂 Suggested File Additions

### 1. .gitignore

```text
logs/*.json
__pycache__/
.env
.DS_Store

```



