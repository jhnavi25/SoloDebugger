# 🔍 SoloDebugger: Faculty Expertise Finder
**Connecting Students with Mentorship, Instantly.**

[![Live MVP](https://img.shields.io/badge/Live-MVP_Link-green?style=for-the-badge)](INSERT_YOUR_RENDER_LINK_HERE)
[![Flask](https://img.shields.io/badge/Flask-v3.0-blue?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## 📌 Project Overview
Finding the right mentor for technical projects is often a manual, time-consuming process for students. Currently, students waste weeks visiting different departments just to find a professor whose expertise matches their project. 

**SoloDebugger** is a streamlined digital platform designed to bridge the gap between student innovation and faculty expertise. By categorizing faculty members through specific technology tags (e.g., AI, Blockchain, IoT), we eliminate "departmental silos" and allow students to find the perfect mentor in seconds.

## 🚀 Key Features
* **Smart Skill Search:** Instant filtering of faculty based on specific technology expertise (e.g., Python, React, IoT).
* **Humanized Profiles:** Beyond just names—view office locations, bios, and specific research interests.
* **Glassmorphic UI:** A modern, premium interface built for high readability and responsiveness.
* **One-Click Inquiry:** Integrated email triggers to streamline student-faculty communication.
* **Secure Access:** Dedicated student login portal for campus-specific privacy.

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3 (Modern Glassmorphism), JavaScript.
* **Backend:** Python (Flask Framework).
* **Styling & Assets:** Google Fonts (Poppins), Google Material Icons.
* **Deployment:** Render Cloud Hosting using Gunicorn (WSGI Server).

## 🏗️ Architecture
The system follows a Model-View-Controller (MVC) architecture:
1.  **View:** Responsive UI that captures student queries and displays results.
2.  **Controller (Flask):** The engine that handles search logic and filters data.
3.  **Model:** A structured data repository of faculty profiles and skill sets.



## 📋 Process Flow
1.  **User Entry:** Student visits the live portal and logs in.
2.  **Input:** Student enters a tech keyword (e.g., "Machine Learning").
3.  **Search Logic:** Flask scans the database for matching expertise tags.
4.  **Result:** The UI displays cards with faculty contact info and cabin locations.



## 💻 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SoloDebugger.git]
