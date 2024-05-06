import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [unitNames, setUnitNames] = useState("");
  const [result, setResult] = useState(null);

  const handleButtonClick = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/get_exam_info",
        { unit_names: unitNames },
        {
          "content-type": "Application/json",
        }
      );

      if (response.data.success) {
        setResult(response.data.data);
      } else {
        console.error(response.data.error);
      }
    } catch (error) {
      console.error("Error:", error.message);
    }
  };

  useEffect(() => {
    console.log(result);
  });

  return (
    
    <div className="p-8">
      <p className="text-[30px] text-black font-extrabold">Assi<span className="text-[orangered]">gn</span></p>
      <div className="w-[80%] mx-auto p-8 items-center justify-center border border-slate-grey">
        <input
          type="text"
          value={unitNames}
          className="w-[80%] mx-auto shadow-lg bg-white text-black h-[30px] p-8 border border-black"
          placeholder="Enter the units ie. INS212A,BIL112D,MAT120A"
          onChange={(e) => setUnitNames(e.target.value)}
        />
        <button
          onClick={handleButtonClick}
          className="bg-green-900 p-4 text-white ml-[20px]"
        >
          Submit
        </button>
      </div>

      {result &&
        result.map((results, index) => {
          return (
            <div className="w-[80%] mx-auto p-8 border border-slate-grey bg-[orange] rounded-lg mb-[10px]" key={index}>
              <p>{results.Course}</p>
              <p>{results.Location}</p>
              <p>{results.Date}</p>
              <p>{results.Time}</p>
              <p className="text-[red]">{results.message}</p>

            </div>
          );
        })
     
      }
    </div>
  );
}

export default App;
