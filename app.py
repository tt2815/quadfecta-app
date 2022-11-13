import pandas as pd
from utils import *
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Quadfecta Dashboard",
	page_icon=":whale:",
	layout="wide")



df = pd.read_excel("Quadfect_Tag_Filter_Test.xlsx",
	engine="openpyxl")

uiFriendlyColNames = formatColumnNames(df.columns.values)
st.sidebar.header("Please Filter Here:")


topLevelFilters = ["Sector", "Climate/Energy Provision", "Primary Technology Tag", 
"Policy Tag", "Innovation Stage", "Bill Name", "Agency Name"]


uniquevalues = df[~df["Sector"].isnull()]["Sector"].unique()
sectorFilter = st.sidebar.multiselect("Select Sector:", 
		options=uniquevalues,
		default=uniquevalues)

uniquevalues = df[~df["Climate/Energy Provision"].isnull()]["Climate/Energy Provision"].unique()
climateProvisionFilter = st.sidebar.multiselect("Select Climate/Energy Provision:", 
		options=uniquevalues,
		default=uniquevalues)

uniquevalues = df[~df["Primary Technology Tag"].isnull()]["Primary Technology Tag"].unique()
primaryTechTagFilter = st.sidebar.multiselect("Select Primary Technology Tag:", 
		options=uniquevalues,
		default=uniquevalues)

uniquevalues = df[~df["Policy Tag"].isnull()]["Policy Tag"].unique()
policyTagFilter = st.sidebar.multiselect("Select Policy Tag:", 
		options=uniquevalues,
		default=uniquevalues)

uniquevalues = df[~df["Innovation Stage"].isnull()]["Innovation Stage"].unique()
innovationStageFilter = st.sidebar.multiselect("Select Innovation Stage:", 
		options=uniquevalues,
		default=uniquevalues)

uniquevalues = df[~df["Bill Name"].isnull()]["Bill Name"].unique()
billNameFilter = st.sidebar.multiselect("Select Bill Name:", 
		options=uniquevalues,
		default=uniquevalues)

uniquevalues = df[~df["Agency Name"].isnull()]["Agency Name"].unique()
agencyNameFilter = st.sidebar.multiselect("Select Agency Name:", 
		options=uniquevalues,
		default=uniquevalues)

df.rename(columns=uiFriendlyColNames, inplace=True)

dfSelected = df.query(
	"Sector == @sectorFilter & ClimateEnergyProvision == @climateProvisionFilter & PrimaryTechnologyTag == @primaryTechTagFilter & PolicyTag == @policyTagFilter & InnovationStage == @innovationStageFilter & BillName == @billNameFilter & AgencyName == @agencyNameFilter")

st.title(":whale: DataFrame")
st.dataframe(dfSelected)


# ------ MAINPAGE ------

st.title(":whale: Quadfecta Dashboard")
st.markdown("###")

total_funding = dfSelected['FundingAmountmillion'].sum()*1000000

average_funding = round(total_funding/len(dfSelected),2)


left_col, right_col = st.columns(2)

with left_col:
	st.subheader("Total Funding Amount:")
	st.subheader(f"US $ {total_funding:,}")

with right_col:
	st.subheader("Average Funding Amount:")
	st.subheader(f"US $ {average_funding:,}")


st.markdown("---")


total_funding_by_sector = (
	dfSelected.groupby(by=['Sector']).sum()[["FundingAmountmillion"]].sort_values(by="FundingAmountmillion")
	)

fig_funding_amt = px.bar(
	total_funding_by_sector,
	y=total_funding_by_sector.index,
	x="FundingAmountmillion",
	orientation="h",
	title="<b>Total Funding by Sector</b>",
	template="plotly_white",
	color_discrete_sequence=["#0083B8"] * len(total_funding_by_sector)
	)

st.plotly_chart(fig_funding_amt)

st.markdown("---")

total_funding_by_policyTag = (
	dfSelected.groupby(by=['PolicyTag']).sum()[["FundingAmountmillion"]].sort_values(by="FundingAmountmillion")
	)

fig_funding_amt = px.bar(
	total_funding_by_policyTag,
	y=total_funding_by_policyTag.index,
	x="FundingAmountmillion",
	orientation="h",
	title="<b>Total Funding by Policy Tag</b>",
	template="plotly_white",
	color_discrete_sequence=["#0083B8"] * len(total_funding_by_policyTag)
	)

st.plotly_chart(fig_funding_amt)

st.markdown("---")

total_funding_by_primaryTechTag = (
	dfSelected.groupby(by=['PrimaryTechnologyTag']).sum()[["FundingAmountmillion"]].sort_values(by="FundingAmountmillion")
	)

fig_funding_amt = px.bar(
	total_funding_by_primaryTechTag,
	y=total_funding_by_primaryTechTag.index,
	x="FundingAmountmillion",
	orientation="h",
	title="<b>Total Funding by Primary Technology Tag</b>",
	template="plotly_white",
	color_discrete_sequence=["#0083B8"] * len(total_funding_by_primaryTechTag)
	)

st.plotly_chart(fig_funding_amt)


# -------------- Some style formatting --------------------

hide_style_css = """
				<style>
				#MainMenu {visibility: hidden;}
				footer {visibility: hidden;}
				header {visibility: hidden;}
				</style>
"""

st.markdown(hide_style_css, unsafe_allow_html=True)