import React, { useEffect } from 'react';
import Navbar from '../components/Navbar';
import { useNavigate } from "react-router-dom";


const UploadPage = () => {
    const navigate = useNavigate();
    const [data, setData] = React.useState("");
    const fileInput = React.useRef<HTMLInputElement | null>(null);
    const jobDescriptionInput = React.useRef<HTMLTextAreaElement | null>(null);
    
    const handleUpload = async () => {
        const file = fileInput.current?.files?.[0];
        if (!file) {
            return;
        }

        const formData = new FormData();
        formData.append('resume', file);
        formData.append('job_description', jobDescriptionInput.current?.value || '');
        try {
            const response = await fetch('http://127.0.0.1:5000/api/upload', {
                method: 'POST',
                body: formData,
            });
            const result = await response.text();
            setData(result);
            navigate("/cover-letter");
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

  useEffect(() => {
    // Any side effects or data fetching can be done here
  }, []);
 return (
    <div>
        <Navbar />
        <h1>Upload Page</h1>
        <input type="file" ref={fileInput} />
        <button 
        onClick={() => {
            handleUpload()
            
        }}
        style={{
            backgroundColor: 'blue',
            color: 'white',
            padding: '10px 20px',
            borderRadius: '5px',
            border: 'none',
            cursor: 'pointer'
        }}>
            Upload
        </button>
       
        {data && <p>{data}</p>      
        }
        <textarea
            style={{
                width: '100%',
                height: '200px',
                marginTop: '20px',
                padding: '10px',
                borderRadius: '5px',
                border: '1px solid #ccc',
                resize: 'none'
            }}
            ref={jobDescriptionInput}
        />
    </div>
  );
}
export default UploadPage;