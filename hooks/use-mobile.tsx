// =============================================================================
// MOBILE DETECTION HOOK
// =============================================================================
// This custom hook detects if the current viewport is mobile-sized.
// Uses media queries to track screen size changes and provides responsive behavior.
// Useful for conditional rendering based on device type.

import * as React from "react"

// Breakpoint for mobile devices (768px and below)
const MOBILE_BREAKPOINT = 768

/**
 * Custom hook to detect if the current viewport is mobile-sized
 * Listens for window resize events and updates the mobile state accordingly
 * 
 * @returns Boolean indicating if the current viewport is mobile-sized
 */
export function useIsMobile() {
  // State to track mobile status (undefined initially for SSR compatibility)
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(undefined)

  React.useEffect(() => {
    // Create media query listener for mobile breakpoint
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)

    // Function to update mobile state based on window width
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    }

    // Add event listener for media query changes
    mql.addEventListener("change", onChange)

    // Set initial mobile state
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)

    // Cleanup event listener on unmount
    return () => mql.removeEventListener("change", onChange)
  }, [])

  return !!isMobile // Convert to boolean and return
}
