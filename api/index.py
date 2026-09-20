import os
import sys

# Ensure root directory is on Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import subprocess

_streamlit_proc = None

def app(environ, start_response):
    global _streamlit_proc
    # Launch Streamlit process in background if not already running
    if _streamlit_proc is None or _streamlit_proc.poll() is not None:
        try:
            cmd = [sys.executable, "-m", "streamlit", "run", "app.py", "--server.headless=true", "--server.port=8501"]
            _streamlit_proc = subprocess.Popen(cmd, cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        except Exception:
            pass

    status = '302 Found'
    headers = [
        ('Location', 'http://localhost:8501'),
        ('Content-type', 'text/html; charset=utf-8')
    ]
    start_response(status, headers)
    redirect_html = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=http://localhost:8501">
    <title>Redirecting to AetherMind Genesis</title>
</head>
<body style="background:#050816; color:#FFF; font-family:sans-serif; text-align:center; padding-top:100px;">
    <h2>🌌 Launching AetherMind Genesis OS...</h2>
    <p>If you are not redirected automatically, <a href="http://localhost:8501" style="color:#22D3EE;">click here to launch</a>.</p>
</body>
</html>"""
    return [redirect_html.encode('utf-8')]

def handler(request, response):
    return app(request, response)
