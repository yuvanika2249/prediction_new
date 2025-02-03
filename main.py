import streamlit as st
from streamlit_option_menu import option_menu

st.title("JOB SALARY PREDICTION")
with st.sidebar:
    select =option_menu(
        menu_title="MENU",
        options=["Home","About","Contact","How it works"],
        icons=["houses","file-person","person-lines-fill","pc-display-horizontal"]
    )
res=con.cursor()
if select=="Home":
    st.title("Home page")
    st.header("Find Your Expected Salary Instantly!")
    st.text("Our salary prediction tool helps job seekers, employees, and recruiters estimate salaries based on key factors like job title, experience, skills, and location.")
    st.subheader("Enter Your Details :")
    username = st.text_input("Name")
    city = st.text_input("City")
    if st.button("Submit"):
        
        sql= "insert into mydata(username,city)values(%s,%s)"
        res.execute(sql,(username,city))
        con.commit()
        st.success("Data insserted Succesfully")
        
elif select=="About":
    st.title("About page")
    st.text("Welcome to the Job Salary Prediction tool! This application helps job seekers, employers, and recruiters estimate salaries based on key factors such as :")
    st.markdown("""
### 🚀 Features:
- ✅ **Accurate Salary Predictions**  
- 📊 **Compare Salaries Across Locations & Industries**  
- 🎯 **Career Growth Insights**  
- ⚡ **Simple & Fast Salary Estimation**  
""")
    st.subheader("USER DETAILS :")
    df = pd.read_excel("D:/datalist.xlsx") 
    st.dataframe(df)
elif select=="Contact":
    st.title("Contact page")

elif select=="How it works":
    st.markdown("""
## 🔍 How It Works?
1️⃣ **Enter Your Job Details** – Provide job title, experience, education, and location.  
2️⃣ **Analysis** – Our machine learning model processes your input.  
3️⃣ **Get Your Salary Estimate** – View your predicted salary instantly.  
4️⃣ **Explore Trends** – Compare salaries in different locations and industries.  
""")

   

