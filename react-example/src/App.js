import logo from './logo.svg';
import './App.css';

import { useEffect, useState } from "react";

import Question from "./components/Question";

function App() {
  const [data, setData] = useState();

  async function getData() {
      const response = await fetch('/api');
      const data = await response.json();
      return data;
  }

  useEffect(() => {
      getData().then((data) => {
          setData(data);
      });
  }, []);

  return (
      <>
      {data && data.data.map((value, index) =>
        <Question key={index} item={value} />
      )}
      </>
  );
}

export default App;
