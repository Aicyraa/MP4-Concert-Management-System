import streamlit as st

class Concert:
    def __init__(self, hours, mins, secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs
        self.attendees = []

    def pushAttendee(self, name):
        if name: self.attendees.append(name)

    def popAttendee(self):
        if self.attendees: self.attendees.pop()

    def peekLastAttendee(self):
        return self.attendees[-1] if self.attendees else None


st.set_page_config(page_title="Concert System")
st.title("Concert Attendance")

if "concert" not in st.session_state:
    st.session_state.concert = None

if st.session_state.concert is None:
    st.subheader("Setup Concert Duration")
    col1, col2, col3 = st.columns(3)
    h = col1.number_input("Hours", 0, 23, 2)
    m = col2.number_input("Minutes", 0, 59, 30)
    s = col3.number_input("Seconds", 0, 59, 0)
    
    if st.button("Initialize"):
        st.session_state.concert = Concert(h, m, s)
        st.rerun()
else:
    c = st.session_state.concert
    st.info(f"Duration: {c.hours}h {c.mins}m {c.secs}s")
    
    name = st.text_input("Attendee Name")
    
    col1, col2, col3 = st.columns(3)
    if col1.button("Push"):
        c.pushAttendee(name)
    if col2.button("Pop"):
        c.popAttendee()
    if col3.button("Peek"):
        last = c.peekLastAttendee()
        st.write(f"Last: {last}" if last else "Empty")

    st.write("### Attendees")
    st.write(list(reversed(c.attendees)))
    
    if st.sidebar.button("Reset Session"):
        st.session_state.concert = None
        st.rerun()