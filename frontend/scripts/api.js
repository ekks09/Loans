const API_BASE_URL = window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')
    ? 'http://localhost:3000'
    : window.location.origin;

const API = {
    getToken() {
        return localStorage.getItem('access_token');
    },

    getRefreshToken() {
        return localStorage.getItem('refresh_token');
    },

    isAuthenticated() {
        return !!this.getToken();
    },

    async request(endpoint, options = {}) {
        const url = `${API_BASE_URL}${endpoint}`;
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers
        };

        if (this.getToken() && !options.noAuth) {
            headers['Authorization'] = `Bearer ${this.getToken()}`;
        }

        try {
            const response = await fetch(url, {
                ...options,
                headers
            });

            if (response.status === 401 && !options.isRetry) {
                const refreshed = await this.refreshToken();
                if (refreshed) {
                    return this.request(endpoint, { ...options, isRetry: true });
                } else {
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('refresh_token');
                    window.location.href = 'login.html';
                    throw new Error('Session expired. Please login again.');
                }
            }

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'An error occurred');
            }

            return data;
        } catch (error) {
            if (error.name === 'TypeError' && error.message === 'Failed to fetch') {
                throw new Error('Unable to connect to server. Please check your connection.');
            }
            throw error;
        }
    },

    async refreshToken() {
        const refreshToken = this.getRefreshToken();
        if (!refreshToken) return false;

        try {
            const response = await fetch(`${API_BASE_URL}/api/auth/refresh`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ refresh_token: refreshToken })
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('access_token', data.access_token);
                localStorage.setItem('refresh_token', data.refresh_token);
                return true;
            }
            return false;
        } catch {
            return false;
        }
    },

    async register(phone, idNumber, password) {
        return this.request('/api/auth/register', {
            method: 'POST',
            body: JSON.stringify({ phone, id_number: idNumber, password }),
            noAuth: true
        });
    },

    async login(phone, password) {
        return this.request('/api/auth/login', {
            method: 'POST',
            body: JSON.stringify({ phone, password }),
            noAuth: true
        });
    },

    async getMe() {
        return this.request('/api/auth/me');
    },

    async getLoanPreview(principal) {
        return this.request('/api/loans/preview', {
            method: 'POST',
            body: JSON.stringify({ principal })
        });
    },

    async applyLoan(amount) {
        return this.request('/api/loans/apply', {
            method: 'POST',
            body: JSON.stringify({ amount })
        });
    },

    async getLoanHistory() {
        return this.request('/api/loans/history');
    },

    async getLoan(loanId) {
        return this.request(`/api/loans/${loanId}`);
    },

    async initializePayment(loanId, callbackUrl = null) {
        const body = { loan_id: loanId };
        if (callbackUrl) {
            body.callback_url = callbackUrl;
        }
        return this.request('/api/payments/initialize', {
            method: 'POST',
            body: JSON.stringify(body)
        });
    },

    async verifyPayment(reference) {
        return this.request(`/api/payments/verify/${reference}`);
    },

    async getTransactions() {
        return this.request('/api/payments/transactions');
    }
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = API;
}
