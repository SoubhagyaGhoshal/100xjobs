import { Link } from 'react-router-dom';
import { Youtube, Twitter } from 'lucide-react';
import './Footer.css';

const Footer = () => {
    return (
        <footer className="footer gradient-glow-bottom">
            <div className="container">
                <div className="footer-content">
                    <div className="footer-links">
                        <Link to="/about">About Us</Link>
                        <Link to="/terms">Terms of Service</Link>
                        <Link to="/privacy">Privacy Policy</Link>
                    </div>

                    <div className="footer-social">
                        <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
                            <Youtube size={20} />
                        </a>
                        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
                            <Twitter size={20} />
                        </a>
                    </div>
                </div>

                <div className="footer-copyright">
                    <p>© 2024 100xJobs. All rights reserved.</p>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
