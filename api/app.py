from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>100xJobs - Success!</title>
            <style>
                body { 
                    font-family: -apple-system, BlinkMacSystemFont, sans-serif; 
                    margin: 0; 
                    padding: 40px; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .container { 
                    background: white; 
                    padding: 40px; 
                    border-radius: 12px; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                    text-align: center;
                    max-width: 600px;
                }
                h1 { color: #333; margin-bottom: 20px; }
                .success { 
                    background: #d4edda; 
                    color: #155724; 
                    padding: 20px; 
                    border-radius: 8px; 
                    margin: 20px 0; 
                    font-weight: bold;
                }
                .info { color: #666; line-height: 1.6; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎉 100xJobs Deployed Successfully!</h1>
                <div class="success">
                    ✅ Your Django job portal is now live on Vercel!
                </div>
                <div class="info">
                    <p>The serverless function is working correctly.</p>
                    <p>This confirms that your application can handle HTTP requests on Vercel's infrastructure.</p>
                    <p><strong>Next:</strong> We can now integrate Django functionality step by step.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(html.encode())
        
    def do_POST(self):
        self.do_GET()
