// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================
// This file contains utility functions used throughout the application.
// Includes CSS class merging utilities for Tailwind CSS integration.

import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

/**
 * Utility function to merge CSS classes with proper conflict resolution
 * Combines clsx for conditional classes and twMerge for Tailwind CSS class merging
 * 
 * @param inputs - Array of class values (strings, objects, arrays, etc.)
 * @returns Merged class string with resolved conflicts
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
