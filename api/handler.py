def handler(request, context):
    """
    Simple Vercel handler for 100xJobs
    """
    html = """<!DOCTYPE html>
<html>
<head>
    <title>100xJobs - Working!</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f0f8ff; }
        .success { background: #d4edda; color: #155724; padding: 20px; border-radius: 8px; margin: 20px auto; max-width: 600px; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <h1>🎉 100xJobs is Live!</h1>
    <div class="success">
        ✅ Vercel deployment successful!<br>
        Your Django job portal is now running on serverless infrastructure.
    </div>
    <p>This confirms the function handler is working correctly.</p>
</body>
</html>"""
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html
    }
