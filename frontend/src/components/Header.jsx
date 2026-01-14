import { Link, useNavigate } from 'react-router-dom';
import { Sun, Moon, LogOut, User as UserIcon } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';
import { useState, useEffect } from 'react';
import { getCurrentUser, logoutUser } from '../utils/authUtils';
import Logo from './Logo';
import './Header.css';

const Header = () => {
    const { theme, toggleTheme } = useTheme();
    const navigate = useNavigate();
    const [user, setUser] = useState(null);

    useEffect(() => {
        // Check for logged in user using secure storage
        const userData = getCurrentUser();
        if (userData) {
            setUser(userData);
        }

        // Listen for auth changes
        const handleAuthChange = () => {
            const userData = getCurrentUser();
            setUser(userData || null);
        };

        window.addEventListener('auth-change', handleAuthChange);
        window.addEventListener('session-timeout', handleAuthChange);

        return () => {
            window.removeEventListener('auth-change', handleAuthChange);
            window.removeEventListener('session-timeout', handleAuthChange);
        };
    }, []);

    const handleLogout = () => {
        logoutUser();
        window.dispatchEvent(new Event('auth-change'));
        setUser(null);
        navigate('/');
    };

    return (
        <header className="header glass">
            <div className="container">
                <div className="header-content">
                    <Link to="/" className="logo">
                        <Logo className="logo-icon-svg" />
                        <h3 className="logo-text">
                            <span className="text-100x">100x</span>
                            <span className="text-jobs">Jobs</span>
                        </h3>
                    </Link>

                    <nav className="nav">
                        <Link to="/jobs" className="nav-link">Explore jobs</Link>
                        <a href="mailto:contact@100xjobs.com" className="nav-link">Contact us</a>
                    </nav>

                    <div className="header-actions">
                        <button
                            onClick={toggleTheme}
                            className="theme-toggle"
                            aria-label="Toggle theme"
                        >
                            {theme === 'light' ? <Moon size={20} /> : <Sun size={20} />}
                        </button>

                        {user ? (
                            <div className="user-menu">
                                <div className="user-info">
                                    <UserIcon size={18} />
                                    <span>{user.name}</span>
                                </div>
                                <button onClick={handleLogout} className="btn btn-secondary btn-logout">
                                    <LogOut size={18} />
                                    Logout
                                </button>
                            </div>
                        ) : (
                            <Link to="/login" className="btn btn-primary">Login</Link>
                        )}
                    </div>
                </div>
            </div>
        </header>
    );
};

export default Header;
