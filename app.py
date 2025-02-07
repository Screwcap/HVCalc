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

def main():
    st.set_page_config(page_title="Hotel Financing Calculator", layout="wide")
    st.title("🏨 Hotel Financing Calculator")
    st.markdown("### Analyze the profitability and investment potential of your hotel.")
    
    with st.sidebar:
        st.header("Input Parameters")
        purchase_price = st.number_input("💰 Purchase Price ($)", min_value=10000, step=50000, value=1000000, format="%d")
        down_payment_pct = st.slider("💵 Down Payment (%)", min_value=0, max_value=100, value=20)
        interest_rate = st.slider("📉 Interest Rate (%)", min_value=1.0, max_value=10.0, step=0.1, value=5.0)
        loan_term = st.slider("📅 Loan Term (Years)", min_value=5, max_value=30, step=5, value=20)
        noi = st.number_input("📊 Net Operating Income (NOI) ($)", min_value=0, step=25000, value=100000, format="%d")
    
    # Calculations
    down_payment = (down_payment_pct / 100) * purchase_price
    loan_amount = purchase_price - down_payment
    monthly_payment = calculate_loan_payment(loan_amount, interest_rate, loan_term)
    annual_debt_service = monthly_payment * 12
    annual_profit = noi - annual_debt_service
    
    # Investment Rating
    def get_project_rating(profit):
        if profit > 100000:
            return "🟢 Great Start! But dive deeper for hidden costs and opportunities."
        elif 25000 < profit <= 100000:
            return "🟡 Worth Looking Into—consider optimization strategies."
        elif 0 < profit <= 25000:
            return "🟠 Something Feels Off—run deeper analysis before committing."
        else:
            return "🔴 High Risk—seek professional insights before proceeding!"
    
    rating = get_project_rating(annual_profit)
    
    st.subheader("📈 Financial Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🏦 Loan Amount", f"${loan_amount:,.0f}")
        st.metric("📉 Monthly Payment", f"${monthly_payment:,.0f}")
    with col2:
        st.metric("📅 Annual Debt Service", f"${annual_debt_service:,.0f}")
        st.metric("💰 Estimated Annual Profit", f"${annual_profit:,.0f}")
    
    st.subheader("💡 Investment Rating: ")
    st.markdown(f"### {rating}")
    
    with st.form("lead_capture"):
        email = st.text_input("📩 Enter your email to receive a detailed PDF report")
        submit = st.form_submit_button("📬 Send My Report")
        
        if submit:
            st.success(f"✅ Report will be sent to {email} shortly!")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        '<small>Built by a <a href="https://boutiquehotel.consulting" target="_blank">Screwcap Company.</a>. '
        'For more detailed property evaluations, <a href="https://boutiquehotel.consulting/services" target="_blank">visit our services page</a>.</small>',
        unsafe_allow_html=True
    )
    
    # Google Analytics Tracking
    st.markdown("""
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-PPKQTJWXHS"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-PPKQTJWXHS');
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown("<small>*All information is deemed reliable but not guaranteed. Buyer to verify all information. If you make a bad deal, don’t come crying to us—we just do math.*</small>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
