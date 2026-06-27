import React, { useEffect } from 'react';
import Navbar from '../components/Navbar';
import { Link } from 'react-router-dom';

const UploadPage = () => {
    const [data, setData] = React.useState("");
 

    useEffect(() => {
        const fetchData = async () => {
            const res = await fetch('http://127.0.0.1:5000/api/test');
            const data = await res.text();
            setData(data);
        };
        fetchData();
    }, []);
 return (
    <div>
        <Navbar />
        <h1>Upload Page</h1>
        <p>Data from backend: {data.toString()}</p>
    </div>
  );
}
export default UploadPage;