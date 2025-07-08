// =============================================================================
// API CLIENT FUNCTIONS
// =============================================================================
// This file contains all the API functions that communicate with the backend server.
// Each function handles a specific API endpoint and includes proper error handling.

// Base URL for the backend API server
export const API_URL = "http://localhost:8000";

// =============================================================================
// AUTHENTICATION API FUNCTIONS
// =============================================================================

/**
 * Register a new user account
 * @param email - User's email address
 * @param password - User's password
 * @returns Promise with user data
 */
export async function signup({ email, password }: { email: string; password: string }) {
    const res = await fetch(`${API_URL}/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
    });
    if (!res.ok) throw new Error((await res.json()).detail || "Signup failed");
    return res.json();
}

/**
 * Authenticate user and get access token
 * @param email - User's email address
 * @param password - User's password
 * @returns Promise with access token
 */
export async function login({ email, password }: { email: string; password: string }) {
    const form = new URLSearchParams();
    form.append("username", email);
    form.append("password", password);
    const res = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: form,
    });
    if (!res.ok) throw new Error((await res.json()).detail || "Login failed");
    return res.json();
}

/**
 * Get current user's profile information
 * @param token - JWT access token
 * @returns Promise with user data
 */
export async function getMe(token: string) {
    const res = await fetch(`${API_URL}/me`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Not authenticated");
    return res.json();
}

// =============================================================================
// QUIZ API FUNCTIONS
// =============================================================================

/**
 * Get quiz questions for a specific subject and level
 * @param subjectId - Subject ID (1=Python, 2=ML, 3=JS, 4=C)
 * @param levelId - Level ID within the subject
 * @returns Promise with quiz data
 */
export async function getQuiz(subjectId: number, levelId: number) {
    const res = await fetch(`${API_URL}/quiz/${subjectId}/${levelId}`);
    if (!res.ok) throw new Error("Quiz not found");
    return res.json();
}

/**
 * Submit quiz answers and get results
 * @param subjectId - Subject ID
 * @param levelId - Level ID
 * @param answers - Object with question IDs as keys and selected answers as values
 * @param token - Optional JWT token for authenticated users
 * @returns Promise with quiz results and score
 */
export async function submitQuiz(subjectId: number, levelId: number, answers: Record<number, string>, token?: string) {
    const headers: any = { "Content-Type": "application/json" };
    if (token) headers["Authorization"] = `Bearer ${token}`;
    const res = await fetch(`${API_URL}/quiz/${subjectId}/${levelId}/submit`, {
        method: "POST",
        headers,
        body: JSON.stringify(answers),
    });
    if (!res.ok) throw new Error("Quiz submission failed");
    return res.json();
}

// =============================================================================
// GENERAL DATA API FUNCTIONS
// =============================================================================

/**
 * Get leaderboard data with user rankings
 * @param period - Time period for leaderboard (default: "all-time")
 * @returns Promise with leaderboard data
 */
export async function getLeaderboard(period: string = "all-time") {
    const res = await fetch(`${API_URL}/leaderboard?period=${period}`);
    if (!res.ok) throw new Error("Leaderboard not found");
    return res.json();
}

/**
 * Get all available subjects
 * @returns Promise with subjects list
 */
export async function getSubjects() {
    const res = await fetch(`${API_URL}/subjects`);
    if (!res.ok) throw new Error("Failed to fetch subjects");
    return res.json();
}

/**
 * Get specific subject details
 * @param subjectId - Subject ID
 * @returns Promise with subject data
 */
export async function getSubject(subjectId: number) {
    const res = await fetch(`${API_URL}/subjects/${subjectId}`);
    if (!res.ok) throw new Error("Subject not found");
    return res.json();
}

/**
 * Get dashboard statistics and data
 * @returns Promise with dashboard data
 */
export async function getDashboardData() {
    const res = await fetch(`${API_URL}/dashboard-data`);
    if (!res.ok) throw new Error("Failed to fetch dashboard data");
    return res.json();
}

// =============================================================================
// USER-SPECIFIC API FUNCTIONS
// =============================================================================

/**
 * Get user's subjects with progress data
 * @param token - JWT access token
 * @returns Promise with user's subjects and progress
 */
export async function getUserSubjects(token: string) {
    const res = await fetch(`${API_URL}/user/subjects`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch user subjects");
    return res.json();
}

/**
 * Update user's progress for a specific subject
 * @param subjectId - Subject ID
 * @param completedQuizzes - Number of completed quizzes
 * @param token - JWT access token
 * @returns Promise with updated progress
 */
export async function updateUserProgress(subjectId: number, completedQuizzes: number, token: string) {
    const res = await fetch(`${API_URL}/user/subjects/${subjectId}/progress`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify({ completed_quizzes: completedQuizzes }),
    });
    if (!res.ok) throw new Error("Failed to update progress");
    return res.json();
}

/**
 * Mark a quiz level as completed for the user
 * @param subjectId - Subject ID
 * @param levelId - Level ID
 * @param token - JWT access token
 * @returns Promise with completion status
 */
export async function completeQuizLevel(subjectId: number, levelId: number, token: string) {
    const res = await fetch(`${API_URL}/user/subjects/${subjectId}/levels/${levelId}/complete`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to mark quiz as completed");
    return res.json();
}

/**
 * Get user's activity history
 * @param token - JWT access token
 * @returns Promise with user activity data
 */
export async function getUserActivity(token: string) {
    const res = await fetch(`${API_URL}/user/activity`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch user activity");
    return res.json();
}

/**
 * Get user's statistics and performance data
 * @param token - JWT access token
 * @returns Promise with user stats
 */
export async function getUserStats(token: string) {
    const res = await fetch(`${API_URL}/user/stats`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch user stats");
    return res.json();
}

/**
 * Get total number of students in the platform
 * @returns Promise with student count
 */
export async function getTotalStudents() {
    const res = await fetch(`${API_URL}/total-students`);
    if (!res.ok) throw new Error("Failed to fetch total students count");
    return res.json();
}

/**
 * Save a user goal
 * @param goal - Goal data
 * @param token - JWT access token
 * @returns Promise with saved goal
 */
export async function saveUserGoal(goal: any, token: string) {
    const res = await fetch(`${API_URL}/user/goals`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify(goal),
    });
    if (!res.ok) throw new Error("Failed to save goal");
    return res.json();
}

/**
 * Fetch user goals
 * @param token - JWT access token
 * @returns Promise with user goals
 */
export async function getUserGoals(token: string) {
    const res = await fetch(`${API_URL}/user/goals`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch goals");
    return res.json();
}

/**
 * Send a challenge to a friend
 * @param challenge - Challenge data
 * @param token - JWT access token
 * @returns Promise with challenge info
 */
export async function sendChallenge(challenge: any, token: string) {
    const res = await fetch(`${API_URL}/user/challenge`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify(challenge),
    });
    if (!res.ok) throw new Error("Failed to send challenge");
    return res.json();
}

/**
 * Fetch challenges for the current user
 * @param token - JWT access token
 * @returns Promise with challenges
 */
export async function getUserChallenges(token: string) {
    const res = await fetch(`${API_URL}/user/challenges`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch challenges");
    return res.json();
}

// =============================================================================
// ADMIN API FUNCTIONS
// =============================================================================
// These functions require admin privileges and are used in the admin panel

/**
 * Get all users with their progress data (admin only)
 * @param token - JWT access token (must be admin)
 * @returns Promise with all users data
 */
export async function getAllUsers(token: string) {
    const res = await fetch(`${API_URL}/admin/users`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch users");
    return res.json();
}

/**
 * Get detailed progress for a specific user (admin only)
 * @param userId - User ID to get progress for
 * @param token - JWT access token (must be admin)
 * @returns Promise with user's detailed progress
 */
export async function getUserProgress(userId: number, token: string) {
    const res = await fetch(`${API_URL}/admin/user/${userId}/progress`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch user progress");
    return res.json();
}

/**
 * Delete a user account (admin only)
 * @param userId - User ID to delete
 * @param token - JWT access token (must be admin)
 * @returns Promise with deletion status
 */
export async function deleteUser(userId: number, token: string) {
    const res = await fetch(`${API_URL}/admin/user/${userId}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to delete user");
    return res.json();
}

/**
 * Create a new admin user (admin only)
 * @param userData - User data (email, password, name)
 * @param token - JWT access token (must be admin)
 * @returns Promise with created user data
 */
export async function createAdminUser(userData: { email: string; password: string; name: string }, token: string) {
    const res = await fetch(`${API_URL}/admin/create-admin`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify(userData),
    });
    if (!res.ok) throw new Error("Failed to create admin user");
    return res.json();
}

/**
 * Add a new subject to the platform (admin only)
 * @param subject - Subject data
 * @param token - JWT access token (must be admin)
 * @returns Promise with added subject data
 */
export async function addSubject(subject: any, token: string) {
    const res = await fetch(`${API_URL}/admin/add-subject`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify(subject),
    });
    if (!res.ok) throw new Error("Failed to add subject");
    return res.json();
}

/**
 * Add a new level to a subject (admin only)
 * @param data - Level data including subject ID
 * @param token - JWT access token (must be admin)
 * @returns Promise with added level data
 */
export async function addLevel(data: any, token: string) {
    const res = await fetch(`${API_URL}/admin/add-level`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error("Failed to add level");
    return res.json();
}

/**
 * Reset a user's progress (admin only)
 * @param userId - User ID to reset
 * @param token - JWT access token (must be admin)
 * @returns Promise with reset status
 */
export async function resetUserProgress(userId: number, token: string) {
    const res = await fetch(`${API_URL}/admin/reset-user-progress/${userId}`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to reset user progress");
    return res.json();
} 