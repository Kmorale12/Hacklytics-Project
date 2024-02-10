import streamlit as st
import json 
import subprocess
st.title("HIV Treatment Server")
st.text("HIV is a common disease that compromises patients immune system and limits their ability to fight infections.")
st.text("Furthermore due to HIV's high mutation rate, its treatment life long anti retroviral therapy may have to change in patients and hiv devlops drug resitance within their bodies.")
st.text("The goal of this website is to analyze HIV sequences from patients, and determine which drugs are suitiable for retroviral therapy")
HIV_Consesus_Genome_Upload = st.file_uploader("Upload your sequence")
# sierrapy fasta sequences_Test_HIV_Genome.fasta

    
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
    