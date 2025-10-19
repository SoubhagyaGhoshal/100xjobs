# Deploying 100xJobs to Render

This guide will walk you through deploying your Django job portal to Render, a modern cloud platform that makes deployment simple and scalable.

## 🚀 Quick Deployment Steps

### 1. Prepare Your Repository

Make sure your code is pushed to a Git repository (GitHub, GitLab, or Bitbucket):

```bash
# If not already initialized
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/100xjobs.git
git push -u origin main
```

### 2. Create a Render Account

1. Go to [render.com](https://render.com)
2. Sign up with your GitHub/GitLab account
3. This will allow Render to access your repositories

### 3. Create a New Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your repository containing the job portal
3. Configure the service:

#### Basic Settings
- **Name**: `100xjobs-portal` (or your preferred name)
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: Leave empty (unless your Django project is in a subdirectory)

#### Build & Deploy Settings
- **Runtime**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn jobportal.wsgi:application`

#### Environment Variables
Add these environment variables in the Render dashboard:

```
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DEBUG=False
DATABASE_URL=postgresql://user:password@host:port/database
ALLOWED_HOSTS=your-app-name.onrender.com
PYTHON_VERSION=3.11.0
```

### 4. Database Setup

#### Option A: Use Render PostgreSQL (Recommended)
1. Create a new **PostgreSQL** service in Render
2. Copy the **Internal Database URL** 
3. Set it as your `DATABASE_URL` environment variable

#### Option B: External Database
Use any PostgreSQL provider (AWS RDS, Google Cloud SQL, etc.) and set the connection URL.

### 5. Deploy

1. Click **"Create Web Service"**
2. Render will automatically:
   - Clone your repository
   - Run the build command
   - Install dependencies
   - Start your application

## 📁 Required Files

Your project already includes most required files, but here's what Render needs:

### ✅ Already Present
- `requirements.txt` - Python dependencies
- `build.sh` - Build script (will be updated)
- `manage.py` - Django management
- Proper Django settings with environment variables

### 🔄 Files We'll Update
- `build.sh` - Enhanced for Render
- `settings.py` - Add Render-specific configurations

## 🔧 Configuration Details

### Environment Variables Explained

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-xyz123...` |
| `DEBUG` | Debug mode (always False in production) | `False` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host:5432/db` |
| `ALLOWED_HOSTS` | Allowed hostnames | `your-app.onrender.com` |
| `PYTHON_VERSION` | Python version to use | `3.11.0` |

### Build Process

Render will execute these steps:
1. Install Python dependencies from `requirements.txt`
2. Run database migrations
3. Collect static files
4. Create superuser (if configured)
5. Start the Gunicorn server

## 🌐 Custom Domain (Optional)

1. Go to your service settings
2. Click **"Custom Domains"**
3. Add your domain (e.g., `jobs.yourdomain.com`)
4. Update your DNS to point to Render's servers
5. Render will automatically provision SSL certificates

## 📊 Monitoring & Logs

- **Logs**: Available in the Render dashboard
- **Metrics**: CPU, memory, and request metrics
- **Health Checks**: Automatic health monitoring
- **Alerts**: Email notifications for issues

## 🔄 Automatic Deployments

Render automatically deploys when you push to your connected branch:

```bash
# Make changes to your code
git add .
git commit -m "Update feature"
git push origin main
# Render automatically deploys the changes
```

## 💰 Pricing

- **Free Tier**: Available with limitations (sleeps after 15 minutes of inactivity)
- **Paid Plans**: Start at $7/month for always-on services
- **Database**: PostgreSQL starts at $7/month

## 🛠 Troubleshooting

### Common Issues

1. **Build Fails**
   - Check build logs in Render dashboard
   - Ensure all dependencies are in `requirements.txt`
   - Verify Python version compatibility

2. **Database Connection Issues**
   - Verify `DATABASE_URL` is correct
   - Ensure database service is running
   - Check firewall/security group settings

3. **Static Files Not Loading**
   - Ensure `STATIC_ROOT` is set correctly
   - Check WhiteNoise configuration
   - Verify `collectstatic` runs in build process

4. **Application Won't Start**
   - Check start command: `gunicorn jobportal.wsgi:application`
   - Verify WSGI configuration
   - Check for import errors in logs

### Debug Commands

```bash
# Check logs
# (Available in Render dashboard)

# Connect to your service shell (if needed)
# Available through Render dashboard
```

## 🔐 Security Best Practices

1. **Environment Variables**: Never commit secrets to Git
2. **HTTPS**: Always enabled on Render
3. **Database**: Use strong passwords
4. **Updates**: Keep dependencies updated
5. **Monitoring**: Set up alerts for errors

## 📈 Performance Optimization

1. **Database**: Use connection pooling
2. **Static Files**: Leverage WhiteNoise compression
3. **Caching**: Consider Redis for session storage
4. **CDN**: Use Render's global CDN for static assets

## 🎯 Next Steps After Deployment

1. **Test thoroughly**: Check all functionality
2. **Set up monitoring**: Configure alerts
3. **Backup strategy**: Regular database backups
4. **Custom domain**: Add your own domain
5. **SSL certificate**: Automatically provided
6. **Performance monitoring**: Use Render's metrics

## 📞 Support

- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Community**: Render Discord/Forum
- **Support**: Available for paid plans

---

Your Django job portal is now ready for production deployment on Render! 🚀
