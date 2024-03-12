# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:19:49 2024

@author: laxmi
"""


import pandas as pd
import streamlit as st
import time
import sklearn_json as skljson



def main():
    html_temp="""
      <div style = "background-color:Lightblue;padding:16px">
      <h2 style="color:black; text-align:center;">Candidate Campus Placement Prediction ML System </h2>
      </div>
      """
    deserialized_model = skljson.from_json('lr_campus_model.json')


    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.write('')
    st.write('')

    st.markdown("##### Would you like to know the Candidate placement in the Campus Interviews?\n##### So let's try using Ml model to predict the probability.")
    
    gender_e = st.radio("Gender?", ('Male', 'Female'))
    if (gender_e == 'Male'):
        gender_v=0
    elif(gender_e == 'Female'):
        gender_v=1 

    ssc_p_v = st.slider("Secondary Education Percentage - 10th Grade", 0,100)

    ssc_b_e = st.radio("Board of Education", ('Central', 'Others'))
    if (ssc_b_e == 'Central'):
        ssc_b_v = 0
    elif(ssc_b_e == 'Others'):
        ssc_b_v = 1 

    hsc_p_v = st.slider("Higher Secondary Education Percentage - 12th Grade", 0,100)
    
    hsc_b_e = st.selectbox("Board of Education", ('Central', 'Others'))
    if (hsc_b_e == 'Central'):
        hsc_b_v = 0
    elif(hsc_b_e == 'Others'):
        hsc_b_v = 1

    hsc_s_e = st.selectbox("Specialization in Higher Secondary Education", ("Science", "Commerce", "Arts"))
    if (hsc_s_e == 'Science'):
        hsc_s_v = 0
    elif (hsc_s_e == 'Commerce'):
        hsc_s_v = 1 
    elif (hsc_s_e == 'Arts'):
        hsc_s_v = 2     

    degree_p_v = st.slider("Degree Percentage", 0,100)

    degree_t_e = st.radio("Under Graduation(Degree type)- Field of degree education", ("Sci & Tech", "Comm & Mgmt", "Others"))
    if (degree_t_e == 'Sci & Tech'):
        degree_t_v = 0
    elif (degree_t_e == 'Comm & Mgmt'):
        degree_t_v = 1 
    elif (degree_t_e == 'Others'):
        degree_t_v = 2

    st.write(' ')
    st.write(' ')
    workex_v = st.toggle("Work Experience?")
    st.write(' ')
    st.write(' ')

    etest_p_v = st.slider("Enter test percentage", 0,100)

    specialization_e = st.radio("Branch specialization", ("Mkt & HR", "Mkt & Fin"))
    if (specialization_e == 'Mkt & HR'):
        specialization_v = 0
    elif(specialization_e == 'Mkt & Fin'):
        specialization_v = 1    

    mba_p_v = st.slider("MBA percentage", 0,100)
    
    new_data = pd.DataFrame({
        'gender':gender_v,
        'ssc_p':ssc_p_v,
        'ssc_b':ssc_b_v,
        'hsc_p':hsc_p_v,
        'hsc_b':hsc_b_v,
        'hsc_s':hsc_s_v,
        'degree_p':degree_p_v,
        'degree_t':degree_t_v,
        'workex':workex_v,
        'etest_p':etest_p_v,
        'specialization':specialization_v,
        'mba_p':mba_p_v
    }, index=[0])
    
    
    

    
    try:
       if st.button('Predict'):        
          predicted_status=deserialized_model.predict(new_data)
          predicted_status_prob=deserialized_model.predict_proba(new_data)  
          
          if predicted_status>0:
             with st.spinner('Wait for it...'):
                 time.sleep(1)
          

             st.toast('Hip!')
             time.sleep(.5)
             st.toast('Hip!')
             time.sleep(.5)
             st.toast('Hooray!', icon='🎉')
             st.balloons()
             st.success("Your candidate can be placed in campus interviews with a probability of {:.2f} percent".format(predicted_status_prob[0][1]*100), icon="✅")
          else:
              st.warning("Your candidate will not be placed in the campus interviews with a probability of {:.2f} percent".format(predicted_status_prob[0][0]*100), icon="🔥")
    except:
        st.warning("Something went wrong, please check your input")
           
if __name__ == '__main__':
   main()