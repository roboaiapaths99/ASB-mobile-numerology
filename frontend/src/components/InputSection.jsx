import React, { useState } from 'react';

const InputSection = ({ onSubmit, loading }) => {
  const [formData, setFormData] = useState({
    name: '',
    dob: '',
    mobile: '',
    challenges: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!formData.name || !formData.dob || !formData.mobile) {
      alert('Please fill in all required fields');
      return;
    }

    onSubmit(formData);
  };

  return (
    <div className="asb-card mb-8">
      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <label className="block text-sm font-medium text-asb-text mb-2">
              👤 Full Name
            </label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter your full name"
              className="input-field w-full"
              required
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-asb-text mb-2">
              📅 Date of Birth
            </label>
            <input
              type="date"
              name="dob"
              value={formData.dob}
              onChange={handleChange}
              className="input-field w-full"
              required
            />
          </div>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <label className="block text-sm font-medium text-asb-text mb-2">
              📱 Mobile Number
            </label>
            <input
              type="tel"
              name="mobile"
              value={formData.mobile}
              onChange={handleChange}
              placeholder="Enter your 10-digit mobile number"
              className="input-field w-full"
              pattern="[0-9]{10}"
              maxLength="10"
              required
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-asb-text mb-2">
              🎯 Current Challenges (Optional)
            </label>
            <textarea
              name="challenges"
              value={formData.challenges}
              onChange={handleChange}
              placeholder="Describe your current life challenges"
              className="input-field w-full resize-none"
              rows="3"
            />
          </div>
        </div>

        <div className="text-center">
          <button
            type="submit"
            disabled={loading}
            className="asb-button text-lg px-12 py-4 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? (
              <span className="flex items-center justify-center text-white">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Generating...
              </span>
            ) : (
              '🔮 Generate Numerology Consultation'
            )}
          </button>
        </div>
      </form>
    </div>
  );
};

export default InputSection;
