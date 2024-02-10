# import streamlit as st
# import json 
# import subprocess
# import tempfile

# st.title("HIV Treatment Server")
# st.text("HIV is a common disease that compromises patients immune system and limits their ability to fight infections.")
# st.text("Furthermore due to HIV's high mutation rate, its treatment life long anti retroviral therapy may have to change in patients and hiv devlops drug resitance within their bodies.")
# st.text("The goal of this website is to analyze HIV sequences from patients, and determine which drugs are suitiable for retroviral therapy")
# HIV_Consesus_Genome_Upload = st.file_uploader("Upload your sequence")

# # If statement to check if object is not null
# if HIV_Consesus_Genome_Upload is not None:
#     content = HIV_Consesus_Genome_Upload.read().decode('utf-8')
    
#     # Save the uploaded file to a temporary location
#     with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#         temp_file.write(content.encode())
#         temp_file_path = temp_file.name
    
#     # Check that file has extension type '.fasta'
#     if (temp_file_path.lower().endswith('.fasta')):
#         st.text("Hi")

#         # Try-catch block to check if file/server/etc is up
#         try:
#             # Run command, pass in the temporary file path
#             subprocess.call(['sierrapy', 'fasta', temp_file_path, '-o', 'test4433343443.json'], shell=True) #Run under Windows 
        
#         # Exception block: print out errors, end program, pass errors into variable to be displayed.
#         except Exception as error:
#             # handle the exception
#             print("An exception occurred:", error) # An exception occurred: <EXCEPTION>

#     else:
#         st.text("ERROR: file must be of type .fasta")
import json
file = open()










# with open('test.json', 'r') as file:
#     # Load the JSON data into a dictionary
#     data = json.load(file)

# # Now, data contains the contents of the JSON file as a dictionary

# #for dictionary in data:
# #    for json_info in data:
# #        for stuff in json_info:
# #            print(stuff["drugResistance"])
# for json_info in data:
#     drug_resistance = json_info.get("drugResistance")
#     if drug_resistance is not None:
#         resistant_drugs_information.append(drug_resistance)     
# for index_drug in range(len(resistant_drugs_information)):
#     #print(drug)
#     print(resistant_drugs_information[index_drug])
#        # drug_names.append(drug['drug']['name'])
# #print(drug_names)
    