import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import { faqs } from '../data/jobs';
import './FAQ.css';

const FAQ = () => {
    const [openIndex, setOpenIndex] = useState(null);

    const toggleFAQ = (index) => {
        setOpenIndex(openIndex === index ? null : index);
    };

    return (
        <section className="faq-section">
            <div className="container">
                <h2 className="text-center mb-3">Frequently Asked Questions</h2>
                <p className="text-center mb-4" style={{ color: 'var(--text-secondary)' }}>
                    Quick answers to any questions you may have.
                </p>

                <div className="faq-list">
                    {faqs.map((faq, index) => (
                        <div key={index} className="faq-item card">
                            <button
                                className="faq-question"
                                onClick={() => toggleFAQ(index)}
                            >
                                <span>{faq.question}</span>
                                <ChevronDown
                                    className={`faq-icon ${openIndex === index ? 'rotated' : ''}`}
                                    size={20}
                                />
                            </button>
                            {openIndex === index && (
                                <div className="faq-answer slide-down">
                                    {faq.answer}
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default FAQ;
