def handler(request, context):
    """
    Vercel serverless function handler for Django application
    """
    try:
        # Simple HTML response for now
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>100xJobs - Job Portal</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body { 
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
                    margin: 0; 
                    padding: 40px 20px; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    color: #333;
                }
                .container { 
                    max-width: 800px; 
                    margin: 0 auto; 
                    background: white; 
                    padding: 40px; 
                    border-radius: 12px; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                }
                h1 { 
                    color: #333; 
                    text-align: center; 
                    margin-bottom: 10px;
                    font-size: 2.5em;
                }
                .subtitle {
                    text-align: center;
                    color: #666;
                    margin-bottom: 30px;
                    font-size: 1.1em;
                }
                .status { 
                    background: linear-gradient(135deg, #4CAF50, #45a049); 
                    color: white; 
                    padding: 20px; 
                    border-radius: 8px; 
                    margin: 30px 0; 
                    text-align: center;
                    font-weight: bold;
                    font-size: 1.1em;
                }
                .links { 
                    text-align: center; 
                    margin: 40px 0; 
                }
                .links a { 
                    display: inline-block; 
                    margin: 10px; 
                    padding: 12px 24px; 
                    background: linear-gradient(135deg, #007bff, #0056b3); 
                    color: white; 
                    text-decoration: none; 
                    border-radius: 6px; 
                    transition: transform 0.2s, box-shadow 0.2s;
                    font-weight: 500;
                }
                .links a:hover { 
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(0,123,255,0.3);
                }
                .features {
                    background: #f8f9fa;
                    padding: 30px;
                    border-radius: 8px;
                    margin-top: 30px;
                }
                .features h3 {
                    color: #333;
                    margin-bottom: 20px;
                    text-align: center;
                }
                .features ul {
                    list-style: none;
                    padding: 0;
                }
                .features li {
                    padding: 8px 0;
                    border-bottom: 1px solid #eee;
                }
                .features li:before {
                    content: "✓ ";
                    color: #4CAF50;
                    font-weight: bold;
                    margin-right: 10px;
                }
                .tech-stack {
                    text-align: center;
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #eee;
                    color: #666;
                    font-size: 0.9em;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 100xJobs</h1>
                <div class="subtitle">Professional Job Portal</div>
                
                <div class="status">
                    ✅ Successfully deployed on Vercel!
                </div>
                
                <p style="text-align: center; font-size: 1.1em; line-height: 1.6;">
                    Welcome to 100xJobs, a comprehensive job portal built with Django. 
                    This application is now running on Vercel's serverless infrastructure.
                </p>
                
                <div class="links">
                    <a href="/admin/">🔧 Admin Panel</a>
                    <a href="/accounts/login/">🔐 Login</a>
                    <a href="/accounts/register/">📝 Register</a>
                </div>
                
                <div class="features">
                    <h3>🌟 Key Features</h3>
                    <ul>
                        <li>Job posting and management for employers</li>
                        <li>Advanced job search and filtering for job seekers</li>
                        <li>User authentication with role-based access control</li>
                        <li>Application tracking and management system</li>
                        <li>Responsive design optimized for all devices</li>
                        <li>Admin panel for comprehensive system management</li>
                        <li>File upload support for resumes and documents</li>
                        <li>Email notifications and communication system</li>
                    </ul>
                </div>
                
                <div class="tech-stack">
                    <strong>Tech Stack:</strong> Django 5.2.7 • Python 3.9+ • Bootstrap 5 • SQLite/PostgreSQL • Vercel Serverless
                </div>
            </div>
        </body>
        </html>
        """
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html; charset=utf-8',
                'Cache-Control': 'public, max-age=300'
            },
            'body': html_content
        }
        
    except Exception as e:
        # Return error page
        error_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error - 100xJobs</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
                .error {{ background: #f8d7da; color: #721c24; padding: 20px; border-radius: 8px; }}
            </style>
        </head>
        <body>
            <div class="error">
                <h1>Application Error</h1>
                <p><strong>Error:</strong> {str(e)}</p>
                <p><strong>Type:</strong> {type(e).__name__}</p>
                <p>Please check the deployment logs for more details.</p>
            </div>
        </body>
        </html>
        """
        
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'text/html; charset=utf-8'
            },
            'body': error_html
        }
