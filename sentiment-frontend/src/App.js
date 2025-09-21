import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import SentimentVerySatisfiedIcon from '@mui/icons-material/SentimentVerySatisfied';
import MoodBadIcon from '@mui/icons-material/MoodBad';
function App() {
  return (
    <div className="container mt-5 pt-5 text-center">
      <h1>Sentiment Analysis App</h1>
      <br></br>
      <p>Welcome to the Sentiment Analysis Application.</p>
      <SentimentVerySatisfiedIcon style={{ fontSize: 40, color: 'black' }}/>
      <MoodBadIcon style={{ fontSize: 40, color: 'black' }}/>
      <br></br>
      <br></br>
      <button type ="button" className='btn btn-dark'> <Link to="/analyze" className='text-decoration-none text-light'>Go to Analysis</Link></button>
    </div>
  )
}

export default App;
