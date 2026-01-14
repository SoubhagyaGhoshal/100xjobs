def handler(request, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '''
        <!DOCTYPE html>
        <html>
        <head><title>100xJobs - Live!</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px; background: #f0f8ff;">
            <h1>🎉 Success!</h1>
            <p>100xJobs is now running on Vercel!</p>
            <p>The deployment is working correctly.</p>
        </body>
        </html>
        '''
    }
