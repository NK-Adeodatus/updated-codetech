#!/usr/bin/env python3
"""
Simple test script to verify the API endpoints are working
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test if the server is running"""
    try:
        response = requests.get(f"{BASE_URL}/docs")
        print("✅ Server is running")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the backend server first.")
        return False

def test_signup():
    """Test user signup"""
    data = {
        "email": "test@example.com",
        "password": "testpassword",
        "name": "Test User"
    }
    try:
        response = requests.post(f"{BASE_URL}/signup", json=data)
        if response.status_code == 200:
            print("✅ Signup endpoint working")
            return response.json()
        else:
            print(f"❌ Signup failed: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Signup error: {e}")
        return None

def test_login():
    """Test user login"""
    data = {
        "username": "AdminIbra@gmail.com",
        "password": "IbraGold@1"
    }
    try:
        response = requests.post(f"{BASE_URL}/login", data=data)
        if response.status_code == 200:
            print("✅ Login endpoint working")
            return response.json()
        else:
            print(f"❌ Login failed: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return None

def test_admin_endpoints(token):
    """Test admin endpoints"""
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test get all users
    try:
        response = requests.get(f"{BASE_URL}/admin/users", headers=headers)
        if response.status_code == 200:
            users = response.json()
            print(f"✅ Admin users endpoint working - Found {len(users)} users")
            return True
        else:
            print(f"❌ Admin users failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Admin users error: {e}")
        return False

def test_quiz_endpoints():
    """Test quiz endpoints"""
    try:
        response = requests.get(f"{BASE_URL}/quiz/1/1")
        if response.status_code == 200:
            quiz = response.json()
            print(f"✅ Quiz endpoint working - Quiz: {quiz.get('title', 'Unknown')}")
            return True
        else:
            print(f"❌ Quiz endpoint failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Quiz endpoint error: {e}")
        return False

def test_subjects_endpoint():
    """Test subjects endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/subjects")
        if response.status_code == 200:
            subjects = response.json()
            print(f"✅ Subjects endpoint working - Found {len(subjects)} subjects")
            return True
        else:
            print(f"❌ Subjects endpoint failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Subjects endpoint error: {e}")
        return False

def main():
    print("🧪 Testing CodeTech API...")
    print("=" * 50)
    
    # Test server health
    if not test_health():
        return
    
    # Test basic endpoints
    test_subjects_endpoint()
    test_quiz_endpoints()
    
    # Test authentication
    login_result = test_login()
    if login_result:
        token = login_result.get("access_token")
        if token:
            test_admin_endpoints(token)
    
    print("=" * 50)
    print("✅ API testing completed!")

if __name__ == "__main__":
    main() 