import React from 'react';

const Header = () => {
  return (
    <div className="header-section">
      <h1 className="header-title animate-cosmic-float text-asb-purple flex flex-col md:flex-row items-center justify-center gap-2 font-semibold">
        <img
          src="/images/cb4c8e26-4cfb-407c-be4c-3e65d19edaa5-Photoroom.png"
          alt="ASB Logo"
          className="header-logo object-contain"
        />
        ASB mobile numerology
      </h1>
      <p className="text-shadow-glow text-asb-text-muted text-sm sm:text-base">Discover Your Divine Numerological Blueprint</p>
    </div>
  );
};

export default Header;
