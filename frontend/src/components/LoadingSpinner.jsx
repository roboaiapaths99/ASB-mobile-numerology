import React from 'react';

const LoadingSpinner = () => {
  return (
    <div className="flex justify-center items-center py-12">
      <div className="text-center">
        <div className="loading-spinner mx-auto mb-4"></div>
        <p className="text-asb-text font-medium">Generating your numerology consultation...</p>
      </div>
    </div>
  );
};

export default LoadingSpinner;
