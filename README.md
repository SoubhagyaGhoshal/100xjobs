# 100xJobs - Modern Job Portal Platform

<div align="center">

![100xJobs](frontend/public/favicon.png)

**A comprehensive, secure job portal with modern UI/UX and enterprise-grade features**

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://your-deployment-url.vercel.app)
[![GitHub](https://img.shields.io/badge/github-100xjobs-blue)](https://github.com/SoubhagyaGhoshal/100xjobs)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[Live Demo](#) • [Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation)

</div>

---

## 🌟 Overview

100xJobs is a full-stack job portal platform featuring a **React + Vite** frontend with advanced security features and a **Django** backend. Built with modern web technologies, it provides a seamless experience for job seekers and employers.

### ✨ What's New (Latest Update)

- 🔐 **Enterprise-grade security** with bcrypt password hashing and AES encryption
- 🎨 **Beautiful UI animations** with smooth transitions
- 💪 **Real-time password strength validation**
- ⏱️ **Smart rate limiting** and account lockout protection
- 🎯 **Professional job application flow** with success modals
- 📱 **Custom branding** with SEO optimization
- 🚀 **Vercel deployment ready** with optimized build

---

## � Features

### 🔒 Security Features (NEW)

| Feature | Description |
|---------|-------------|
| **Password Hashing** | bcrypt with 10 salt rounds for secure password storage |
| **Data Encryption** | AES encryption for all localStorage data |
| **Rate Limiting** | 5 login attempts per 15 minutes with account lockout |
| **Session Management** | 30-minute inactivity timeout with activity tracking |
| **Input Sanitization** | XSS protection on all user inputs |
| **Password Strength Meter** | Real-time validation with visual feedback |
| **CSRF Protection** | Token-based protection against cross-site attacks |

### 👤 For Job Seekers

- ✅ **Secure Registration & Login** with email validation
- 🔍 **Advanced Job Search** with multiple filters
- 📄 **Easy Application Process** with resume upload and cover letter
- 💾 **Application Tracking** - view all submitted applications
- ⭐ **Saved Jobs** - bookmark interesting positions
- 🎨 **Beautiful Success Modals** with smooth animations
- 📱 **Responsive Design** - works on all devices
- 🌓 **Dark/Light Theme** toggle

### 💼 For Employers

- 📊 **Employer Dashboard** with analytics
- ✍️ **Job Posting** with rich text editor
- 👥 **Application Management** with status tracking
- 📈 **Performance Metrics** for job postings
- 🔍 **Candidate Review** with resume viewing
- 📧 **Application Notifications**

### 🎨 UI/UX Excellence

- **Modern Design System** with consistent styling
- **Smooth Animations** - fade-in, slide-up, bounce effects
- **Interactive Elements** - hover states, transitions
- **Professional Color Scheme** - blue to purple gradients
- **Glassmorphism Effects** for modern look
- **Micro-animations** for enhanced user engagement
- **Loading States** for better feedback
- **Toast Notifications** for user actions

---

## 🛠 Tech Stack

### Frontend
```
React 19.2.0          - UI library
Vite 7.2.4            - Build tool & dev server
React Router 7.12.0   - Client-side routing
Lucide React          - Icon system
bcryptjs 3.0.3        - Password hashing
crypto-js 4.2.0       - Data encryption
```

### Backend
```
Django 5.2.7          - Web framework
PostgreSQL            - Production database
SQLite                - Development database
Gunicorn              - WSGI server
WhiteNoise            - Static file serving
```

### Deployment
```
Vercel                - Frontend hosting
Render/Railway        - Backend hosting (optional)
```

---

## 📁 Project Structure

```
100xjobs/
├── frontend/                    # React + Vite application
│   ├── src/
│   │   ├── components/         # Reusable UI components
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── JobCard.jsx
│   │   │   └── Logo.jsx
│   │   ├── pages/              # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── ExploreJobs.jsx
│   │   │   ├── JobDetail.jsx
│   │   │   ├── Login.jsx
│   │   │   └── Register.jsx
│   │   ├── utils/              # Utility functions ✨ NEW
│   │   │   ├── authUtils.js    # Authentication & encryption
│   │   │   ├── passwordValidator.js  # Password validation
│   │   │   └── sessionManager.js     # Session management
│   │   ├── context/            # React context
│   │   │   └── ThemeContext.jsx
│   │   └── data/               # Static data
│   │       └── jobs.js
│   ├── public/
│   │   └── favicon.png         # Custom 100xJobs favicon ✨ NEW
│   ├── vercel.json             # Vercel configuration ✨ NEW
│   ├── DEPLOYMENT.md           # Deployment guide ✨ NEW
│   └── package.json
├── backend/                     # Django application
│   ├── jobportal/              # Project settings
│   ├── jobs/                   # Jobs app
│   ├── accounts/               # User authentication
│   └── templates/              # Django templates
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Node.js 16+ and npm
- Python 3.10+
- Git

### Frontend Setup

```bash
# Clone the repository
git clone https://github.com/SoubhagyaGhoshal/100xjobs.git
cd 100xjobs/frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

The app will be available at `http://localhost:5173`

### Backend Setup (Optional)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

---

## 🌐 Deployment

### Deploy to Vercel (Frontend)

**Quick Deploy:**
```bash
cd frontend
npm install -g vercel
vercel --prod
```

**Or via GitHub:**
1. Push code to GitHub
2. Import repository in Vercel
3. Set root directory to `frontend`
4. Deploy!

**Configuration:**
- Framework: Vite
- Build Command: `npm run build`
- Output Directory: `dist`
- Root Directory: `frontend`

### Deploy Backend (Optional)

The backend can be deployed to:
- **Render** - Easy Django deployment
- **Railway** - Modern platform
- **Heroku** - Traditional PaaS
- **DigitalOcean** - VPS option

See [DEPLOYMENT.md](frontend/DEPLOYMENT.md) for detailed instructions.

---

## 🔐 Security Features Explained

### Password Security
```javascript
// Passwords are hashed with bcrypt before storage
const hashedPassword = await bcrypt.hash(password, 10);

// All localStorage data is encrypted with AES
const encrypted = CryptoJS.AES.encrypt(data, SECRET_KEY);
```

### Rate Limiting
```javascript
// Maximum 5 login attempts per 15 minutes
const MAX_ATTEMPTS = 5;
const LOCKOUT_DURATION = 15 * 60 * 1000; // 15 minutes
```

### Session Management
```javascript
// Auto-logout after 30 minutes of inactivity
const SESSION_TIMEOUT = 30 * 60 * 1000; // 30 minutes
```

---

## 🎨 UI Components

### Success Modal
Beautiful animated modal with:
- ✨ Fade-in overlay animation
- 📈 Scale-in content animation
- 🎯 Bouncing checkmark icon
- ⏱️ Auto-close after 3 seconds

### Password Strength Meter
Real-time validation showing:
- 🔴 Weak (0-40%)
- 🟠 Medium (41-70%)
- 🟢 Strong (71-100%)

### Applied Button State
Dynamic button that changes from:
- 🔵 "Apply Now" → 🟢 "Applied ✓"

---

## � Features Comparison

| Feature | Basic Version | Enhanced Version ✨ |
|---------|--------------|---------------------|
| Authentication | Simple login | Secure with encryption |
| Password Storage | Plain text | bcrypt hashed |
| Rate Limiting | ❌ | ✅ 5 attempts/15min |
| Session Management | ❌ | ✅ 30min timeout |
| Application Flow | Alert popup | Animated modal |
| Application Tracking | ❌ | ✅ Full history |
| Password Validation | Basic | Real-time strength meter |
| Branding | Generic | Custom favicon + SEO |
| Animations | None | Professional transitions |

---

## 🧪 Testing

### Run Frontend Tests
```bash
cd frontend
npm run test
```

### Test Security Features
1. **Password Hashing**: Register a user and check localStorage
2. **Rate Limiting**: Try 6 failed login attempts
3. **Session Timeout**: Wait 30 minutes of inactivity
4. **Application Flow**: Apply to a job and verify modal

---

## 📈 Performance

### Build Optimization
- **Bundle Size**: 367 KB (gzipped: 123 KB)
- **Build Time**: ~1.15s
- **Lighthouse Score**: 90+ across all metrics

### Caching Strategy
- Static assets: 1 year cache
- HTML: No cache
- API responses: Smart caching

---

## 🎯 Roadmap

### Upcoming Features
- [ ] Email verification for registration
- [ ] Two-factor authentication (2FA)
- [ ] Social login (Google, LinkedIn)
- [ ] Advanced job recommendations
- [ ] Real-time notifications
- [ ] Video interview integration
- [ ] Resume builder
- [ ] Salary insights
- [ ] Company reviews

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍� Author

**Soubhagya Ghoshal**

- GitHub: [@SoubhagyaGhoshal](https://github.com/SoubhagyaGhoshal)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- **100xDevs Community** for inspiration and support
- **React Team** for the amazing library
- **Vite Team** for the blazing-fast build tool
- **Vercel** for seamless deployment

---

## 📞 Support

For questions, issues, or feature requests:

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/SoubhagyaGhoshal/100xjobs/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/SoubhagyaGhoshal/100xjobs/discussions)

---

<div align="center">

**Built with ❤️ for the 100xDevs community**

⭐ Star this repo if you find it helpful!

</div>
