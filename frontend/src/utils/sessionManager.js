import { secureStorage, logoutUser } from './authUtils';

// Session configuration
const SESSION_TIMEOUT = 30 * 60 * 1000; // 30 minutes in milliseconds
const WARNING_TIME = 2 * 60 * 1000; // Show warning 2 minutes before timeout

let timeoutId = null;
let warningTimeoutId = null;
let warningCallback = null;

/**
 * Update last activity timestamp
 */
const updateActivity = () => {
    secureStorage.set('lastActivity', Date.now());
};

/**
 * Check if session has expired
 * @returns {boolean} - True if session expired
 */
export const isSessionExpired = () => {
    const lastActivity = secureStorage.get('lastActivity');
    if (!lastActivity) return true;

    const now = Date.now();
    const elapsed = now - lastActivity;

    return elapsed >= SESSION_TIMEOUT;
};

/**
 * Get remaining session time in seconds
 * @returns {number} - Remaining time in seconds
 */
export const getRemainingTime = () => {
    const lastActivity = secureStorage.get('lastActivity');
    if (!lastActivity) return 0;

    const now = Date.now();
    const elapsed = now - lastActivity;
    const remaining = SESSION_TIMEOUT - elapsed;

    return Math.max(0, Math.floor(remaining / 1000));
};

/**
 * Handle session timeout
 */
const handleTimeout = () => {
    logoutUser();
    window.dispatchEvent(new CustomEvent('session-timeout'));
    window.location.href = '/login?timeout=true';
};

/**
 * Handle warning before timeout
 */
const handleWarning = () => {
    if (warningCallback) {
        warningCallback(getRemainingTime());
    }
    window.dispatchEvent(new CustomEvent('session-warning', {
        detail: { remainingTime: getRemainingTime() }
    }));
};

/**
 * Reset session timers
 */
const resetTimers = () => {
    // Clear existing timers
    if (timeoutId) clearTimeout(timeoutId);
    if (warningTimeoutId) clearTimeout(warningTimeoutId);

    // Update activity
    updateActivity();

    // Set warning timer
    warningTimeoutId = setTimeout(handleWarning, SESSION_TIMEOUT - WARNING_TIME);

    // Set timeout timer
    timeoutId = setTimeout(handleTimeout, SESSION_TIMEOUT);
};

/**
 * Initialize session manager
 * @param {Function} onWarning - Callback for warning event
 */
export const initSessionManager = (onWarning) => {
    warningCallback = onWarning;

    // Check if session already expired
    if (isSessionExpired()) {
        handleTimeout();
        return;
    }

    // Set up activity listeners
    const events = ['mousedown', 'keydown', 'scroll', 'touchstart', 'click'];

    const activityHandler = () => {
        resetTimers();
    };

    events.forEach(event => {
        document.addEventListener(event, activityHandler, true);
    });

    // Initial timer setup
    resetTimers();

    // Return cleanup function
    return () => {
        events.forEach(event => {
            document.removeEventListener(event, activityHandler, true);
        });
        if (timeoutId) clearTimeout(timeoutId);
        if (warningTimeoutId) clearTimeout(warningTimeoutId);
    };
};

/**
 * Extend session (reset timers)
 */
export const extendSession = () => {
    resetTimers();
};

/**
 * End session manually
 */
export const endSession = () => {
    if (timeoutId) clearTimeout(timeoutId);
    if (warningTimeoutId) clearTimeout(warningTimeoutId);
    logoutUser();
};
