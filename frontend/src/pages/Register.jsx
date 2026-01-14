import { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Mail, Lock, User, Eye, EyeOff, AlertCircle, CheckCircle, Loader } from 'lucide-react';
import { registerUser, setCurrentUser } from '../utils/authUtils';
import { calculatePasswordStrength, validatePassword, getStrengthColor } from '../utils/passwordValidator';
import { initSessionManager } from '../utils/sessionManager';
import './Login.css';

const Register = () => {
    const navigate = useNavigate();
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [passwordStrength, setPasswordStrength] = useState({ score: 0, strength: 'none', feedback: [] });
    const [passwordErrors, setPasswordErrors] = useState([]);
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        confirmPassword: ''
    });

    // Calculate password strength on password change
    useEffect(() => {
        if (formData.password) {
            const strength = calculatePasswordStrength(formData.password);
            setPasswordStrength(strength);

            const validation = validatePassword(formData.password);
            setPasswordErrors(validation.errors);
        } else {
            setPasswordStrength({ score: 0, strength: 'none', feedback: [] });
            setPasswordErrors([]);
        }
    }, [formData.password]);

    const validateEmail = (email) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        // Validate name
        if (formData.name.trim().length < 2) {
            setError('Please enter your full name');
            return;
        }

        // Validate email
        if (!validateEmail(formData.email)) {
            setError('Please enter a valid email address');
            return;
        }

        // Validate password
        const passwordValidation = validatePassword(formData.password);
        if (!passwordValidation.isValid) {
            setError(passwordValidation.errors[0]);
            return;
        }

        // Check password match
        if (formData.password !== formData.confirmPassword) {
            setError('Passwords do not match');
            return;
        }

        setLoading(true);

        try {
            // Register user
            const result = await registerUser({
                name: formData.name,
                email: formData.email,
                password: formData.password
            });

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
                setError(result.message);
            }
        } catch (err) {
            console.error('Registration error:', err);
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
                            <h1>Create Account</h1>
                            <p>Sign up to start your job search journey</p>
                        </div>

                        {error && (
                            <div className="error-message">
                                <AlertCircle size={18} />
                                <span>{error}</span>
                            </div>
                        )}

                        <form onSubmit={handleSubmit} className="login-form">
                            <div className="form-group">
                                <label htmlFor="name">Full Name</label>
                                <div className="input-wrapper">
                                    <User size={20} className="input-icon" />
                                    <input
                                        type="text"
                                        id="name"
                                        name="name"
                                        placeholder="Enter your full name"
                                        value={formData.name}
                                        onChange={handleChange}
                                        autoComplete="name"
                                        required
                                        disabled={loading}
                                    />
                                </div>
                            </div>

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
                                        placeholder="Create a password"
                                        value={formData.password}
                                        onChange={handleChange}
                                        autoComplete="new-password"
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

                                {formData.password && (
                                    <div className="password-strength-container">
                                        <div className="password-strength-bar">
                                            <div
                                                className="password-strength-fill"
                                                style={{
                                                    width: `${passwordStrength.score}%`,
                                                    backgroundColor: getStrengthColor(passwordStrength.strength)
                                                }}
                                            />
                                        </div>
                                        <div className="password-strength-label">
                                            <span style={{ color: getStrengthColor(passwordStrength.strength) }}>
                                                {passwordStrength.strength === 'weak' && 'Weak password'}
                                                {passwordStrength.strength === 'medium' && 'Medium password'}
                                                {passwordStrength.strength === 'strong' && 'Strong password'}
                                            </span>
                                        </div>

                                        {passwordErrors.length > 0 && (
                                            <div className="password-requirements">
                                                {passwordErrors.map((err, idx) => (
                                                    <div key={idx} className="requirement-item error">
                                                        <AlertCircle size={14} />
                                                        <span>{err}</span>
                                                    </div>
                                                ))}
                                            </div>
                                        )}

                                        {passwordErrors.length === 0 && formData.password.length >= 8 && (
                                            <div className="password-requirements">
                                                <div className="requirement-item success">
                                                    <CheckCircle size={14} />
                                                    <span>All requirements met</span>
                                                </div>
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>

                            <div className="form-group">
                                <label htmlFor="confirmPassword">Confirm Password</label>
                                <div className="input-wrapper">
                                    <Lock size={20} className="input-icon" />
                                    <input
                                        type={showConfirmPassword ? 'text' : 'password'}
                                        id="confirmPassword"
                                        name="confirmPassword"
                                        placeholder="Confirm your password"
                                        value={formData.confirmPassword}
                                        onChange={handleChange}
                                        autoComplete="new-password"
                                        required
                                        disabled={loading}
                                    />
                                    <button
                                        type="button"
                                        className="password-toggle"
                                        onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                                        disabled={loading}
                                        aria-label="Toggle confirm password visibility"
                                    >
                                        {showConfirmPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                                    </button>
                                </div>

                                {formData.confirmPassword && formData.password !== formData.confirmPassword && (
                                    <div className="password-requirements">
                                        <div className="requirement-item error">
                                            <AlertCircle size={14} />
                                            <span>Passwords do not match</span>
                                        </div>
                                    </div>
                                )}

                                {formData.confirmPassword && formData.password === formData.confirmPassword && (
                                    <div className="password-requirements">
                                        <div className="requirement-item success">
                                            <CheckCircle size={14} />
                                            <span>Passwords match</span>
                                        </div>
                                    </div>
                                )}
                            </div>

                            <button
                                type="submit"
                                className="btn btn-primary btn-large"
                                disabled={loading}
                            >
                                {loading ? (
                                    <>
                                        <Loader size={20} className="spinner" />
                                        Creating account...
                                    </>
                                ) : (
                                    'Create Account'
                                )}
                            </button>
                        </form>

                        <div className="login-footer">
                            <p>Already have an account? <Link to="/login">Sign in</Link></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Register;
