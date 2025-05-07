import re
import streamlit as st
import string
import random


st.title("Password Strength Meter")

input_num = st.text_input("Enter Password", type="password")

def strength_checker(password):
    if not password:  # Check if password is empty so run
        return
    
    upper = False
    lower = False
    digit = False
    special = False
    
    # Check each character
    for char in password:
        if char.isupper():
             upper = True
        elif char.islower():
             lower = True
        elif char.isdigit():
            digit = True
        elif re.search(r'[!@#$%^&*]', char):
            special = True
     
    # Length check
    if len(password) >= 8:
        st.success("✅ Your password is 8 characters or longer")
    else:
        st.error("❌ Password should be at least 8 characters")
    
    # Case checks
    if upper:
        st.success("✅ Contains uppercase letters")
    else:
        st.error("❌ Missing uppercase letters")
    
    if lower:
        st.success("✅ Contains lowercase letters")
    else:
        st.error("❌ Missing lowercase letters")
    
    # Digit check
    if digit:
        st.success("✅ Contains numbers")
    else:
        st.error("❌ Missing numbers")
    
    # Special character check
    if special:
        st.success("✅ Contains special characters")
    else:
        st.error("❌ Missing special characters (!@#$%^&*)")
    
    # Calculate strength score
    checks_passed = sum([len(password) >= 8, upper,lower, digit,special])

    st.progress(checks_passed/5)
    if checks_passed < 3:
         st.write("Strength score is low ❗")
    elif checks_passed >3:
         st.write("Strength score is Hight⚡")
    else:
         st.write("Strength score is Moderate😀")
        



    # generete random password

    def generate_pass():
        upper_gen = string.ascii_uppercase
        lower_gen = string.ascii_lowercase
        num_gen = string.digits
        spec_gen = string.punctuation
        spec_chr = "!@#$%^&*"

    # pick random one keyword
        one_upp = random.choice(upper_gen)
        one_low = random.choice(lower_gen)
        one_num = random.choice(num_gen)
        one_spe = random.choice(spec_gen)
        one_chr = random.choice(spec_chr)

        cal_keys = 2 * (one_upp + one_low + one_num + one_spe + one_chr)
    
        remaining_key =  4 * (random.choice(cal_keys))
        final_key = cal_keys + remaining_key

        st.success(f'''Try This Strong Password : {final_key}''')
    

    generate_pass()

if input_num:
    strength_checker(input_num)