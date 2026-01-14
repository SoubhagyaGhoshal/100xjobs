import bcrypt from 'bcryptjs';
import CryptoJS from 'crypto-js';

// Encryption key - in production, this should be more secure
const ENCRYPTION_KEY = 'your-secret-key-change-in-production';
const SALT_ROUNDS = 10;

// Rate limiting configuration
const MAX_LOGIN_ATTEMPTS = 5;
const LOCKOUT_DURATION = 15 * 60 * 1000; // 15 minutes in milliseconds

/**
 * Hash a password using bcrypt
 * @param {string} password - Plain text password
 * @returns {Promise<string>} - Hashed password
 */
export const hashPassword = async (password) => {
    try {
        const salt = await bcrypt.genSalt(SALT_ROUNDS);
        const hash = await bcrypt.hash(password, salt);
        return hash;
    } catch (error) {
        console.error('Error hashing password:', error);
        throw new Error('Failed to hash password');
    }
};

/**
 * Verify a password against a hash
 * @param {string} password - Plain text password
 * @param {string} hash - Hashed password
 * @returns {Promise<boolean>} - True if password matches
 */
export const verifyPassword = async (password, hash) => {
    try {
        return await bcrypt.compare(password, hash);
    } catch (error) {
        console.error('Error verifying password:', error);
        return false;
    }
};

/**
 * Encrypt data using AES
 * @param {any} data - Data to encrypt
 * @returns {string} - Encrypted string
 */
export const encryptData = (data) => {
    try {
        const jsonString = JSON.stringify(data);
        return CryptoJS.AES.encrypt(jsonString, ENCRYPTION_KEY).toString();
    } catch (error) {
        console.error('Error encrypting data:', error);
        throw new Error('Failed to encrypt data');
    }
};

/**
 * Decrypt data using AES
 * @param {string} encryptedData - Encrypted string
 * @returns {any} - Decrypted data
 */
export const decryptData = (encryptedData) => {
    try {
        const bytes = CryptoJS.AES.decrypt(encryptedData, ENCRYPTION_KEY);
        const decryptedString = bytes.toString(CryptoJS.enc.Utf8);
        return JSON.parse(decryptedString);
    } catch (error) {
        console.error('Error decrypting data:', error);
        return null;
    }
};

/**
 * Securely store data in localStorage with encryption
 * @param {string} key - Storage key
 * @param {any} data - Data to store
 */
export const secureStorage = {
    set: (key, data) => {
        try {
            const encrypted = encryptData(data);
            localStorage.setItem(key, encrypted);
        } catch (error) {
            console.error('Error storing data:', error);
        }
    },

    get: (key) => {
        try {
            const encrypted = localStorage.getItem(key);
            if (!encrypted) return null;
            return decryptData(encrypted);
        } catch (error) {
            console.error('Error retrieving data:', error);
            return null;
        }
    },

    remove: (key) => {
        localStorage.removeItem(key);
    },

    clear: () => {
        localStorage.clear();
    }
};

/**
 * Sanitize input to prevent XSS attacks
 * @param {string} input - User input
 * @returns {string} - Sanitized input
 */
