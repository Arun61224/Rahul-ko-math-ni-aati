import streamlit as st
import time

# Page config thodi fun kar dete hain
st.set_page_config(page_title="Magic Math! 🎈", page_icon="🦄")

# Custom CSS for Childish/Playful UI and Animations
st.markdown("""
<style>
/* Font change karne ke liye */
@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Comic Neue', cursive !important;
}

/* Title pe Pulse Animation */
.title-text {
    color: #ff007f;
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    text-shadow: 2px 2px #ffcc00;
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

/* Button pe hover animation aur colors */
.stButton>button {
    background-color: #ff9900 !important;
    color: white !important;
    border-radius: 30px !important;
    border: 4px solid #ff007f !important;
    font-size: 22px !important;
    font-weight: bold !important;
    transition: 0.3s !important;
    width: 100%;
}
.stButton>button:hover {
    background-color: #ff007f !important;
    border: 4px solid #ff9900 !important;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Animated Title
st.markdown('<div class="title-text">✨ Jadoo Wala Calculator ✨</div>', unsafe_allow_html=True)
st.write("---")

# Inputs thode fun labels ke sath
col1, col2 = st.columns(2)
with col1:
    selling_price = st.number_input("🛍️ Kitne ka tha? (Original Price):", min_value=0.0, format="%.2f")
with col2:
    discounted_price = st.number_input("💸 Kitne me mila? (Final Price):", min_value=0.0, format="%.2f")

st.write("") # Thodi space ke liye

# Animated Button
if st.button("🪄 Chalo Jadoo Dekhein!"):
    
    # Tumhara special popup (toast)
    st.toast("Terko Itna bhi ni aata 🤦‍♂️", icon="🐣")
    
    if selling_price > 0:
        if discounted_price > selling_price:
            st.error("Arre buddhu! 🤪 Discounted price original se zyada thodi hota hai!")
        else:
            # Bachcho jaisi suspense ke liye thoda loading time
            with st.spinner('Ruko, Jadoo ho raha hai... 🧚‍♀️✨'):
                time.sleep(1.5)
            
            # Streamlit ki apni Balloon Animation!
            st.balloons()
            
            # Calculation
            discount_amount = selling_price - discounted_price
            discount_percentage = (discount_amount / selling_price) * 100
            
            st.success(f"🎉 **Waah! Pura {discount_percentage:.2f}% OFF mila!** 🥳")
            st.info(f"💰 **Tumhari Bachat:** ₹{discount_amount:.2f} (Ab iske golgappe kha lena! 🌮)")
    else:
        st.warning("⚠️ Pehle koi price toh daalo baba!")
