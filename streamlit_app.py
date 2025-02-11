import streamlit as st
import authlib

st.title("Streamlit OAuth Playground")
if not st.experimental_user.is_logged_in:
    if st.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
else:
    st.html(f"Hello, <span style='color: orange; font-weight: bold;'>{st.experimental_user.name}</span>!")
    if st.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()

st.caption(f"Streamlit version {st.__version__}")
st.caption(f"Authlib version {authlib.__version__}")



xxx='''


di=st.experimental_user.to_dict()
st.write(f"{di=}")

if not st.experimental_user.is_logged_in:
    if st.button("Log in with Google"):
        st.login()
        st.rerun()
    st.stop()

if st.button("Log out"):
    st.logout()
    st.rerun()
st.markdown(f"Welcome! {st.experimental_user.name}")
'''