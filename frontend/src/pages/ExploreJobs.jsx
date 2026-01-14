import { useState } from 'react';
import { Search, SlidersHorizontal, ChevronDown, ChevronUp } from 'lucide-react';
import JobCard from '../components/JobCard';
import { jobs } from '../data/jobs';
import './ExploreJobs.css';

const ExploreJobs = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [filters, setFilters] = useState({
        employmentType: [],
        workMode: [],
        salaryRange: [],
        experience: [],
        city: []
    });
    const [expandedGroups, setExpandedGroups] = useState({
        employmentType: true,
        workMode: true,
        salaryRange: true,
        experience: true,
        city: true
    });
    const [sortBy, setSortBy] = useState('recent');

    const parseSalary = (salaryStr) => {
        if (!salaryStr) return { min: 0, max: 0 };
        const clean = salaryStr.toLowerCase().replace(/k/g, '000').replace(/£/g, '').replace(/\$/g, '');
        if (clean.includes('or above') || clean.includes('+')) {
            return { min: parseInt(clean), max: Infinity };
        }
        const [min, max] = clean.split('-').map(val => parseInt(val.trim()));
        return { min: min || 0, max: max || Infinity };
    };

    const checkSalaryMatch = (jobSalary, filterRanges) => {
        if (filterRanges.length === 0) return true;

        const jobRange = parseSalary(jobSalary);

        return filterRanges.some(range => {
            const filterRange = parseSalary(range);
            // Check for overlap
            return (jobRange.min <= filterRange.max && jobRange.max >= filterRange.min);
        });
    };

    const filteredJobs = jobs.filter(job => {
        const matchesSearch = job.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
            job.company.toLowerCase().includes(searchQuery.toLowerCase());

        const matchesEmploymentType = filters.employmentType.length === 0 ||
            filters.employmentType.includes(job.employmentType);

        // Map "Office" filter to "onsite" data value if needed, or just match lowercase
        const matchesWorkMode = filters.workMode.length === 0 ||
            filters.workMode.some(mode => {
                if (mode === 'Office') return job.workMode === 'onsite';
                return job.workMode.toLowerCase() === mode.toLowerCase();
            });

        const matchesSalary = checkSalaryMatch(job.salary, filters.salaryRange);

        const matchesExp = filters.experience.length === 0 ||
            filters.experience.includes(job.experience);

        const matchesCity = filters.city.length === 0 ||
            filters.city.some(city => job.location.includes(city));

        return matchesSearch && matchesEmploymentType && matchesWorkMode && matchesSalary && matchesExp && matchesCity;
    });

    const toggleGroup = (group) => {
        setExpandedGroups(prev => ({ ...prev, [group]: !prev[group] }));
    };

    const handleFilterChange = (filterType, value) => {
        setFilters(prev => {
            if (Array.isArray(prev[filterType])) {
                const newValues = prev[filterType].includes(value)
                    ? prev[filterType].filter(v => v !== value)
                    : [...prev[filterType], value];
                return { ...prev, [filterType]: newValues };
            }
            return { ...prev, [filterType]: value };
        });
    };

    return (
        <div className="explore-jobs grid-background">
            <div className="container">
                <div className="explore-header">
                    <h1>Explore Jobs</h1>
                    <p>Explore thousands of remote and onsite jobs that match your skills and aspirations.</p>
                </div>

                <div className="explore-content">
                    {/* Sidebar Filters */}
                    <aside className="filters-sidebar">
                        <div className="filters-header">
                            <h3>
                                <SlidersHorizontal size={20} />
                                All Filters
                            </h3>
                        </div>

                        {/* Employment Type */}
                        <div className="filter-group">
                            <button className="filter-group-header" onClick={() => toggleGroup('employmentType')}>
                                <h4>Employment Type</h4>
                                {expandedGroups.employmentType ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                            </button>
                            {expandedGroups.employmentType && (
                                <div className="filter-options slide-down">
                                    {['Full Time', 'Part Time', 'Contract', 'Internship'].map(type => (
                                        <label key={type} className="filter-checkbox">
                                            <input
                                                type="checkbox"
                                                checked={filters.employmentType.includes(type)}
                                                onChange={() => handleFilterChange('employmentType', type)}
                                            />
                                            <span>{type}</span>
                                        </label>
                                    ))}
                                </div>
                            )}
                        </div>

                        {/* Work Mode */}
                        <div className="filter-group">
                            <button className="filter-group-header" onClick={() => toggleGroup('workMode')}>
                                <h4>Work Mode</h4>
                                {expandedGroups.workMode ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                            </button>
                            {expandedGroups.workMode && (
                                <div className="filter-options slide-down">
                                    {['Remote', 'Hybrid', 'Office'].map(mode => (
                                        <label key={mode} className="filter-checkbox">
                                            <input
                                                type="checkbox"
                                                checked={filters.workMode.includes(mode)}
                                                onChange={() => handleFilterChange('workMode', mode)}
                                            />
                                            <span>{mode}</span>
                                        </label>
                                    ))}
                                </div>
                            )}
                        </div>

                        {/* Salary Range */}
                        <div className="filter-group">
                            <button className="filter-group-header" onClick={() => toggleGroup('salaryRange')}>
                                <h4>Salary Range</h4>
                                {expandedGroups.salaryRange ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                            </button>
                            {expandedGroups.salaryRange && (
                                <div className="filter-options slide-down">
                                    {['$0-$50k', '$50k-$100k', '$100k-$150k', '$150k or above'].map(range => (
                                        <label key={range} className="filter-checkbox">
                                            <input
                                                type="checkbox"
                                                checked={filters.salaryRange.includes(range)}
                                                onChange={() => handleFilterChange('salaryRange', range)}
                                            />
                                            <span>{range}</span>
                                        </label>
                                    ))}
                                </div>
                            )}
                        </div>

                        {/* City */}
                        <div className="filter-group">
                            <button className="filter-group-header" onClick={() => toggleGroup('city')}>
                                <h4>City</h4>
                                {expandedGroups.city ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                            </button>
                            {expandedGroups.city && (
                                <div className="filter-options slide-down">
                                    {['Remote', 'San Francisco', 'New York', 'Austin', 'Seattle', 'Boston', 'London'].map(city => (
                                        <label key={city} className="filter-checkbox">
                                            <input
                                                type="checkbox"
                                                checked={filters.city.includes(city)}
                                                onChange={() => handleFilterChange('city', city)}
                                            />
                                            <span>{city}</span>
                                        </label>
                                    ))}
                                </div>
                            )}
                        </div>
                    </aside>

                    {/* Main Content */}
                    <main className="jobs-main">
                        <div className="search-bar-container">
                            <div className="search-bar">
                                <Search size={20} />
                                <input
                                    type="text"
                                    placeholder="Search by title or company name"
                                    value={searchQuery}
                                    onChange={(e) => setSearchQuery(e.target.value)}
                                />
                            </div>
                            <select
                                value={sortBy}
                                onChange={(e) => setSortBy(e.target.value)}
                                className="sort-select"
                            >
                                <option value="recent">Most Recent</option>
                                <option value="salary">Highest Salary</option>
                                <option value="company">Company A-Z</option>
                            </select>
                        </div>

                        <div className="jobs-count">
                            <p>{filteredJobs.length} jobs found</p>
                        </div>

                        <div className="jobs-list">
                            {filteredJobs.map(job => (
                                <JobCard key={job.id} job={job} />
                            ))}
                        </div>

                        {filteredJobs.length === 0 && (
                            <div className="no-jobs">
                                <p>No jobs found matching your criteria</p>
                            </div>
                        )}
                    </main>
                </div>
            </div>
        </div>
    );
};

export default ExploreJobs;
