# 🚀 Quick Deploy to Vercel

## Fastest Way (3 commands)

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Navigate to frontend
cd frontend

# 3. Deploy
vercel --prod
```

That's it! Your app will be live at `https://your-project-name.vercel.app`

---

## Alternative: Use Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your Git repo
4. Set **Root Directory** to `frontend`
5. Click "Deploy"

---

## Vercel Project Settings

| Setting | Value |
|---------|-------|
| Framework | Vite |
| Root Directory | `frontend` |
| Build Command | `npm run build` |
| Output Directory | `dist` |

---

## Files Created

✅ `frontend/vercel.json` - SPA routing & security headers  
✅ `frontend/DEPLOYMENT.md` - Detailed instructions  
✅ Build tested and verified  

---

## What's Included

- ✅ Secure login with password hashing
- ✅ Rate limiting (5 attempts/15 min)
- ✅ Password strength meter
- ✅ Session management (30 min timeout)
- ✅ Job application flow
- ✅ Responsive design
- ✅ Dark/Light theme

---

**Ready to deploy!** 🎉
