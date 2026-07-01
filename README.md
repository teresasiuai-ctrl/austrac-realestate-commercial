# 📘 AUSTRAC Real Estate AI Agent (Commercial SaaS Edition)

## 🏢 Overview

The AUSTRAC Real Estate AI Agent is a **compliance-focused SaaS simulation platform** built for real estate and property workflows.

It demonstrates how organisations can apply **AML/CTF risk detection, case management, audit logging, and compliance reporting workflows** using an AI-assisted system.

This platform is designed for **internal compliance support, training, and decision assistance (not legal advice or regulatory submission)**.

---

## 🚀 Key Features

* Secure login system (demo authentication)
* Real-time AML/CTF risk scoring engine
* Automated compliance case creation
* High-risk transaction detection
* Case management dashboard (filter, search, track)
* Full audit logging system
* Risk analytics dashboard with visual insights
* Draft Suspicious Matter Report (SMR) generator
* Compliance workflow simulation

---

## 🧠 Core Value

* Reduces manual compliance workload
* Standardises risk assessment processes
* Improves audit visibility and traceability
* Supports internal compliance decision-making
* Generates structured draft compliance reports

---

## 🏗️ System Architecture

Streamlit Frontend (UI Dashboard)
→ Python Application Layer (app.py)
→ Business Logic (Risk Engine + Case Management)
→ SQLite Database (Cases + Audit Logs)

---

## 📁 Project Structure

```
app.py
utils/
  ├── db.py
  ├── auth.py

assets/
  ├── logo.png

requirements.txt
README.md
```

---

## ⚙️ Installation & Run

```bash
git clone https://github.com/your-username/austrac-realestate-ai-agent.git
cd austrac-realestate-ai-agent

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Demo Login

```
Username: admin
Password: admin
```

---

## 📊 Modules Overview

### 📊 Dashboard

* KPI monitoring (cases, risk, exposure)
* Risk distribution charts
* Transaction analytics

### ⚠️ Risk Engine

* Input property ID + transaction amount
* Generates risk score (0–100)
* Automatically creates compliance case

### 📁 Case Management

* View all cases
* Filter by risk level and status
* Search by property ID

### 🧾 Audit Log

* Tracks system activity
* Login events
* Risk checks
* Case creation history

### 📄 Compliance Report Generator

* Generates draft SMR-style reports per case
* Standardised compliance reasoning
* Supports internal review workflows

---

## ⚠️ Compliance Disclaimer

This system is a **decision-support simulation tool only**.

It does not:

* Provide legal or financial advice
* Replace AUSTRAC reporting obligations
* Guarantee regulatory compliance outcomes

Users remain responsible for compliance obligations.

---

## 🚀 Intended Use

Designed for:

* Real estate agencies
* Property compliance teams
* AML/CTF workflow simulation
* Internal training and prototyping

---

## 📌 Roadmap

* Role-based access control (multi-user system)
* PDF export for compliance reports
* PostgreSQL database upgrade
* Production SaaS deployment
* AI-powered risk explanation engine

---

