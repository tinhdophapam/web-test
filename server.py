#!/usr/bin/env python3
"""
Simple HTTP Server with CORS support for local development
"""
import http.server
import socketserver
from http import HTTPStatus

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()

    def log_message(self, format, *args):
        # Custom log format
        print(f"[{self.log_date_time_string()}] {format % args}")

PORT = 8000

print(f"""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   🎵 Tịnh Độ Pháp Âm - Local Development Server 🎵      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

✅ Server đang chạy tại:
   
   🌐 Local:    http://localhost:{PORT}
   🌐 Network:  http://127.0.0.1:{PORT}

📱 Để truy cập từ điện thoại:
   1. Kiểm tra IP máy tính: ipconfig (Windows) hoặc ifconfig (Mac/Linux)
   2. Truy cập: http://[IP-của-bạn]:{PORT}

🛑 Nhấn Ctrl+C để dừng server

════════════════════════════════════════════════════════════
""")

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server đã dừng. Tạm biệt!")
        httpd.shutdown()
