// =============================================================================
// ADMIN PANEL PAGE COMPONENT
// =============================================================================
// This page provides administrative functionality for managing the platform.
// Includes user management, subject/level creation, and progress monitoring.
// Restricted to users with admin role only.

"use client"

// Import React hooks for state management and side effects
import { useState, useEffect } from "react"
// Import UI components from the design system
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
// Import API functions for admin operations
import { getSubjects, getAllUsers, getUserProgress, addSubject, addLevel, deleteUser, createAdminUser, resetUserProgress } from "@/lib/api"
// Import Next.js routing components
import { useRouter } from "next/navigation"
// Import API function for user authentication
import { getMe } from "@/lib/api"

export default function AdminPage() {
    // State management for subjects and levels
    const [subjects, setSubjects] = useState<any[]>([]) // All subjects in the system
    const [subjectName, setSubjectName] = useState("") // New subject name input
    const [subjectDesc, setSubjectDesc] = useState("") // New subject description input
    const [addSubjectMsg, setAddSubjectMsg] = useState("") // Success/error message for subject creation
    const [levelSubjectId, setLevelSubjectId] = useState("") // Selected subject ID for new level
    const [levelName, setLevelName] = useState("") // New level name input
    const [levelDesc, setLevelDesc] = useState("") // New level description input
    const [addLevelMsg, setAddLevelMsg] = useState("") // Success/error message for level creation

    // State management for user management
    const [users, setUsers] = useState<any[]>([]) // All users in the system
    const [selectedUser, setSelectedUser] = useState<any>(null) // Currently selected user for progress view
    const [userProgress, setUserProgress] = useState<any>(null) // Progress data for selected user

    // General state management
    const [loading, setLoading] = useState(true) // Loading state for data fetching
    const [error, setError] = useState("") // Error message state

    // Create admin form state
    const [showCreateAdmin, setShowCreateAdmin] = useState(false) // Toggle admin creation form
    const [adminFormData, setAdminFormData] = useState({
        email: "",
        password: "",
        name: ""
    }) // Form data for new admin user
    const [createAdminMsg, setCreateAdminMsg] = useState("") // Success/error message for admin creation

    const router = useRouter() // Next.js router for navigation

    // Effect hook to verify admin access and load admin data
    useEffect(() => {
        const token = localStorage.getItem("authToken")
        if (!token) {
            router.push("/login") // Redirect to login if no token found
            return
        }

        // Verify user is admin before allowing access
        getMe(token)
            .then((user) => {
                if (user.role !== "admin") {
                    setError("Access denied. Admin privileges required.") // Show error for non-admin users
                    return
                }
                loadAdminData(token) // Load admin data if user is admin
            })
            .catch(() => {
                localStorage.removeItem("authToken") // Clear invalid token
                router.push("/login") // Redirect to login
            })
    }, [router])

    const loadAdminData = async (token: string) => {
        try {
            const [subjectsData, usersData] = await Promise.all([
                getSubjects(),
                getAllUsers(token)
            ])
            setSubjects(subjectsData)
            setUsers(usersData)
        } catch (err: any) {
            setError(err.message || "Failed to load admin data")
        } finally {
            setLoading(false)
        }
    }

    const handleAddSubject = async (e: any) => {
        e.preventDefault()
        setAddSubjectMsg("")
        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            await addSubject({
                name: subjectName,
                description: subjectDesc,
                icon: "📚",
                color: "bg-gray-500",
                levels: [],
                totalQuizzes: 0,
            }, token)
            setAddSubjectMsg("Subject added!")
            setSubjectName("")
            setSubjectDesc("")
            // Reload subjects
            const subjectsData = await getSubjects()
            setSubjects(subjectsData)
        } catch (err: any) {
            setAddSubjectMsg(err.message || "Failed to add subject.")
        }
    }

    const handleAddLevel = async (e: any) => {
        e.preventDefault()
        setAddLevelMsg("")
        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            await addLevel({
                subject_id: Number(levelSubjectId),
                level: {
                    name: levelName,
                    description: levelDesc,
                    quizzes: 0,
                    completedQuizzes: 0,
                    estimatedTime: "1 hour",
                    topics: [],
                },
            }, token)
            setAddLevelMsg("Level added!")
            setLevelName("")
            setLevelDesc("")
            // Reload subjects
            const subjectsData = await getSubjects()
            setSubjects(subjectsData)
        } catch (err: any) {
            setAddLevelMsg(err.message || "Failed to add level.")
        }
    }

    const handleViewUserProgress = async (user: any) => {
        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            const progress = await getUserProgress(user.id, token)
            setSelectedUser(user)
            setUserProgress(progress)
        } catch (err: any) {
            console.error("Failed to load user progress:", err)
        }
    }

    const handleDeleteUser = async (user: any) => {
        // Check if this is the protected creator admin
        if (user.email === "AdminIbra@gmail.com") {
            alert("Cannot delete the original creator admin account. This account is protected.")
            return
        }

        const isAdmin = user.role === "admin"
        const confirmMessage = isAdmin
            ? `Are you sure you want to delete ADMIN user ${user.email}? This action cannot be undone and will remove admin privileges.`
            : `Are you sure you want to delete user ${user.email}? This action cannot be undone.`

        if (!confirm(confirmMessage)) {
            return
        }

        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            await deleteUser(user.id, token)
            // Reload users list
            const usersData = await getAllUsers(token)
            setUsers(usersData)
            alert("User deleted successfully")
        } catch (err: any) {
            alert(err.message || "Failed to delete user")
        }
    }

    const handleResetUserProgress = async (user: any) => {
        if (!window.confirm(`Are you sure you want to reset progress for user ${user.email}? This will erase all their progress and stats.`)) {
            return;
        }
        const token = localStorage.getItem("authToken")
        if (!token) return
        try {
            await resetUserProgress(user.id, token)
            // Reload users list
            const usersData = await getAllUsers(token)
            setUsers(usersData)
            alert("User progress reset successfully")
        } catch (err: any) {
            alert(err.message || "Failed to reset user progress")
        }
    }

    const handleCreateAdmin = async (e: any) => {
        e.preventDefault()
        setCreateAdminMsg("")

        const token = localStorage.getItem("authToken")
        if (!token) return

        try {
            await createAdminUser(adminFormData, token)
            setCreateAdminMsg("Admin user created successfully!")
            setAdminFormData({ email: "", password: "", name: "" })
            setShowCreateAdmin(false)
            // Reload users list
            const usersData = await getAllUsers(token)
            setUsers(usersData)
        } catch (err: any) {
            setCreateAdminMsg(err.message || "Failed to create admin user")
        }
    }

    if (loading) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
                <div className="text-center">Loading admin panel...</div>
            </div>
        )
    }

    if (error) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 flex items-center justify-center">
                <div className="text-center text-red-600">{error}</div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100">
            <div className="container mx-auto py-12 px-4">
                <h1 className="text-3xl font-bold mb-8">Admin Dashboard</h1>

                <div className="grid md:grid-cols-2 gap-8 mb-12">
                    <Card>
                        <CardHeader>
                            <CardTitle>Add New Subject</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form onSubmit={handleAddSubject} className="space-y-4">
                                <Input
                                    placeholder="Subject Name"
                                    value={subjectName}
                                    onChange={e => setSubjectName(e.target.value)}
                                    required
                                />
                                <Input
                                    placeholder="Description"
                                    value={subjectDesc}
                                    onChange={e => setSubjectDesc(e.target.value)}
                                    required
                                />
                                <Button type="submit">Add Subject</Button>
                                {addSubjectMsg && <div className="text-sm mt-2">{addSubjectMsg}</div>}
                            </form>
                        </CardContent>
                    </Card>
                    <Card>
                        <CardHeader>
                            <CardTitle>Add Level to Subject</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form onSubmit={handleAddLevel} className="space-y-4">
                                <select
                                    className="w-full border rounded p-2"
                                    value={levelSubjectId}
                                    onChange={e => setLevelSubjectId(e.target.value)}
                                    required
                                >
                                    <option value="">Select Subject</option>
                                    {subjects.map((s) => (
                                        <option key={s.id} value={s.id}>{s.name}</option>
                                    ))}
                                </select>
                                <Input
                                    placeholder="Level Name"
                                    value={levelName}
                                    onChange={e => setLevelName(e.target.value)}
                                    required
                                />
                                <Input
                                    placeholder="Level Description"
                                    value={levelDesc}
                                    onChange={e => setLevelDesc(e.target.value)}
                                    required
                                />
                                <Button type="submit">Add Level</Button>
                                {addLevelMsg && <div className="text-sm mt-2">{addLevelMsg}</div>}
                            </form>
                        </CardContent>
                    </Card>
                </div>

                {/* Create Admin Section */}
                <div className="mt-12">
                    <div className="flex justify-between items-center mb-4">
                        <h2 className="text-2xl font-bold">Admin Management</h2>
                        <Button onClick={() => setShowCreateAdmin(true)}>
                            Add New Admin
                        </Button>
                    </div>

                    {showCreateAdmin && (
                        <Card className="mb-6">
                            <CardHeader>
                                <CardTitle>Create New Admin User</CardTitle>
                            </CardHeader>
                            <CardContent>
                                <form onSubmit={handleCreateAdmin} className="space-y-4">
                                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                        <Input
                                            placeholder="Email"
                                            type="email"
                                            value={adminFormData.email}
                                            onChange={(e) => setAdminFormData({ ...adminFormData, email: e.target.value })}
                                            required
                                        />
                                        <Input
                                            placeholder="Password"
                                            type="password"
                                            value={adminFormData.password}
                                            onChange={(e) => setAdminFormData({ ...adminFormData, password: e.target.value })}
                                            required
                                        />
                                        <Input
                                            placeholder="Name (Optional)"
                                            value={adminFormData.name}
                                            onChange={(e) => setAdminFormData({ ...adminFormData, name: e.target.value })}
                                        />
                                    </div>
                                    <div className="flex space-x-2">
                                        <Button type="submit">Create Admin</Button>
                                        <Button type="button" variant="outline" onClick={() => setShowCreateAdmin(false)}>
                                            Cancel
                                        </Button>
                                    </div>
                                    {createAdminMsg && (
                                        <div className={`text-sm mt-2 ${createAdminMsg.includes("successfully") ? "text-green-600" : "text-red-600"}`}>
                                            {createAdminMsg}
                                        </div>
                                    )}
                                </form>
                            </CardContent>
                        </Card>
                    )}
                </div>

                {/* Users Table */}
                <div className="mt-12">
                    <h2 className="text-2xl font-bold mb-4">Registered Users</h2>
                    <div className="overflow-x-auto">
                        <table className="min-w-full bg-white border border-slate-200 rounded-lg">
                            <thead>
                                <tr>
                                    <th className="px-4 py-2 border-b">ID</th>
                                    <th className="px-4 py-2 border-b">Email</th>
                                    <th className="px-4 py-2 border-b">Name</th>
                                    <th className="px-4 py-2 border-b">Role</th>
                                    <th className="px-4 py-2 border-b">Completed Quizzes</th>
                                    <th className="px-4 py-2 border-b">Avg Score</th>
                                    <th className="px-4 py-2 border-b">Last Activity</th>
                                    <th className="px-4 py-2 border-b">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {users.map((user: any) => (
                                    <tr key={user.id}>
                                        <td className="px-4 py-2 border-b text-center">{user.id}</td>
                                        <td className="px-4 py-2 border-b">{user.email}</td>
                                        <td className="px-4 py-2 border-b">{user.name || "N/A"}</td>
                                        <td className="px-4 py-2 border-b">
                                            <Badge variant={user.role === "admin" ? "destructive" : "secondary"}>
                                                {user.role}
                                            </Badge>
                                        </td>
                                        <td className="px-4 py-2 border-b text-center">{user.total_completed}</td>
                                        <td className="px-4 py-2 border-b text-center">{user.avg_score.toFixed(1)}%</td>
                                        <td className="px-4 py-2 border-b text-sm">
                                            {user.last_activity ? new Date(user.last_activity).toLocaleDateString() : "Never"}
                                        </td>
                                        <td className="px-4 py-2 border-b">
                                            <div className="flex space-x-2">
                                                <Button
                                                    size="sm"
                                                    variant="outline"
                                                    onClick={() => handleViewUserProgress(user)}
                                                >
                                                    View Progress
                                                </Button>
                                                <Button
                                                    size="sm"
                                                    variant="secondary"
                                                    onClick={() => handleResetUserProgress(user)}
                                                >
                                                    Reset Progress
                                                </Button>
                                                {user.email !== "AdminIbra@gmail.com" && (
                                                    <Button
                                                        size="sm"
                                                        variant="destructive"
                                                        onClick={() => handleDeleteUser(user)}
                                                    >
                                                        Delete User
                                                    </Button>
                                                )}
                                            </div>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                        {users.length === 0 && <div className="text-slate-500 mt-4">No users found.</div>}
                    </div>
                </div>

                {/* User Progress Modal */}
                {selectedUser && userProgress && (
                    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
                        <div className="bg-white rounded-lg p-6 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
                            <div className="flex justify-between items-center mb-4">
                                <h3 className="text-xl font-bold">
                                    Progress for {selectedUser.email}
                                </h3>
                                <Button onClick={() => setSelectedUser(null)}>Close</Button>
                            </div>

                            <div className="grid md:grid-cols-2 gap-6">
                                <div>
                                    <h4 className="font-semibold mb-3">Subject Progress</h4>
                                    {userProgress.subjects.map((subject: any) => (
                                        <div key={subject.id} className="mb-4 p-3 border rounded">
                                            <div className="flex justify-between items-center mb-2">
                                                <span className="font-medium">{subject.name}</span>
                                                <span className="text-sm text-slate-600">
                                                    {subject.completed}/{subject.total} quizzes
                                                </span>
                                            </div>
                                            <Progress value={subject.percentage} className="mb-2" />
                                            <div className="text-sm text-slate-600">
                                                {subject.percentage}% complete
                                            </div>
                                        </div>
                                    ))}
                                </div>

                                <div>
                                    <h4 className="font-semibold mb-3">Recent Activity</h4>
                                    <div className="space-y-2">
                                        {userProgress.recent_activities.map((activity: any, index: number) => (
                                            <div key={index} className="p-2 border rounded text-sm">
                                                <div className="font-medium">{activity.action}</div>
                                                <div className="text-slate-600">
                                                    {new Date(activity.timestamp).toLocaleString()}
                                                </div>
                                                {activity.score && (
                                                    <div className="text-green-600">
                                                        Score: {activity.score}%
                                                    </div>
                                                )}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    )
} 