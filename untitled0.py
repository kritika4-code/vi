import streamlit as st

def calculate_emi(principal, annual_rate, months):
    # Convert annual rate to monthly rate
    monthly_rate = annual_rate / (12 * 100)

    # Calculate EMI using the formula
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

    return emi

# Streamlit app UI
def main():
    st.title("EMI Calculator")

    # Input fields for loan amount, interest rate, and loan tenure
    principal = st.number_input("Enter Loan Amount (Principal)", min_value=1, value=500000, step=1000)
    annual_rate = st.number_input("Enter Annual Interest Rate (%)", min_value=0.0, value=10.0, step=0.1)
    months = st.number_input("Enter Loan Tenure (Months)", min_value=1, value=24, step=1)

    # When the button is clicked, calculate EMI
    if st.button("Calculate EMI"):
        if principal > 0 and annual_rate > 0 and months > 0:
            emi = calculate_emi(principal, annual_rate, months)
            total_payment = emi * months

            # Display results
            st.subheader(f"Your Monthly EMI: ₹{emi:.2f}")
            st.subheader(f"Total Amount Paid Over {months} Months: ₹{total_payment:.2f}")
        else:
            st.error("Please enter valid positive values.")

# Run the app
if __name__ == "__main__":
    main()
