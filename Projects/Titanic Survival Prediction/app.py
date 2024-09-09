import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.lb')

st.image('titanic.jpg',use_column_width=True)

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 40px;
    }
    </style>
    <div class="title">Titanic Survival Prediction</div>
    """,
    unsafe_allow_html=True
)

# Collect user input
Class = st.selectbox('Select Class', ['First Class','Second Class','Third Class'])
sex = st.selectbox('Select Gender',['Male','Female'])
age = st.number_input('Enter Age', min_value=0, max_value=120, step=1)
embark_town = st.selectbox('Embark Town',['Southampton','Cherbourg','Queenstown'])
alone = st.selectbox('Alone',['Yes','No'])


# Center the button using custom CSS
st.markdown(
    """
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True
)

submit = st.button("Submit")

if submit:
    new_data = pd.DataFrame({
        'Class': [Class], 
        'Gender': [sex], 
        'Age': [age], 
        'Embark Town': [embark_town], 
        'Alone': [alone], 
    })

    if Class=='First Class':
        Class=1
    elif Class=='Second Class':
        Class=2
    else:
        Class=3

    if sex=='Male':
        sex=1
    else:
        sex=0

    if embark_town=='Southampton':
        embark_town=1
    elif embark_town=='Cherbourg':
        embark_town=2
    else:
        embark_town=3

    if alone=='Yes':
        alone=1
    else:
        alone=0

    # Perform further actions with new_data if needed
    st.write("Data for prediction:", new_data)

    # Center the response box using custom CSS
    st.markdown(
        """
        <style>
        div.response-box {
            display: block;
            margin: 20px auto;
            padding: 15px;
            border-radius: 10px;
            background-color: #f0f0f0;
            width: 50%;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    prediction = model.predict([[Class,sex,age,embark_town,alone]])
    
    if prediction[0] == 0:
        data = 'No'
    else:
        data = 'Yes'

    # Display the results
    st.subheader(f"Alive : {data}")