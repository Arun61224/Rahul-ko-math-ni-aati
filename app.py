import streamlit as st

st.title("Discount Percentage Calculator 💸")

# User inputs
selling_price = st.number_input("Selling Price (Original Price) dalein:", min_value=0.0, format="%.2f")
discounted_price = st.number_input("Discounted Price (Final Price) dalein:", min_value=0.0, format="%.2f")

# Calculate button
if st.button("Check Discount"):
    # Ye raha aapka popup!
    st.toast("Terko Itna bhi ni aata 🤦‍♂️")
    
    if selling_price > 0:
        if discounted_price > selling_price:
            st.error("Discounted Price, Selling Price se zyada nahi ho sakta!")
        else:
            # Discount calculation
            discount_amount = selling_price - discounted_price
            discount_percentage = (discount_amount / selling_price) * 100
            
            st.success(f"**Discount Percentage:** {discount_percentage:.2f}%")
            st.info(f"**Aapki Bachat (Savings):** ₹{discount_amount:.2f}")
    else:
        st.warning("Kripya Selling Price 0 se zyada dalein.")