export const sanitizeInput = (input) => {
    if (typeof input !== 'string') return input;

    return input
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
        .replace(/\//g, '&#x2F;');
};

/**
 * Generate a CSRF-like token
 * @returns {string} - Random token
 */
export const generateToken = () => {
    return CryptoJS.lib.WordArray.random(32).toString();
};

/**
 * Rate limiting for login attempts
 */
export const rateLimiter = {
    /**
     * Check if user is locked out
     * @param {string} identifier - User identifier (email)
     * @returns {Object} - { isLocked, remainingTime }
     */
    checkLockout: (identifier) => {
        const key = `lockout_${identifier}`;
        const lockoutData = secureStorage.get(key);

        if (!lockoutData) {
            return { isLocked: false, remainingTime: 0 };
        }

        const now = Date.now();
        const timeElapsed = now - lockoutData.lockedAt;

        if (timeElapsed >= LOCKOUT_DURATION) {
            // Lockout expired
            secureStorage.remove(key);
            return { isLocked: false, remainingTime: 0 };
        }

        const remainingTime = Math.ceil((LOCKOUT_DURATION - timeElapsed) / 1000 / 60);
        return { isLocked: true, remainingTime };
    },

    /**
     * Record a failed login attempt
     * @param {string} identifier - User identifier (email)
     * @returns {Object} - { attemptsLeft, isLocked }
     */
    recordFailedAttempt: (identifier) => {
        const key = `attempts_${identifier}`;
        const lockoutKey = `lockout_${identifier}`;
        const attemptData = secureStorage.get(key) || { count: 0, firstAttempt: Date.now() };

        const now = Date.now();
        const timeElapsed = now - attemptData.firstAttempt;

        // Reset if more than lockout duration has passed
        if (timeElapsed >= LOCKOUT_DURATION) {
            attemptData.count = 0;
            attemptData.firstAttempt = now;
        }

        attemptData.count += 1;
        secureStorage.set(key, attemptData);

        if (attemptData.count >= MAX_LOGIN_ATTEMPTS) {
            // Lock the account
            secureStorage.set(lockoutKey, { lockedAt: now });
            secureStorage.remove(key);
            return { attemptsLeft: 0, isLocked: true };
        }

        return {
            attemptsLeft: MAX_LOGIN_ATTEMPTS - attemptData.count,
            isLocked: false
        };
    },

    /**
     * Clear failed attempts on successful login
     * @param {string} identifier - User identifier (email)
     */
    clearAttempts: (identifier) => {
        secureStorage.remove(`attempts_${identifier}`);
        secureStorage.remove(`lockout_${identifier}`);
    }
};

/**
 * Register a new user
 * @param {Object} userData - User registration data
 * @returns {Promise<Object>} - { success, message, user }
 */
export const registerUser = async (userData) => {
    try {
        const { name, email, password } = userData;

        // Sanitize inputs
        const sanitizedName = sanitizeInput(name);
        const sanitizedEmail = sanitizeInput(email.toLowerCase());

        // Check if user already exists
        const existingUsers = secureStorage.get('users') || [];
        const userExists = existingUsers.some(user => user.email === sanitizedEmail);

        if (userExists) {
            return {
                success: false,
                message: 'An account with this email already exists'
            };
        }

        // Hash password
        const hashedPassword = await hashPassword(password);

        // Create user object
        const newUser = {
            id: generateToken(),
            name: sanitizedName,
            email: sanitizedEmail,
            password: hashedPassword,
            createdAt: new Date().toISOString()
        };

        // Store user
        existingUsers.push(newUser);
        secureStorage.set('users', existingUsers);

        // Return user without password
        const { password: _, ...userWithoutPassword } = newUser;

        return {
            success: true,
            message: 'Account created successfully',
            user: userWithoutPassword
        };
    } catch (error) {
        console.error('Registration error:', error);
        return {
            success: false,
            message: 'Failed to create account. Please try again.'
        };
    }
};

/**
 * Authenticate a user
 * @param {string} email - User email
 * @param {string} password - User password
 * @returns {Promise<Object>} - { success, message, user }
 */
export const authenticateUser = async (email, password) => {
    try {
        const sanitizedEmail = sanitizeInput(email.toLowerCase());

        // Check rate limiting
        const lockoutStatus = rateLimiter.checkLockout(sanitizedEmail);
        if (lockoutStatus.isLocked) {
            return {
                success: false,
                message: `Account locked. Please try again in ${lockoutStatus.remainingTime} minutes.`,
                locked: true
            };
        }

        // Get users
        const users = secureStorage.get('users') || [];
        const user = users.find(u => u.email === sanitizedEmail);

        if (!user) {
            // Record failed attempt
            const attemptResult = rateLimiter.recordFailedAttempt(sanitizedEmail);
            return {
                success: false,
                message: 'Invalid email or password',
                attemptsLeft: attemptResult.attemptsLeft
            };
        }

        // Verify password
        const isValidPassword = await verifyPassword(password, user.password);

        if (!isValidPassword) {
            // Record failed attempt
            const attemptResult = rateLimiter.recordFailedAttempt(sanitizedEmail);
            return {
                success: false,
                message: 'Invalid email or password',
                attemptsLeft: attemptResult.attemptsLeft
            };
        }

        // Clear failed attempts on successful login
        rateLimiter.clearAttempts(sanitizedEmail);

        // Return user without password
        const { password: _, ...userWithoutPassword } = user;

        return {
            success: true,
            message: 'Login successful',
            user: userWithoutPassword
        };
    } catch (error) {
        console.error('Authentication error:', error);
        return {
            success: false,
            message: 'An error occurred. Please try again.'
        };
    }
};

/**
 * Get current logged-in user
 * @returns {Object|null} - User object or null
 */
export const getCurrentUser = () => {
    return secureStorage.get('currentUser');
};

/**
 * Set current logged-in user
 * @param {Object} user - User object
 */
export const setCurrentUser = (user) => {
    secureStorage.set('currentUser', user);
    secureStorage.set('lastActivity', Date.now());
};

/**
 * Logout current user
 */
export const logoutUser = () => {
    secureStorage.remove('currentUser');
    secureStorage.remove('lastActivity');
    secureStorage.remove('sessionToken');
};
