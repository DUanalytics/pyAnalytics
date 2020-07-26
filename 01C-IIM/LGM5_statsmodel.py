#Topic:Logistic Regression - Stats Model - spector_data.exog
#-----------------------------
#libraries
# Load the data from Spector and Mazzeo (1980)
import statsmodels.api as sm

spector_data = sm.datasets.spector.load_pandas()
spector_data.data

spector_data.exog = sm.add_constant(spector_data.exog)

# Logit Model
logit_mod = sm.Logit(spector_data.endog, spector_data.exog)

logit_res = logit_mod.fit()
#Optimization terminated successfully.   Current function value: 0.402801 Iterations 7
print(logit_res.summary())
