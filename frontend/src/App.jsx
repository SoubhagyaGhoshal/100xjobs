import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import ExploreJobs from './pages/ExploreJobs';
import JobDetail from './pages/JobDetail';
import Login from './pages/Login';
import Register from './pages/Register';

function App() {
  return (
    <ThemeProvider>
      <Router>
        <div className="app">
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/jobs" element={<ExploreJobs />} />
            <Route path="/jobs/:id" element={<JobDetail />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/about" element={<div className="container" style={{ padding: '3rem 0', textAlign: 'center' }}><h2>About Us (Coming Soon)</h2></div>} />
            <Route path="/terms" element={<div className="container" style={{ padding: '3rem 0', textAlign: 'center' }}><h2>Terms of Service (Coming Soon)</h2></div>} />
            <Route path="/privacy" element={<div className="container" style={{ padding: '3rem 0', textAlign: 'center' }}><h2>Privacy Policy (Coming Soon)</h2></div>} />
          </Routes>
          <Footer />
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
