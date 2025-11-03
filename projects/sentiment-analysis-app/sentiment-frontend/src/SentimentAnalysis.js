import React, {useState} from 'react';

function SentimentAnalysis() {
const [input, setInput] = useState("");
const [result, setResult] = useState("");

const handleChange = (e) => {
  setInput(e.target.value);
}

const handleSubmit = async (e) => {
        e.preventDefault();
        try {
      const res = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input }), // must match FastAPI
      });
      const data = await res.json();
      setResult(data);
    } catch (error) {
      console.error("Error calling API:", error);
    }
  };
    return (
        <div className="container mt-5">
      <h2 className='text-center'>Sentiment Analysis</h2>
        <br></br>
      <form onSubmit={handleSubmit} className="mb-3">
        <div className="row">
            <div className="col-9">
                 <input
                    type="text"
                    className="form-control mb-2"
                    placeholder="Type a sentence..."
                    value={input}
                    onChange={handleChange}
                    />
            </div>
            <div className="col-3">
                 <button type="submit" className="btn btn-dark">
                    Analyze
                </button>
            </div>
        </div>
       
       
      </form>
<hr></hr>
<br></br>
      {result && (
        <div className="card p-3 mt-3">
          <h5>Result:</h5>
          <br></br>
          <p>
            <b>Label:</b> {result.label}
          </p>
          <p>
            <b>Confidence:</b> {(result.score * 100).toFixed(2)}%
          </p>
        </div>
      )}
    </div>
        );
    }

export default SentimentAnalysis;