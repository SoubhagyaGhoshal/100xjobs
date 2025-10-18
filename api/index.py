from http.server import BaseHTTPRequestHandler
import os
import sys
from pathlib import Path
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Add the project root to Python path
            BASE_DIR = Path(__file__).resolve().parent.parent
            if str(BASE_DIR) not in sys.path:
                sys.path.insert(0, str(BASE_DIR))

            # Set Django settings module
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')

            # Import Django after path setup
            import django
            from django.core.wsgi import get_wsgi_application
            from django.http import HttpResponse
            from django.conf import settings

            # Configure Django if not already configured
            if not settings.configured:
                django.setup()

            # Simple response for now
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>100xJobs - Job Portal</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                    .container { max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                    h1 { color: #333; text-align: center; }
                    .status { background: #d4edda; color: #155724; padding: 15px; border-radius: 4px; margin: 20px 0; }
                    .links { text-align: center; margin-top: 30px; }
                    .links a { display: inline-block; margin: 10px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 4px; }
                    .links a:hover { background: #0056b3; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🚀 100xJobs - Professional Job Portal</h1>
                    <div class="status">
                        ✅ Django application is running successfully on Vercel!
                    </div>
                    <p>Welcome to the 100xJobs professional job portal. This Django application is now deployed and running on Vercel's serverless infrastructure.</p>
                    
                    <div class="links">
                        <a href="/admin/">Admin Panel</a>
                        <a href="/accounts/login/">Login</a>
                        <a href="/accounts/register/">Register</a>
                    </div>
                    
                    <p><strong>Features:</strong></p>
                    <ul>
                        <li>Job posting and management for employers</li>
                        <li>Job search and application for job seekers</li>
                        <li>User authentication with role-based access</li>
                        <li>Admin panel for system management</li>
                        <li>Responsive design with Bootstrap 5</li>
                    </ul>
                </div>
            </body>
            </html>
            """
            
            self.wfile.write(html_content.encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            error_html = f"""
            <html>
            <body>
                <h1>Error</h1>
                <p>Error: {str(e)}</p>
                <p>Type: {type(e).__name__}</p>
            </body>
            </html>
            """
            self.wfile.write(error_html.encode())

    def do_POST(self):
        self.do_GET()  # Handle POST same as GET for now
