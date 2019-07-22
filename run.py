import statistical_cal as st
name_of_column = ""
data = ""


st.menu()
print("Which number of column do you chose?")
choice = int(input())
#st.import_data(choice, name_of_column)
st.average(name_of_column,choice,data)
st.median(choice)
st.standard_deviation(choice)
st.standard_error(choice)
st.variance(choice)
st.kurtosis(choice)










