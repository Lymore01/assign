from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Load your Excel file when the server starts
excel_file_path = 'Final 2023.xls'
df = pd.read_excel(excel_file_path)

@app.route('/api/get_exam_info', methods=['GET','POST'])
def get_exam_info():
    try:
        # get the locations
        Location = []
        for i in range(2,130):
            location_column = df.loc[i,"Unnamed: 0"]
            Location.append(str(location_column).replace("nan", "No location"))
        # get the courses row
        Row = []

        for i in range(2, 130):
            row = df.iloc[i]
            Row.append({
            "Location":f"{df.loc[i, 'Unnamed: 0']}",
            "Courses":row,
            })

# request.json.get('unit_names', '')
        data = request.get_json()
        print(data)
        unit_names = data["unit_names"].upper().replace(" ","")
        unit_name = unit_names.split(',')
        no_of_outputs = []
        all_rows = []
        # All_location = []
        # newCol = []
        result_data = []

        if (unit_names):
            for c in range(0,len(Location)):
                for i in range(0,17):
                    for j in range(0, len(unit_name)):
                        if (unit_name[j] == Row[c]["Courses"][f"Unnamed: {i}"]):
                            all_rows.append(Row[c]["Courses"][f"Unnamed: {i}"])
                            print(f"Location ({unit_name[j]}): " + Row[c]["Location"])
                            time_column = df.loc[:,f"Unnamed: {i}"] 
                            
                            print("Time: "+time_column[1])
                            units_row = df.loc[:, "Unnamed: 0"].tolist()
                            if(units_row.index(Row[c]["Location"])<67):
                                print("Date: "+time_column[0])
                            else:
                                units_row_two_index = units_row_two.index(Row[c]["Location"])
                                if units_row_two_index != -1:
                                     print("Date: " + time_column[67 + units_row_two_index])
                                else:
                                    print("None")
                            no_of_outputs.append(j)
                            result_data.append({
                                    "Location": Row[c]["Location"],
                                    "Course": unit_name[j],
                                    "Time": df.loc[:, f"Unnamed: {i}"][1],
                                    "Date": df.loc[:, f"Unnamed: {i}"][0] if units_row.index(Row[c]["Location"]) < 67 else df.loc[:, f"Unnamed: {i}"][67],
                            })
                            


                        else:
                            None
        else:
             result_data.append("Confirm if the units entered are correct")
        



        if ((len(no_of_outputs)) != (len(unit_name))):
                for i in range(0, len(unit_name)):
                        if(unit_name[i] not in all_rows):
                             result_data.append({"message":f"Unit {unit_name[i]} is not available, kindly correct it!"})
                        else:
                            None


                
        else:
                None
        
        return jsonify({'success': True, 'data': result_data})
        

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


