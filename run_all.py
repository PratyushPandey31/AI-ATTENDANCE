import subprocess
import time
import sys
import os

def run_landing():
    print("Starting Flask Landing Page on http://localhost:5002...")
    return subprocess.Popen([sys.executable, "landing/app.py"])

def run_app():
    print("Starting Streamlit App on http://localhost:8501...")
    # Streamlit needs to be run via the streamlit module
    return subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app/app.py", "--browser.gatherUsageStats", "false"])



if __name__ == "__main__":
    try:
        landing_proc = run_landing()
        time.sleep(2)  # Give landing page a moment to start
        app_proc = run_app()

        print("\nBoth services are running.")
        print("Press Ctrl+C to stop both.")

        while True:
            time.sleep(1)
            if landing_proc.poll() is not None:
                print("Landing page process exited.")
                break
            if app_proc.poll() is not None:
                print("Streamlit app process exited.")
                break

    except KeyboardInterrupt:
        print("\nStopping services...")
        landing_proc.terminate()
        app_proc.terminate()
        print("Done.")
