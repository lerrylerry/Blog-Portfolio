// components/RightArrowIcon.tsx
import React from "react";

interface RightArrowIconProps {
  size?: number; // control the outer size
}

const RightArrowIcon: React.FC<RightArrowIconProps> = ({ size = 32 }) => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      role="img"
      aria-label="Right arrow"
      className="rounded-full inline mr-3"
    >
      {/* Indigo circular background */}
      <circle cx="12" cy="12" r="12" className="hover:fill-indigo-600 " />

      {/* Black arrow */}
      <path
        d="M8 12H16M12 8L16 12L12 16"
        stroke="white"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
};

export default RightArrowIcon;
