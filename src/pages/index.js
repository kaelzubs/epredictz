import React from "react"
import axios from "axios";

// markup
const IndexPage = () => {

  // Functions
  const fectData = async () => {

    const options = {
      method: 'GET',
      url: 'https://daily-betting-tips.p.rapidapi.com/daily-betting-tip-api/items/daily_betting_coupons',
      params: {sort: '-id'},
      headers: {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': 'f0a543b8d9msh223413be8e8b05bp1dc698jsn8b857748f3a5',
        'X-RapidAPI-Host': 'daily-betting-tips.p.rapidapi.com'
      }
    };

    await axios.request(options).then(function (response) {
      console.log(response.data);
    }).catch(function (error) {
      console.error(error);
    });
  }
  fectData()
  return (
    <main>
      <title>Home Page</title>
      <h1>This is the landing page for Excellent Prediction Zone and will be available soon</h1>
    </main>
  )
}

export default IndexPage

// styles