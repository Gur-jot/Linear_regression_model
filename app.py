import numpy as np
# from flask import Flask, request, jsonify, render_template
import pickle
import streamlit as st

# app = Flask(__name__)
model = pickle.load(open('linearregression.pkl','rb')) 

# @app.route('/')
# def home():
  
#     return render_template("index.html")
  
# @app.route('/predict',methods=['GET'])
def predict(experience):
    
    
    '''
    For rendering results on HTML GUI
    '''
    # exp = float(request.args.get('exp'))

    prediction =int(model.predict([[experience]]))
    
        
    # return render_template('index.html', prediction_text='Regression Model  has predicted salary for given experinace is Rs.  : {}'.format(prediction))
    return prediction

def main():

    st.title("salary prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Salary Prediction ML App </h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    exp = st.number_input('Experience', 2, 40)
    result=""
    if st.button("Predict"):
        result=predict(float(exp))
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
