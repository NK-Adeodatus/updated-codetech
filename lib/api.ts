export const API_URL = "http://localhost:8000";

export async function signup({ email, password }: { email: string; password: string }) {
    const res = await fetch(`${API_URL}/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
    });
    if (!res.ok) throw new Error((await res.json()).detail || "Signup failed");
    return res.json();
}

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

export async function getMe(token: string) {
    const res = await fetch(`${API_URL}/me`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Not authenticated");
    return res.json();
}

export async function getQuiz(subjectId: number, levelId: number) {
    const res = await fetch(`${API_URL}/quiz/${subjectId}/${levelId}`);
    if (!res.ok) throw new Error("Quiz not found");
    return res.json();
}

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

export async function getLeaderboard(period: string = "all-time") {
    const res = await fetch(`${API_URL}/leaderboard?period=${period}`);
    if (!res.ok) throw new Error("Leaderboard not found");
    return res.json();
}

export async function getSubjects() {
    const res = await fetch(`${API_URL}/subjects`);
    if (!res.ok) throw new Error("Failed to fetch subjects");
    return res.json();
}

export async function getSubject(subjectId: number) {
    const res = await fetch(`${API_URL}/subjects/${subjectId}`);
    if (!res.ok) throw new Error("Subject not found");
    return res.json();
}

export async function getDashboardData() {
    const res = await fetch(`${API_URL}/dashboard-data`);
    if (!res.ok) throw new Error("Failed to fetch dashboard data");
    return res.json();
}

export async function getUserSubjects(token: string) {
    const res = await fetch(`${API_URL}/user/subjects`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch user subjects");
    return res.json();
}

export async function updateUserProgress(subjectId: number, completedQuizzes: number, token: string) {
    const res = await fetch(`${API_URL}/user/subjects/${subjectId}/progress`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify({ completed_quizzes: completedQuizzes }),
    });
    if (!res.ok) throw new Error("Failed to update progress");
    return res.json();
}

export async function completeQuizLevel(subjectId: number, levelId: number, token: string) {
    const res = await fetch(`${API_URL}/user/subjects/${subjectId}/levels/${levelId}/complete`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to mark quiz as completed");
    return res.json();
}

export async function getUserActivity(token: string) {
    const res = await fetch(`${API_URL}/user/activity`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch user activity");
    return res.json();
}

export async function getUserStats(token: string) {
    const res = await fetch(`${API_URL}/user/stats`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) throw new Error("Failed to fetch user stats");
    return res.json();
} 