import React, { useState } from 'react';
import axios from 'axios';

const PostureUpload = () => {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [feedback, setFeedback] = useState('');
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    setPreview(URL.createObjectURL(selected));
    setFeedback('');
    setError('');
  };

  const handleUpload = async () => {
    if (!file) return alert('Please select a file.');

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post('http://localhost:8000/api/analyze/', formData);
      setFeedback(response.data.feedback);
      setError('');
    } catch (err) {
      setError(err.response?.data?.error || 'Upload failed.');
      setFeedback('');
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '400px' }}>
      <h2>Upload Posture Image</h2>
      <input type="file" onChange={handleFileChange} />
      {preview && <img src={preview} alt="Preview" style={{ width: '100%', marginTop: '10px' }} />}
      <button onClick={handleUpload} style={{ marginTop: '10px' }}>Upload</button>

      {feedback && <p style={{ color: 'green', marginTop: '10px' }}>✅ Feedback: {feedback}</p>}
      {error && <p style={{ color: 'red', marginTop: '10px' }}>❌ Error: {error}</p>}
    </div>
  );
};

export default PostureUpload;
