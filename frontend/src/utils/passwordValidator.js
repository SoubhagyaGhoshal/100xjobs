// Password strength validation utility

// Common passwords to blacklist
const COMMON_PASSWORDS = [
    'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567',
    'letmein', 'trustno1', 'dragon', 'baseball', 'iloveyou', 'master', 'sunshine',
    'ashley', 'bailey', 'passw0rd', 'shadow', '123123', '654321', 'superman',
    'qazwsx', 'michael', 'football', 'password1', 'welcome', 'jesus', 'ninja'
];

/**
 * Calculate password strength score (0-100)
 * @param {string} password - The password to evaluate
 * @returns {Object} - { score, strength, feedback }
 */
export const calculatePasswordStrength = (password) => {
    if (!password) {
        return { score: 0, strength: 'none', feedback: [] };
    }

    let score = 0;
    const feedback = [];

    // Length check (0-30 points)
    if (password.length >= 8) {
        score += 10;
    } else {
        feedback.push('Use at least 8 characters');
    }

    if (password.length >= 12) {
        score += 10;
    }

    if (password.length >= 16) {
        score += 10;
    }

    // Character variety (0-40 points)
    if (/[a-z]/.test(password)) {
        score += 10;
    } else {
        feedback.push('Add lowercase letters');
    }

    if (/[A-Z]/.test(password)) {
        score += 10;
    } else {
        feedback.push('Add uppercase letters');
    }

    if (/[0-9]/.test(password)) {
        score += 10;
    } else {
        feedback.push('Add numbers');
    }

    if (/[^a-zA-Z0-9]/.test(password)) {
        score += 10;
    } else {
        feedback.push('Add special characters (!@#$%^&*)');
    }

    // Pattern checks (0-30 points)
    // Check for sequential characters
    const hasSequential = /(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|012|123|234|345|456|567|678|789)/i.test(password);
    if (!hasSequential) {
        score += 10;
    } else {
        feedback.push('Avoid sequential characters');
    }

    // Check for repeated characters
    const hasRepeated = /(.)\1{2,}/.test(password);
    if (!hasRepeated) {
        score += 10;
    } else {
        feedback.push('Avoid repeated characters');
    }

    // Check against common passwords
    const isCommon = COMMON_PASSWORDS.some(common =>
        password.toLowerCase().includes(common)
    );
    if (!isCommon) {
        score += 10;
    } else {
        feedback.push('Avoid common passwords');
    }

    // Determine strength level
    let strength;
    if (score < 40) {
        strength = 'weak';
    } else if (score < 70) {
        strength = 'medium';
    } else {
        strength = 'strong';
    }

    return { score, strength, feedback };
};

/**
 * Validate password meets minimum requirements
 * @param {string} password - The password to validate
 * @returns {Object} - { isValid, errors }
 */
export const validatePassword = (password) => {
    const errors = [];

    if (!password) {
        errors.push('Password is required');
        return { isValid: false, errors };
    }

    if (password.length < 8) {
        errors.push('Password must be at least 8 characters long');
    }

    if (!/[a-z]/.test(password)) {
        errors.push('Password must contain at least one lowercase letter');
    }

    if (!/[A-Z]/.test(password)) {
        errors.push('Password must contain at least one uppercase letter');
    }

    if (!/[0-9]/.test(password)) {
        errors.push('Password must contain at least one number');
    }

    if (!/[^a-zA-Z0-9]/.test(password)) {
        errors.push('Password must contain at least one special character');
    }

    return {
        isValid: errors.length === 0,
        errors
    };
};

/**
 * Get password strength color for UI
 * @param {string} strength - 'weak', 'medium', or 'strong'
 * @returns {string} - CSS color value
 */
export const getStrengthColor = (strength) => {
    switch (strength) {
        case 'weak':
            return '#ef4444'; // red
        case 'medium':
            return '#f59e0b'; // orange
        case 'strong':
            return '#10b981'; // green
        default:
            return '#6b7280'; // gray
    }
};
