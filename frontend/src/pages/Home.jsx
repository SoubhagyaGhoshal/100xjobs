import { Link } from 'react-router-dom';
import { ArrowRight } from 'lucide-react';
import JobCard from '../components/JobCard';
import FAQ from '../components/FAQ';
import { jobs, companies } from '../data/jobs';
import './Home.css';

const Home = () => {
    const recentJobs = jobs.slice(0, 3);

    return (
        <div className="home">
            {/* Hero Section */}
            <section className="hero-section grid-background gradient-glow-top">
                <div className="container">
                    <div className="hero-content fade-in">
                        <span className="hero-badge badge-primary">#1 Platform for jobs</span>
                        <h1 className="hero-title">
                            Build Your
                            <span className="highlight-text">Career</span>
                            with 100xJobs
                        </h1>
                        <p className="hero-description">
                            Unlock exclusive job and internship opportunities. Remote, onsite, or hybrid—we've got what you're looking for.
                        </p>
                        <div className="hero-actions">
                            <Link to="/jobs" className="btn btn-primary">
                                Explore Jobs
                            </Link>
                            <a href="#testimonials" className="btn btn-secondary">
                                View Testimonials
                            </a>
                        </div>
                    </div>
                </div>
            </section>

            {/* Trusted By Section */}
            <section className="trusted-section">
                <div className="container">
                    <span className="trusted-badge">Trusted By Leading Companies</span>
                    <div className="companies-grid">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/8/8d/Adobe_Corporate_Logo.png" alt="Adobe" className="company-logo-img" />
                        <span className="company-logo-text">ATLASSIAN</span>
                        <span className="company-logo-text medium-logo">Medium</span>
                        <span className="company-logo-text">coinbase</span>
                        <span className="company-logo-text framer-logo">Framer</span>
                        <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google" className="company-logo-img" />
                    </div>
                </div>
            </section>

            {/* Recently Added Jobs */}
            <section className="recent-jobs-section">
                <div className="container">
                    <div className="section-header">
                        <div>
                            <h2>Recently Added jobs</h2>
                            <p style={{ color: 'var(--text-secondary)' }}>Stay ahead with newly added jobs</p>
                        </div>
                        <Link to="/jobs" className="btn btn-secondary">
                            View all jobs
                            <ArrowRight size={20} />
                        </Link>
                    </div>

                    <div className="jobs-grid">
                        {recentJobs.map(job => (
                            <JobCard key={job.id} job={job} />
                        ))}
                    </div>
                </div>
            </section>

            {/* Testimonials Section */}
            <section id="testimonials" className="testimonials-section">
                <div className="container">
                    <h2 className="text-center mb-2">Testimonials</h2>
                    <p className="text-center mb-4" style={{ color: 'var(--text-secondary)' }}>
                        Real Success Stories from Job Seekers and Employers
                    </p>

                    <div className="testimonials-grid">
                        {[
                            { name: "Sarah Chen", handle: "sarahc_dev", text: "Just landed my dream Senior Frontend role via 100xJobs! The platform's filtering made it so easy to find exactly what I was looking for. 🚀", avatar: "https://i.pravatar.cc/150?u=1" },
                            { name: "Alex Rivera", handle: "arivera_code", text: "The quality of job listings on 100xJobs is unmatched. No spam, just high-quality tech roles. Highly recommend for any dev looking for a switch.", avatar: "https://i.pravatar.cc/150?u=2" },
                            { name: "Jordan Smith", handle: "jsmith_pm", text: "As a Product Manager, I found the perfect remote opportunity here within a week. The UI is super clean and intuitive to use.", avatar: "https://i.pravatar.cc/150?u=3" }
                        ].map((item, index) => (
                            <div key={index} className="testimonial-card card">
                                <div className="testimonial-header">
                                    <img src={item.avatar} alt={item.name} className="testimonial-avatar-img" />
                                    <div className="testimonial-info">
                                        <div className="testimonial-user-row">
                                            <h4>{item.name}</h4>
                                            <span className="verified-badge">
                                                <svg viewBox="0 0 24 24" aria-label="Verified account" fill="currentColor" style={{ width: '18px', height: '18px', color: '#1d9bf0' }}><g><path d="M22.5 12.5c0-1.58-.875-2.95-2.148-3.6.154-.435.238-.905.238-1.4 0-2.21-1.71-3.998-3.818-3.998-.47 0-.92.084-1.336.25C14.818 2.415 13.51 1.5 12 1.5s-2.816.917-3.437 2.25c-.415-.165-.866-.25-1.336-.25-2.11 0-3.818 1.79-3.818 4 0 .495.083.965.237 1.4-1.272.65-2.147 2.018-2.147 3.6 0 1.495.782 2.798 1.942 3.486-.02.17-.032.34-.032.514 0 2.21 1.708 4 3.818 4 .47 0 .92-.086 1.335-.25.62 1.334 1.926 2.25 3.437 2.25 1.512 0 2.818-.916 3.437-2.25.415.163.865.248 1.336.248 2.11 0 3.818-1.79 3.818-4 0-.174-.012-.344-.033-.513 1.158-.687 1.943-1.99 1.943-3.484zm-6.616-3.334l-4.334 6.5c-.145.217-.382.334-.625.334-.143 0-.288-.04-.416-.126l-.115-.094-2.415-2.415c-.293-.293-.293-.768 0-1.06s.768-.294 1.06 0l1.77 1.767 3.825-5.74c.23-.345.696-.436 1.04-.207.346.23.44.696.21 1.04z"></path></g></svg>
                                            </span>
                                        </div>
                                        <p className="testimonial-handle">@{item.handle}</p>
                                    </div>
                                    <div className="testimonial-icon">
                                        <svg viewBox="0 0 24 24" aria-hidden="true" style={{ width: '20px', height: '20px', color: 'var(--text-muted)' }} fill="currentColor"><g><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"></path></g></svg>
                                    </div>
                                </div>
                                <p className="testimonial-text">
                                    {item.text}
                                </p>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* FAQ Section */}
            <FAQ />
        </div>
    );
};

export default Home;
