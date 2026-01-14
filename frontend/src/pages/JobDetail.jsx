import { useParams, Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, MapPin, Briefcase, DollarSign, Clock, Share2, X, CheckCircle } from 'lucide-react';
import { useState, useEffect } from 'react';
import { getCurrentUser } from '../utils/authUtils';
import JobCard from '../components/JobCard';
import Logo from '../components/Logo';
import { jobs } from '../data/jobs';
import './JobDetail.css';

const JobDetail = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const job = jobs.find(j => j.id === parseInt(id));
    const [showApplyModal, setShowApplyModal] = useState(false);
    const [showSuccessModal, setShowSuccessModal] = useState(false);
    const [hasApplied, setHasApplied] = useState(false);
    const [applicationData, setApplicationData] = useState({
        resume: null,
        coverLetter: ''
    });

    useEffect(() => {
        // Check if user has already applied to this job
        const appliedJobs = JSON.parse(localStorage.getItem('appliedJobs') || '[]');
        setHasApplied(appliedJobs.includes(parseInt(id)));
    }, [id]);

    if (!job) {
        return (
            <div className="container" style={{ padding: '3rem 0', textAlign: 'center' }}>
                <h2>Job not found</h2>
                <Link to="/jobs" className="btn btn-primary" style={{ marginTop: '1rem' }}>
                    Back to Jobs
                </Link>
            </div>
        );
    }

    const recommendedJobs = jobs.filter(j => j.id !== job.id).slice(0, 3);

    const handleApplyClick = () => {
        const user = getCurrentUser();
        if (!user) {
            navigate('/login');
        } else {
            setShowApplyModal(true);
        }
    };

    const handleSubmitApplication = (e) => {
        e.preventDefault();

        // Store application in localStorage
        const appliedJobs = JSON.parse(localStorage.getItem('appliedJobs') || '[]');
        if (!appliedJobs.includes(parseInt(id))) {
            appliedJobs.push(parseInt(id));
            localStorage.setItem('appliedJobs', JSON.stringify(appliedJobs));
        }

        // Store application details
        const applications = JSON.parse(localStorage.getItem('applications') || '[]');
        applications.push({
            jobId: parseInt(id),
            jobTitle: job.title,
            company: job.company,
            appliedDate: new Date().toISOString(),
            resume: applicationData.resume?.name || 'Resume uploaded',
            coverLetter: applicationData.coverLetter
        });
        localStorage.setItem('applications', JSON.stringify(applications));

        // Close apply modal and show success modal
        setShowApplyModal(false);
        setShowSuccessModal(true);
        setHasApplied(true);

        // Reset form
        setApplicationData({ resume: null, coverLetter: '' });

        // Auto-close success modal after 3 seconds
        setTimeout(() => {
            setShowSuccessModal(false);
        }, 3000);
    };

    return (
        <div className="job-detail">
            <div className="container">
                <Link to="/jobs" className="back-link">
                    <ArrowLeft size={16} />
                    Back to All Jobs
                </Link>

                <div className="job-detail-content">
                    <main className="job-main">
                        <div className="job-header-card card">
                            <div className="job-header-top">
                                <div className="job-company-logo-wrapper">
                                    <Logo className="job-company-logo" />
                                </div>
                                <div className="job-header-info">
                                    <h1>{job.title}</h1>
                                    <p className="job-sub-meta">
                                        {job.company} • {job.postedDate}
                                    </p>
                                </div>
                            </div>

                            <div className="job-meta-badges">
                                <span className="badge badge-salary">
                                    <DollarSign size={16} />
                                    {job.salary}
                                </span>
                                <span className="badge badge-type">
                                    <Briefcase size={16} />
                                    {job.employmentType}
                                </span>
                                <span className="badge badge-item">
                                    <MapPin size={16} />
                                    {job.location}
                                </span>
                                <span className="badge badge-item">
                                    <Clock size={16} />
                                    {job.experience}
                                </span>
                            </div>

                            <div className="job-actions">
                                {hasApplied ? (
                                    <button className="btn btn-success btn-large" disabled>
                                        <CheckCircle size={18} />
                                        Applied
                                    </button>
                                ) : (
                                    <button className="btn btn-primary btn-large" onClick={handleApplyClick}>
                                        Apply Now
                                    </button>
                                )}
                                <button className="btn btn-secondary btn-share">
                                    <Share2 size={18} />
                                    Share Job
                                </button>
                            </div>
                        </div>

                        <div className="job-description-card card">
                            <div className="section-pill">
                                <h2>Job Description</h2>
                            </div>
                            <p>{job.description}</p>

                            <div className="section-pill mt-3">
                                <h3>About the Role</h3>
                            </div>
                            <ul>
                                <li>Design and develop high-quality software solutions</li>
                                <li>Collaborate with cross-functional teams</li>
                                <li>Write clean, maintainable, and efficient code</li>
                                <li>Participate in code reviews and technical discussions</li>
                                <li>Stay up-to-date with emerging technologies</li>
                            </ul>

                            <div className="section-pill mt-3">
                                <h3>Requirements</h3>
                            </div>
                            <ul>
                                <li>Strong proficiency in required technologies</li>
                                <li>Excellent problem-solving skills</li>
                                <li>Good communication and teamwork abilities</li>
                                <li>Bachelor's degree in Computer Science or related field</li>
                                <li>Experience with version control systems (Git)</li>
                            </ul>

                            <div className="section-pill mt-3">
                                <h3>Required Skills</h3>
                            </div>
                            <div className="skills-list">
                                {job.skills.map((skill, index) => (
                                    <span key={index} className="skill-tag-large">{skill}</span>
                                ))}
                            </div>
                        </div>
                    </main>

                    <aside className="job-sidebar">
                        <div className="sidebar-card card">
                            <h3>Recommended for you</h3>
                            <div className="recommended-jobs">
                                {recommendedJobs.map(recJob => (
                                    <JobCard key={recJob.id} job={recJob} />
                                ))}
                            </div>
                        </div>
                    </aside>
                </div>
            </div>

            {/* Apply Modal */}
            {showApplyModal && (
                <div className="modal-overlay" onClick={() => setShowApplyModal(false)}>
                    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                        <div className="modal-header">
                            <h2>Apply for {job.title}</h2>
                            <button className="modal-close" onClick={() => setShowApplyModal(false)}>
                                <X size={24} />
                            </button>
                        </div>
                        <form onSubmit={handleSubmitApplication} className="apply-form">
                            <div className="form-group">
                                <label htmlFor="resume">Resume/CV *</label>
                                <div className="file-input-wrapper">
                                    <input
                                        type="file"
                                        id="resume"
                                        accept=".pdf,.doc,.docx"
                                        onChange={(e) => setApplicationData({ ...applicationData, resume: e.target.files[0] })}
                                        required
                                        className="file-input"
                                    />
                                    <div className="file-input-custom">
                                        <span className="file-name">
                                            {applicationData.resume ? applicationData.resume.name : 'Upload your resume (PDF, DOC, DOCX)'}
                                        </span>
                                        <span className="btn btn-secondary btn-sm">Browse</span>
                                    </div>
                                </div>
                            </div>

                            <div className="form-group">
                                <label htmlFor="coverLetter">Cover Letter</label>
                                <textarea
                                    id="coverLetter"
                                    rows="8"
                                    placeholder="Tell us why you're a great fit for this role..."
                                    value={applicationData.coverLetter}
                                    onChange={(e) => setApplicationData({ ...applicationData, coverLetter: e.target.value })}
                                />
                            </div>
                            <div className="modal-actions">
                                <button type="button" className="btn btn-secondary" onClick={() => setShowApplyModal(false)}>
                                    Cancel
                                </button>
                                <button type="submit" className="btn btn-primary">
                                    Submit Application
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}

            {/* Success Modal */}
            {showSuccessModal && (
                <div className="modal-overlay success-overlay">
                    <div className="modal-content success-modal">
                        <div className="success-icon">
                            <CheckCircle size={64} />
                        </div>
                        <h2>Application Submitted!</h2>
                        <p>Your application for <strong>{job.title}</strong> at <strong>{job.company}</strong> has been successfully submitted.</p>
                        <p className="success-subtext">We'll notify you once the employer reviews your application.</p>
                        <button
                            className="btn btn-primary"
                            onClick={() => setShowSuccessModal(false)}
                        >
                            Got it!
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default JobDetail;
