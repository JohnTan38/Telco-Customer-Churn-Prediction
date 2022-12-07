import pickle
import streamlit as st
import pandas as pd
from PIL import Image
model_file = (r"M:/CHL/BPI/Internal (can share with other dept & bu)/SCAN/AV_Prime_Mover/Data/model_C_1.bin")

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

NB = st.select_slider('', options = [100,150,200,250,300,350,400,500,600,700,750,800,900,1000,1250,1500,1750,2000,2500,3000,3500,4000,4500,5000,5500,6000 ], value = 100)

ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    background: rgb(1 1 1 / 0%); } </style>''', unsafe_allow_html = True)

Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: rgb(14, 38, 74); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)
    
Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                { color: rgb(14, 38, 74); } </style>''', unsafe_allow_html = True)
    
col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
    background: linear-gradient(to right, rgb(1, 183, 158) 0%, 
                                rgb(1, 183, 158) {NB}%, 
                                rgba(151, 166, 195, 0.25) {NB}%, 
                                rgba(151, 166, 195, 0.25) 100%); }} </style>'''

#ColorSlider = st.markdown(col, unsafe_allow_html = True)

def main():

	#image = Image.open('images/icone.png')
	#image2 = Image.open('images/image.png')
	#st.image(image,use_column_width=False)
	add_selectbox = st.sidebar.selectbox(
	"How would you like to predict?",
	("Online", "Batch"))
	st.sidebar.info('Input data for customer')
	#st.sidebar.image(image2)
	st.title("Predicting Telco Customer Churn")
	if add_selectbox == 'Online':


                

		#MonthlyRevenue= st.number_input('Monthly Revenue', min_value=0, max_value=900, value=0)
		MonthlyRevenue = st.select_slider('Monthly Revenue', options = [100,150,200,250,300,350,400,500,600,700,750,800,900,1000,1250,1500,1750,2000,2500,3000,3500,4000,4500,5000,5500,6000 ], value = 100)
		ColorSlider = st.markdown(col, unsafe_allow_html = True)
		#MonthlyMinutes= st.number_input('Monthly Minutes', min_value=0, max_value=6000, value=0)
		MonthlyMinutes= st.select_slider('Monthly Minutes', options = [100,250,500,750,1000,1250,1500,1750,2000,2500,3000,3500,4000,4500,5000,5500,6000 ], value = 100)
		TotalRecurringCharge = st.number_input('Total Recurring Charge', min_value=0, max_value=400, value=0)
		DirectorAssistedCalls = st.number_input('Director Assisted Calls', min_value=0, max_value=75, value=0)
		CustomerCareCalls = st.number_input('Customer Care Calls', min_value=0, max_value=200, value=0)
		ReceivedCalls = st.number_input('Received Calls', min_value=0, max_value=2500, value=0)
		OutboundCalls = st.number_input('Outbound Calls', min_value=0, max_value=600, value=0)
		InboundCalls = st.number_input('Inbound Calls', min_value=0, max_value=600, value=0)
		MonthsInService= st.number_input(' Months In Service', min_value=6, max_value=61, value=6)
		UniqueSubs= st.number_input(' Unique Subs', min_value=1, max_value=18, value=1)
		ActiveSubs = st.number_input('Active Subs', min_value=0, max_value=11, value=0)

		#RetentionCalls = st.number_input('Retention Calls', min_value=0, max_value=5, value=0)
		RetentionCalls = st.select_slider('Retention Calls', options = [1,2,3,4,5], value = 1)
		RetentionOffersAccepted = st.number_input('Retention Offers Accepted', min_value=0, max_value=3, value=0)
		IncomeGroup = st.number_input('Income Group', min_value=0, max_value=9, value=0)
		AdjustmentsToCreditRating = st.number_input('Adjustments To Credit Rating', min_value=0, max_value=25, value=0)
		CreditRating1 = st.selectbox(' Credit Rating', ['Highest', 'High', 'Good', 'Medium', 'Low', 'VeryLow', 'Lowest'])
		CreditRating = st.selectbox(' Credit Rating', [1, 2, 3, 4, 5, 6, 7])
		PrizmCode1= st.selectbox(' Customer Residence', ['Town', 'Sunurban', 'Rural', 'Other'])
		PrizmCode = st.selectbox(' Customer Residence', [1, 2, 3, 4])
		Occupation1 = st.selectbox(' Customer Occupation', ['Clerical', 'Crafts', 'Homemaker', 'Other', 'Professional', 'Retired', 'Self', 'Student'])
		Occupation = st.selectbox(' Customer Occupation', [1, 2, 3, 4, 5, 6, 7, 8])
				
		output= ""
		output_prob = ""
		input_dict={
					
				"MonthlyRevenue": MonthlyRevenue,
				"MonthlyMinutes": MonthlyMinutes,
				"TotalRecurringCharge": TotalRecurringCharge,
				"DirectorAssistedCalls": DirectorAssistedCalls,
				"CustomerCareCalls": CustomerCareCalls,
				"ReceivedCalls": ReceivedCalls,
				"OutboundCalls": OutboundCalls,
				"InboundCalls": InboundCalls,
                                "MonthsInService":MonthsInService,
                                "UniqueSubs": UniqueSubs,
                                "ActiveSubs": ActiveSubs,
				"RetentionCalls": RetentionCalls,
				"RetentionOffersAccepted": RetentionOffersAccepted,
                                "IncomeGroup": IncomeGroup,
				"AdjustmentsToCreditRating": AdjustmentsToCreditRating,
				"CreditRating": CreditRating,
                                "PrizmCode": PrizmCode,
				"Occupation": Occupation
				
			}

		if st.button("Predict"):
			X = dv.transform([input_dict])
			y_pred = model.predict_proba(X)[0, 1]
			churn = y_pred >= 0.5
			output_prob = float(y_pred)
			output = bool(churn)
		st.success('Churn: {0}, Risk Score: {1}'.format(output, output_prob))
	if add_selectbox == 'Batch':
		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			X = dv.transform([data])
			y_pred = model.predict_proba(X)[0, 1]
			churn = y_pred >= 0.5
			churn = bool(churn)
			st.write(churn)

if __name__ == '__main__':
	main()
