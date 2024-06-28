import streamlit as st

################# APP SETUP #################

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
home_page = st.Page("frontend/home.py", title="Home", icon=":material/home:", default=True)
quantum_portfolio_optimization = st.Page("frontend/portfolio_optimization/quantum_portfolio_optimization.py", title="Quantum Portfolio Optimization", icon=":material/dashboard:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Home": [home_page],
            "Account": [logout_page],
            "Portfolio Optimization": [quantum_portfolio_optimization],
        }
    )
else:
    pg = st.navigation({
        "Home": [home_page],
        "Account": [login_page],
    })

pg.run()
