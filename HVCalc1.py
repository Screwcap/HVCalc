"""
Hotel Valuation Calculator (HVCalc)
Author: Andrew Fritz (Screwcap, LLC)
Website: https://boutiquehotel.consulting
Version: 1.0
Description: A simple hotel valuation calculator built using Streamlit.
License: MIT License
"""
import streamlit as st
import numpy as np

def calculate_loan_payment(loan_amount, interest_rate, loan_term):
    monthly_rate = (interest_rate / 100) / 12
    num_payments = loan_term * 12
    if monthly_rate > 0:
        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    else:
        monthly_payment = loan_amount / num_payments
    return monthly_payment

def get_project_rating(profit):
    if profit > 100000:
        return "🟢 Great Start! This looks promising, but dig deeper—every deal has its quirks!"
    elif 25000 < profit <= 100000:
        return "🟡 Not So Good But Worth Looking Into—maybe there's untapped potential? Let's analyze further!"
    elif 0 < profit <= 25000:
        return "🟠 Something Smells Fishy... Double-check your numbers and get expert insight before diving in."
    else:
        return "🔴 Not Really Worth It in Today's Economy. But hey, creative financing and deep due diligence might turn things around! Need help? We got you."

def main():
    st.set_page_config(page_title="Hotel Valuation Calculator", layout="wide")
    st.title("🏨 Hotel Valuation Calculator")
    st.markdown("### Analyze the profitability and investment potential of your hotel.")
    
    with st.sidebar:
        st.header("Input Parameters")
        purchase_price = st.number_input("💰 Purchase Price ($)", min_value=10000, step=10000, value=1000000, format="%d")
        down_payment_pct = st.slider("💵 Down Payment (%)", min_value=0, max_value=100, value=20)
        interest_rate = st.slider("📉 Interest Rate (%)", min_value=1.0, max_value=10.0, step=0.1, value=5.0)
        loan_term = st.slider("📅 Loan Term (Years)", min_value=5, max_value=30, step=5, value=20)
        noi = st.number_input("📊 Net Operating Income (NOI) ($)", min_value=0, step=1000, value=100000, format="%d")
    
    # Calculations
    down_payment = (down_payment_pct / 100) * purchase_price
    loan_amount = purchase_price - down_payment
    monthly_payment = calculate_loan_payment(loan_amount, interest_rate, loan_term)
    annual_debt_service = monthly_payment * 12
    dscr = noi / annual_debt_service if annual_debt_service > 0 else 0
    cap_rate = (noi / purchase_price) * 100
    cash_on_cash_return = ((noi - annual_debt_service) / down_payment) * 100 if down_payment > 0 else 0
    annual_profit = noi - annual_debt_service
    rating = get_project_rating(annual_profit)
    
    # Display Outputs
    st.subheader("📈 Financial Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏦 Loan Amount", f"${loan_amount:,.0f}")
        st.metric("📉 Monthly Payment", f"${monthly_payment:,.0f}")
    with col2:
        st.metric("📅 Annual Debt Service", f"${annual_debt_service:,.0f}")
        st.metric("📊 Capitalization Rate", f"{cap_rate:.2f}%")
    with col3:
        st.metric("💰 Cash-on-Cash Return", f"{cash_on_cash_return:.2f}%")
        st.metric("📉 DSCR", f"{dscr:.2f}")
    
    st.subheader("Investment Rating: ")
    st.markdown(f"### {rating}")
    
    st.markdown("<small>*All information is deemed reliable but not guaranteed. Buyer to verify all information. If you make a bad deal, don’t come crying to us—we just do math.*</small>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
