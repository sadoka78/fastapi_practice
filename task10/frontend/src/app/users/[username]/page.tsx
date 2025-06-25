'use client';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'next/navigation';

interface Post {
  id: string;
  text: string;
  timestamp: string;
  owner_username: string;
}

const API_URL = 'http://localhost:8000/api';

export default function UserPostsPage() {
  const params = useParams<{ username: string }>();
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUserPosts = async () => {
      try {
        const res = await axios.get(`${API_URL}/users/${params.username}/posts`);
        setPosts(res.data);
      } catch (error) {
        console.error('Ошибка при загрузке постов пользователя:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchUserPosts();
  }, [params.username]);

  if (loading) return <p>Загрузка...</p>;

  return (
    <div className="container mx-auto max-w-2xl p-4">
      <h1 className="text-2xl font-bold mb-4">Посты пользователя: {params.username}</h1>
      {posts.length === 0 ? (
        <p>Нет постов.</p>
      ) : (
        <div className="space-y-4">
          {posts.map(post => (
            <div key={post.id} className="bg-white p-4 rounded-lg shadow">
              <p>{post.text}</p>
              <div className="text-xs text-gray-500 mt-2">{new Date(post.timestamp).toLocaleString()}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
