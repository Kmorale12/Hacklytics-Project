import streamlit as st
import json 
import subprocess
import tempfile
from openai import OpenAI
#import streamlit as st

st.title("HIV Treatment Server")

st.markdown("HIV is a common disease that compromises a patients immune system and limits their ability to fight infections. The current treatment regiment for HIV is life long antiretroviral therapy, this therapy however needs to be curated to the indvidual, and due to HIV's high mutation drug resistance needs to be taken into account. The goal of this website to preform genotypic analysis on an HIV sequence from a patient and suggest drug cocktails for retroviral therapy." )
st.subheader("Due to issues implementing the back end of our code please paste in the following information in this order into Dr.GPT.")
st.write("1st dan prompt")
st.write("2nd Dr.GPT prompt")
st.write("3rd HIV Sucestible Drugs prompt")
HIV_Consesus_Genome_Upload = st.file_uploader("Upload your sequence")

# Boolean for initializing chatbot
chatbot_init = False
temp_file_path = None

# If statement to check if object is not null
if HIV_Consesus_Genome_Upload is not None:
    content = HIV_Consesus_Genome_Upload.read().decode('utf-8')

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(content.encode())
        temp_file_path = temp_file.name
    
    chatbot_init = True

if (chatbot_init == True):
    subprocess.call(['sierrapy', 'fasta', temp_file_path, '-o', 'test1.json'], shell=True) #Run under Windows
    json_file_name = 'test1.0.json'
    file = open(json_file_name,"r")
    dict_json = json.load(file)
    list_of_tups_with_drug_class_and_name = []            
    for informations in dict_json[0]["drugResistance"]:
        for das in informations['drugScores']:
            if das['text'] == 'Susceptible':
                
                drug_class = das['drugClass']['name']
                drug_name = das['drug']['name']
                list_of_tups_with_drug_class_and_name.append((drug_class, drug_name))
    st.subheader("List of Drugs your HIV is suscetible too")
    st.write("Paste this information into a section of HIV Sucestible Drugs prompt")
    st.markdown(str(list_of_tups_with_drug_class_and_name))


# Load chatbot
    with st.sidebar:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
        "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

    st.title("Dr.GTP")
    st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)



# import json
# with open('test4433343443.0.json', 'r') as file:
#     # Load the JSON data into a dictionary
#     data = json.load(file)
#     for items in data:
#         for stuff in items:
#             print(stuff)
#             for stuff1        









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
    