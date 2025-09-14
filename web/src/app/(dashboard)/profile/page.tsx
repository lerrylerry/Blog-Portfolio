"use client";
import { useEffect, useState } from "react";
import { API_URL } from "@/lib/api";

export default function ProfilePage() {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    const token = localStorage.getItem("access");
    if (!token) return;

    fetch(`${API_URL}/api/accounts/profile/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => res.json())
      .then(setUser)
      .catch(console.error);
  }, []);

  if (!user) return <p className="mt-10 text-center">Loading...</p>;

  return (
    <div className="max-w-sm mx-auto mt-10">
      <h1 className="text-xl font-bold">Profile</h1>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
    </div>
  );
}