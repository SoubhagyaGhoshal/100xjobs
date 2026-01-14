import { Link } from 'react-router-dom';
import { MapPin, Briefcase, DollarSign, Clock } from 'lucide-react';
import Logo from './Logo';
import './JobCard.css';

const JobCard = ({ job }) => {
    return (
        <Link to={`/jobs/${job.id}`} className="job-card card">
            <div className="job-card-header">
                <div className="company-logo-wrapper">
                    <Logo className="company-logo" />
                </div>
                <div className="job-info">
                    <h3 className="job-title">{job.title}</h3>
                    <p className="company-name">{job.company}</p>
                    <p className="posted-date">Posted on {job.postedDate}</p>
                </div>
            </div>

            <div className="job-meta">
                <span className="badge badge-type">
                    <Briefcase size={14} />
                    {job.employmentType}
                </span>
                <span className="badge badge-salary">
                    <DollarSign size={14} />
                    {job.salary}
                </span>
                <span className="badge badge-exp">
                    <Clock size={14} />
                    {job.experience}
                </span>
                <span className="badge badge-loc">
                    <MapPin size={14} />
                    {job.location} - {job.workMode}
                </span>
            </div>

            <div className="job-skills">
                {job.skills.slice(0, 6).map((skill, index) => (
                    <span key={index} className="skill-tag">{skill}</span>
                ))}
                {job.skills.length > 6 && (
                    <span className="skill-tag">+{job.skills.length - 6} more</span>
                )}
            </div>
        </Link>
    );
};

export default JobCard;
