import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import InputSection from './components/InputSection';
import ResultsSection from './components/ResultsSection';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';
import Chatbot from './components/Chatbot';

function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [results, setResults] = useState(null);

  // SSO Auth State
  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);

  const MAIN_API_BASE = window.location.hostname.includes('asbreports.in')
    ? 'https://api.asbreports.in'
    : `http://${window.location.hostname}:8001`;

  const MAIN_SITE_URL = window.location.hostname.includes('asbreports.in')
    ? 'https://asbreports.in'
    : `http://${window.location.hostname}:3000`;

  useEffect(() => {
    const checkAuth = async () => {
      const params = new URLSearchParams(window.location.search);
      const urlToken = params.get('token');
      let token = localStorage.getItem('token');

      if (urlToken) {
        token = urlToken;
        localStorage.setItem('token', urlToken);
        const newUrl = window.location.origin + window.location.pathname;
        window.history.replaceState({}, document.title, newUrl);
      }

      // No token -> guest mode, don't redirect
      if (!token || token === 'null' || token === 'undefined') {
        localStorage.removeItem('token');
        setAuthLoading(false);
        return;
      }

      try {
        const response = await fetch(`${MAIN_API_BASE}/api/auth/me`, {
          headers: {
            'X-Auth-Token': token,
            'Authorization': `Bearer ${token}`
          }
        });
        const data = await response.json();
        if (data.success) {
          setUser(data.user);
        } else {
          // Invalid token — clear but stay in guest mode
          localStorage.removeItem('token');
        }
      } catch (err) {
        console.error('Auth verification failed:', err);
        // Network error — stay in guest mode
      } finally {
        setAuthLoading(false);
      }
    };

    checkAuth();
  }, []);

  const handleConsultation = async (formData) => {
    const token = localStorage.getItem('token');
    if (!token || token === 'null' || token === 'undefined') {
      localStorage.removeItem('token');
      localStorage.setItem('pending_mobile_consultation', JSON.stringify(formData));
      const currentUrl = window.location.origin + window.location.pathname;
      window.location.href = `${MAIN_SITE_URL}/login?redirect=${encodeURIComponent(currentUrl)}`;
      return;
    }

    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('/api/numerology/consultation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token || ''}`,
          'X-Auth-Token': token || '',
        },
        body: JSON.stringify(formData),
      });

      if (response.status === 401) {
        localStorage.removeItem('token');
        setUser(null);
        setError('Your session has expired. Redirecting to login...');
        setTimeout(() => {
          const currentUrl = window.location.origin + window.location.pathname;
          window.location.href = `${MAIN_SITE_URL}/login?redirect=${encodeURIComponent(currentUrl)}`;
        }, 1500);
        return;
      }

      if (!response.ok) {
        throw new Error('Failed to generate consultation');
      }

      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message || 'An error occurred while generating your consultation');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (user) {
      const pending = localStorage.getItem('pending_mobile_consultation');
      if (pending) {
        try {
          const pendingData = JSON.parse(pending);
          localStorage.removeItem('pending_mobile_consultation');
          handleConsultation(pendingData);
        } catch (e) {
          console.error('Failed to run pending mobile consultation:', e);
        }
      }
    }
  }, [user]);

  const handleLogoutAction = () => {
    localStorage.removeItem('token');
    const currentUrl = window.location.origin + window.location.pathname;
    window.location.href = `${MAIN_SITE_URL}/login?redirect=${encodeURIComponent(currentUrl)}`;
  };

  if (authLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-[#FDFBF7]">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-purple-600"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        <div className="flex justify-between items-center mb-6 border-b border-purple-100 pb-4">
          <a href={MAIN_SITE_URL} className="text-xs uppercase tracking-widest text-purple-600 font-bold hover:opacity-75 transition-opacity" style={{ textDecoration: 'none' }}>
            ← Back to Main Site
          </a>
          {user ? (
            <div className="flex items-center gap-4">
              <span className="text-sm font-semibold text-purple-950">Hi, {user.name || 'User'}</span>
              <button 
                onClick={handleLogoutAction}
                className="text-xs font-bold text-red-500 hover:bg-red-50 px-3 py-1.5 rounded-lg border border-red-200 transition-colors"
              >
                Logout
              </button>
            </div>
          ) : (
            <div className="flex items-center gap-4">
              <span className="text-sm font-semibold text-purple-950">Hi, Guest</span>
              <button 
                onClick={handleLogoutAction}
                className="text-xs font-bold text-purple-600 hover:bg-purple-50 px-3 py-1.5 rounded-lg border border-purple-200 transition-colors"
              >
                Login
              </button>
            </div>
          )}
        </div>
        <Header />
        <InputSection onSubmit={handleConsultation} loading={loading} />
        
        {loading && <LoadingSpinner />}
        
        {error && <ErrorMessage message={error} />}
        
        {results && !loading && <ResultsSection results={results} />}
      </div>
      <Chatbot user={user} token={localStorage.getItem('token')} />
    </div>
  );
}

export default App;
