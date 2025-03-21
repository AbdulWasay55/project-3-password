import streamlit as st
import re

st.set_page_config(page_title='🔐 Password Strength Meter')
# Custom CSS for styling
st.markdown('''
    <style>
        body {
            background-color: #0d1117;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: #161b22;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button {
            background: linear-gradient(135deg ,rgba(16, 61, 119, 0.3),rgba(65, 152, 228, 0.2));
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            box-shadow: 0 0 10px rgb(65, 152, 228);
        }
        .blue-box {
            background-color: rgba(0, 123, 255, 0.2);
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin-top: 10px;
            opacity
        }
    </style>
''', unsafe_allow_html=True)

def check_password_strength(password: str) -> tuple[int, str, list[str]]:
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append('Password should be at least 8 characters long.')

    # Upper and lower case check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('Password should contain both uppercase and lowercase letters.')

    # Digit check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append('Password should include at least one digit (0-9).')

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append('Password should have at least one special character (!@#$%^&*).')

    # Scoring system
    if score <= 2:
        strength = 'Weak'
    elif score == 3 :
        strength = 'Moderate'
    else:
        strength = 'Strong'

    if strength == 'Strong':
        feedback.append('Your password is strong! Great job!')

    return score, strength, feedback


# Streamlit App UI
st.title('🔐 Password Strength Meter')

password = st.text_input('Enter your password:', type='password')

if st.button('Check Password Strength'):
    if password:
        score, strength, feedback = check_password_strength(password)
        st.write(f'### Password Strength: {strength}')
        st.write(f'Score: {score}/4')

        if strength == 'Weak':
            st.error('Your password is weak! Please improve it.')
        elif strength == 'Moderate':
            st.markdown('<div class="blue-box">Your password is moderate. Try adding more complexity.</div>', unsafe_allow_html=True)
        elif strength == 'Strong':
            st.success('Your password is strong! Great job!')

        if feedback:
            st.write('### Feedback:')
            for suggestion in feedback:
                st.write(f'- {suggestion}')
    else:
        st.warning('Please enter a password to check.')
