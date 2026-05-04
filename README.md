# SnapClass - AI Attendance System 🚀

SnapClass is a modern, AI-powered attendance system that integrates a beautiful Flask landing page with a powerful Streamlit application. It uses Face Recognition and Voice AI to make attendance faster and more secure.

## 🌟 Features

- **Modern Landing Page**: A sleek, professional entry point built with Flask.
- **AI-Powered Attendance**: Face recognition and voice embedding for student verification.
- **Teacher Dashboard**: Manage subjects, students, and view attendance logs.
- **Student Portal**: Students can view their attendance and enroll in subjects.
- **Supabase Integration**: Robust backend for database and file storage.
- **Real-time Logs**: Instant attendance tracking with QR code support.

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Main App), HTML/CSS/JS (Landing Page)
- **Backend**: Flask, Python
- **Database**: Supabase
- **AI/ML**: Face Recognition, Resemblyzer, Scikit-learn
- **Design**: Vanilla CSS with modern aesthetics.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- A Supabase Project

### 2. Installation
Clone the repository:
```bash
git clone https://github.com/PratyushPandey31/AI-ATTENDANCE.git
cd AI-ATTENDANCE
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory and add your Supabase credentials:
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

### 4. Running the Application
Launch both the Landing Page and the Streamlit App simultaneously:
```bash
python run_all.py
```

- **Landing Page**: http://localhost:5002
- **Streamlit App**: http://localhost:8501

## 📂 Project Structure

- `app/`: Streamlit application source code.
- `landing/`: Flask landing page source code.
- `run_all.py`: Central script to run both services.
- `requirements.txt`: Unified dependency list.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---
Built with ❤️ by [Pratyush Pandey](https://github.com/PratyushPandey31)
