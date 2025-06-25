'use client';

import { useState, useEffect, ChangeEvent, FormEvent } from 'react';
import axios from 'axios';
import Image from 'next/image';
import { Trash2 } from 'lucide-react';  // Иконка корзины (если используешь lucide-react, или замени на любую другую)

const API_URL = 'http://localhost:8000';

export default function Home() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [images, setImages] = useState<string[]>([]);
  const [error, setError] = useState('');
  const [uploading, setUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState<number>(0);

  const fetchImages = async () => {
    try {
      const response = await axios.get(`${API_URL}/api/images`);
      setImages(response.data);
    } catch (err) {
      console.error('Ошибка при получении изображений:', err);
      setError('Не удалось загрузить галерею.');
    }
  };

  useEffect(() => {
    fetchImages();
  }, []);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
      setError('');
    }
  };

  const handleUpload = async (e: FormEvent) => {
    e.preventDefault();
    if (!selectedFile) {
      setError('Пожалуйста, выберите файл.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    setUploading(true);
    setUploadProgress(0);
    setError('');

    try {
      await axios.post(`${API_URL}/api/upload`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (progressEvent) => {
          if (progressEvent.total) {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            setUploadProgress(percentCompleted);
          }
        },
      });

      setSelectedFile(null);
      setUploadProgress(0);
      fetchImages();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Ошибка при загрузке файла.');
    } finally {
      setUploading(false);
    }
  };

  const handleDelete = async (imgUrl: string) => {
    const filename = imgUrl.split('/').pop();
    if (!filename) return;

    try {
      await axios.delete(`${API_URL}/api/images/${filename}`);
      setImages((prev) => prev.filter((url) => url !== imgUrl));
    } catch (err) {
      console.error('Ошибка при удалении:', err);
      setError('Не удалось удалить изображение.');
    }
  };

  return (
    <main className="container mx-auto p-8">
      <h1 className="text-4xl font-bold text-center mb-8">Галерея Изображений</h1>

      <form onSubmit={handleUpload} className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md mb-12">
        <div className="mb-4">
          <label htmlFor="file-upload" className="block text-gray-700 text-sm font-bold mb-2">
            Выберите изображение:
          </label>
          <input
            id="file-upload"
            type="file"
            onChange={handleFileChange}
            accept="image/*"
            className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
          />
        </div>

        {uploading && (
          <div className="w-full bg-gray-200 rounded-full h-4 mb-4">
            <div
              className="bg-blue-500 h-4 rounded-full transition-all duration-300"
              style={{ width: `${uploadProgress}%` }}
            ></div>
          </div>
        )}

        <button
          type="submit"
          disabled={!selectedFile || uploading}
          className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded disabled:bg-gray-400"
        >
          {uploading ? `Загрузка... ${uploadProgress}%` : 'Загрузить'}
        </button>

        {error && <p className="text-red-500 text-xs italic mt-4">{error}</p>}
      </form>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {images.map((imgUrl, index) => (
          <div key={index} className="relative aspect-square rounded-lg overflow-hidden shadow-lg group">
            <Image
              src={
                imgUrl.startsWith('http://') || imgUrl.startsWith('https://')
                  ? imgUrl
                  : `${API_URL}${imgUrl.startsWith('/') ? '' : '/'}${imgUrl}`
              }
              alt={`Uploaded image ${index + 1}`}
              fill
              className="object-cover"
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
              priority={index < 4}
            />

            {/* Кнопка удаления */}
            <button
              onClick={() => handleDelete(imgUrl)}
              className="absolute top-2 right-2 bg-red-600 text-white p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity"
              title="Удалить изображение"
            >
              <Trash2 size={16} />
            </button>
          </div>
        ))}
      </div>
    </main>
  );
}
