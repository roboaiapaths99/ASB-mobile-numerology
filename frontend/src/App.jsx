import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import InputSection from './components/InputSection';
import ResultsSection from './components/ResultsSection';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';

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

      if (!token) {
        redirectToLogin();
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
          logout();
        }
      } catch (err) {
        console.error('Auth verification failed:', err);
        logout();
      } finally {
        setAuthLoading(false);
      }
    };

    const redirectToLogin = () => {
      const currentUrl = window.location.origin + window.location.pathname;
      window.location.href = `${MAIN_SITE_URL}/login?redirect=${encodeURIComponent(currentUrl)}`;
    };

    const logout = () => {
      localStorage.removeItem('token');
      redirectToLogin();
    };

    checkAuth();
  }, []);

  const handleConsultation = async (formData) => {
    setLoading(true);
    setError(null);
    const token = localStorage.getItem('token');
    
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
          {user && (
            <div className="flex items-center gap-4">
              <span className="text-sm font-semibold text-purple-950">Hi, {user.name || 'User'}</span>
              <button 
                onClick={handleLogoutAction}
                className="text-xs font-bold text-red-500 hover:bg-red-50 px-3 py-1.5 rounded-lg border border-red-200 transition-colors"
              >
                Logout
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
    </div>
  );
}

export default App;
