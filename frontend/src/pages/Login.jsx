import { useState, useEffect } from 'react';
import { useNavigate, Link, useSearchParams } from 'react-router-dom';
import { Mail, Lock, Eye, EyeOff, AlertCircle, Loader } from 'lucide-react';
import { authenticateUser, setCurrentUser } from '../utils/authUtils';
import { initSessionManager } from '../utils/sessionManager';
import './Login.css';

const Login = () => {
    const navigate = useNavigate();
    const [searchParams] = useSearchParams();
    const [showPassword, setShowPassword] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [attemptsLeft, setAttemptsLeft] = useState(null);
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    useEffect(() => {
        // Check if redirected due to session timeout
        if (searchParams.get('timeout') === 'true') {
            setError('Your session has expired. Please log in again.');
        }
    }, [searchParams]);

    const validateEmail = (email) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setAttemptsLeft(null);

        // Validate email format
        if (!validateEmail(formData.email)) {
            setError('Please enter a valid email address');
            return;
        }

        // Validate password
        if (formData.password.length < 6) {
            setError('Password must be at least 6 characters');
            return;
        }

        setLoading(true);

        try {
            // Authenticate user
            const result = await authenticateUser(formData.email, formData.password);

            if (result.success) {
                // Store user data securely
                setCurrentUser(result.user);

                // Initialize session manager
                initSessionManager();

                // Notify header of auth change
                window.dispatchEvent(new Event('auth-change'));

                // Navigate to home
                navigate('/');
            } else {
                // Handle authentication failure
                setError(result.message);

                if (result.locked) {
                    // Account is locked
                    setAttemptsLeft(0);
                } else if (result.attemptsLeft !== undefined) {
                    // Show remaining attempts
                    setAttemptsLeft(result.attemptsLeft);
                }
            }
        } catch (err) {
            console.error('Login error:', err);
            setError('An unexpected error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const handleChange = (e) => {
        // Clear errors when user starts typing
        if (error) setError('');

        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    return (
        <div className="login-page grid-background">
            <div className="container">
                <div className="login-container">
                    <div className="login-card card">
                        <div className="login-header">
                            <h1>Welcome Back</h1>
                            <p>Please enter your details to sign in</p>
                        </div>

                        {error && (
                            <div className={`error-message ${attemptsLeft === 0 ? 'error-locked' : ''}`}>
                                <AlertCircle size={18} />
                                <span>{error}</span>
                            </div>
                        )}

                        {attemptsLeft !== null && attemptsLeft > 0 && (
                            <div className="warning-message">
                                <AlertCircle size={18} />
                                <span>
                                    {attemptsLeft} {attemptsLeft === 1 ? 'attempt' : 'attempts'} remaining before account lockout
                                </span>
                            </div>
                        )}

                        <form onSubmit={handleSubmit} className="login-form">
                            <div className="form-group">
                                <label htmlFor="email">Email Address</label>
                                <div className="input-wrapper">
                                    <Mail size={20} className="input-icon" />
                                    <input
                                        type="email"
                                        id="email"
                                        name="email"
                                        placeholder="name@gmail.com"
                                        value={formData.email}
                                        onChange={handleChange}
                                        autoComplete="email"
                                        required
                                        disabled={loading}
                                    />
                                </div>
                            </div>

                            <div className="form-group">
                                <label htmlFor="password">Password</label>
                                <div className="input-wrapper">
                                    <Lock size={20} className="input-icon" />
                                    <input
                                        type={showPassword ? 'text' : 'password'}
                                        id="password"
                                        name="password"
                                        placeholder="Password"
                                        value={formData.password}
                                        onChange={handleChange}
                                        autoComplete="current-password"
                                        required
                                        disabled={loading}
                                    />
                                    <button
                                        type="button"
                                        className="password-toggle"
                                        onClick={() => setShowPassword(!showPassword)}
                                        disabled={loading}
                                        aria-label="Toggle password visibility"
                                    >
                                        {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                                    </button>
                                </div>
                            </div>

                            <div className="form-options">
                                <label className="checkbox-label">
                                    <input type="checkbox" disabled={loading} />
                                    <span>Remember me</span>
                                </label>
                                <Link to="/forgot-password" className="forgot-link">
                                    Forgot password?
                                </Link>
                            </div>

                            <button
                                type="submit"
                                className="btn btn-primary btn-large"
                                disabled={loading}
                            >
                                {loading ? (
                                    <>
                                        <Loader size={20} className="spinner" />
                                        Signing in...
                                    </>
                                ) : (
                                    'Sign In'
                                )}
                            </button>
                        </form>

                        <div className="login-footer">
                            <p>Don't have an account? <Link to="/register">Sign up</Link></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
