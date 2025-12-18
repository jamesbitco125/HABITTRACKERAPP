import streamlit as st

# Custom CSS for styling (Minimalist and Right-Sized Buttons)
st.markdown("""
<style>
    body {
        background: linear-gradient(135deg, #8a4fff 0%, #4f46e5 100%);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    /* Global Button Styles - Minimalist */
    .stButton>button {
        border: none;
        border-radius: 8px;  /* Less rounded for minimalism */
        font-weight: 500;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);  /* Subtle shadow */
        padding: 8px 16px;  /* Smaller padding for right size */
        min-width: 80px;  /* Consistent min width */
        height: 36px;  /* Fixed height for uniformity */
    }
    
    /* Primary Buttons (START, Add New Habit, Check-in, Save) */
    .stButton>button[data-testid*="START"], 
    .stButton>button[data-testid*="add_habit"], 
    .stButton>button[data-testid*="checkin"], 
    .stButton>button[data-testid*="Start Habit"], 
    .stButton>button[data-testid*="Update Habit"] {
        background: #4f46e5;  /* Solid color for minimalism */
        color: white;
    }
    .stButton>button[data-testid*="START"]:hover, 
    .stButton>button[data-testid*="add_habit"]:hover, 
    .stButton>button[data-testid*="checkin"]:hover, 
    .stButton>button[data-testid*="Start Habit"]:hover, 
    .stButton>button[data-testid*="Update Habit"]:hover {
        background: #4338ca;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }
    
    /* Secondary Buttons (Back, Cancel) */
    .stButton>button[data-testid*="←"], 
    .stButton>button[data-testid*="Cancel"] {
        background: #f3f4f6;
        color: #374151;
    }
    .stButton>button[data-testid*="←"]:hover, 
    .stButton>button[data-testid*="Cancel"]:hover {
        background: #e5e7eb;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Edit Button */
    .stButton>button[data-testid*="edit"] {
        background: #3b82f6;
        color: white;
    }
    .stButton>button[data-testid*="edit"]:hover {
        background: #2563eb;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    
    /* Delete Button */
    .stButton>button[data-testid*="delete"] {
        background: #ef4444;
        color: white;
    }
    .stButton>button[data-testid*="delete"]:hover {
        background: #dc2626;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
    }
    
    /* Disabled Buttons */
    .stButton>button:disabled {
        background: #d1d5db !important;
        color: #9ca3af !important;
        cursor: not-allowed;
        box-shadow: none !important;
        transform: none !important;
    }
    
    .habit-card {
        background: white;
        color: #2d3436;
        padding: 20px;  /* Slightly smaller padding */
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .habit-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }
    .progress-bar-bg {
        background: #edf2f7;
        border-radius: 10px;
        height: 8px;
        margin: 10px 0;
        overflow: hidden;
    }
    .progress-bar-fill {
        background: #4a90e2;
        height: 100%;
        transition: width 0.3s ease;
    }
    .habit-card.done {
        background-color: #f0fff4;
        border: 2px solid #48bb78;
        opacity: 0.9;
    }
    .habit-card.done .progress-bar-fill {
        background: #48bb78;
    }
    .modal-content {
        background: white;
        color: #2d3436;
        padding: 25px;  /* Smaller padding */
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        animation: fadeIn 0.3s ease-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 40px;
        padding-top: 10px;
    }
    .profile-pic {
        width: 40px;
        height: 40px;
        background: white;
        border-radius: 50%;
        border: 2px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .add-habit-pill {
        background: white;
        color: #2d3436;
        border: none;
        padding: 8px 20px;  /* Smaller padding */
        border-radius: 8px;
        font-weight: 500;
        font-size: 0.9rem;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
    }
    .add-habit-pill:hover {
        transform: translateY(-1px);
    }
    .empty-card {
        background: white;
        color: #2d3436;
        padding: 40px 25px;  /* Smaller padding */
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .action-buttons {
        display: flex;
        gap: 8px;
    }
    .celebration {
        text-align: center;
        color: #48bb78;
        font-weight: 600;
        font-size: 1.1rem;
        margin: 10px 0;
    }
    .nav-title {
        text-align: center;
        width: 100%;
        font-size: 1.2rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'habits' not in st.session_state:
    st.session_state.habits = []
if 'current_screen' not in st.session_state:
    st.session_state.current_screen = 'start'
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = False
if 'editing_habit' not in st.session_state:
    st.session_state.editing_habit = None

# Functions
def navigate_to(screen):
    st.session_state.current_screen = screen

def open_modal(habit_id=None):
    st.session_state.show_modal = True
    st.session_state.editing_habit = habit_id

def close_modal():
    st.session_state.show_modal = False
    st.session_state.editing_habit = None

def save_habit(name, limit):
    if st.session_state.editing_habit:
        habit = next(h for h in st.session_state.habits if h['id'] == st.session_state.editing_habit)
        habit['name'] = name
        habit['limit'] = limit
        if habit['current'] > limit:
            habit['current'] = limit
            habit['completed'] = True
        elif habit['current'] == limit:
            habit['completed'] = True
        else:
            habit['completed'] = False
    else:
        new_habit = {
            'id': len(st.session_state.habits) + 1,
            'name': name,
            'limit': limit,
            'current': 0,
            'completed': False
        }
        st.session_state.habits.append(new_habit)
    close_modal()
    st.rerun()

def check_in(habit_id):
    habit = next(h for h in st.session_state.habits if h['id'] == habit_id)
    if habit['current'] < habit['limit']:
        habit['current'] += 1
        if habit['current'] == habit['limit']:
            habit['completed'] = True
            st.balloons()  # Celebration for completing the habit
    st.rerun()

def delete_habit(habit_id):
    st.session_state.habits = [h for h in st.session_state.habits if h['id'] != habit_id]
    st.rerun()

# Start Screen
if st.session_state.current_screen == 'start':
    st.markdown('<h1 style="text-align: center; font-size: clamp(2.5rem, 6vw, 3.5rem); letter-spacing: -0.5px; font-weight: 800; margin-bottom: 15px;">HABIT TRACKER</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.1rem; font-weight: 300; opacity: 0.9; margin-bottom: 40px;">Build habits that change your life</p>', unsafe_allow_html=True)
    if st.button('START'):
        navigate_to('tracker')

# Tracker Screen
elif st.session_state.current_screen == 'tracker':
    # Nav Bar
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button('←'):
            navigate_to('start')
    with col2:
        st.markdown('<span class="nav-title">My Habits</span>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="profile-pic"></div>', unsafe_allow_html=True)

    # Header
    st.markdown('<h1 style="text-align: center;">Track Progress</h1>', unsafe_allow_html=True)
    if st.button('+ Add New Habit', key='add_habit'):
        open_modal()

    # Empty State
    if not st.session_state.habits:
        st.markdown('<div class="empty-card"><div>🌱</div><p>Your journey starts here. Add your first habit!</p></div>', unsafe_allow_html=True)
    else:
        # Habit List
        for habit in st.session_state.habits:
            is_done = habit['completed']
            progress_percent = (habit['current'] / habit['limit']) * 100
            with st.container():
                st.markdown(f'<div class="habit-card {"done" if is_done else ""}">', unsafe_allow_html=True)
                # Habit Header
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f'<h3>{habit["name"]}</h3>', unsafe_allow_html=True)
                with col2:
                    col_edit, col_delete = st.columns(2)
                    with col_edit:
                        if st.button('✏️', key=f'edit_{habit["id"]}'):
                            open_modal(habit['id'])
                    with col_delete:
                        if st.button('×', key=f'delete_{habit["id"]}'):
                            delete_habit(habit['id'])
                # Progress Text
                st.markdown(f'<p>{"<strong>✅ Habit Done!</strong>" if is_done else f"Progress: {habit["current"]} / {habit["limit"]}"}</p>', unsafe_allow_html=True)
                # Celebration for completed habits
                if is_done:
                    st.markdown('<div class="celebration">🎉 Congratulations! Habit Completed! 🎉</div>', unsafe_allow_html=True)
                # Progress Bar
                st.progress(progress_percent / 100)
                # Check-in Button
                if st.button('+ Check-in' if not is_done else 'Goal Reached', disabled=is_done, key=f'checkin_{habit["id"]}'):
                    check_in(habit['id'])
                st.markdown('</div>', unsafe_allow_html=True)

# Modal for Add/Edit
if st.session_state.show_modal:
    with st.form(key='habit_form'):
        st.markdown('<h2>' + ('Edit Habit' if st.session_state.editing_habit else 'New Habit') + '</h2>', unsafe_allow_html=True)
        st.write('What goal are we crushing today?')
        name = st.text_input('Habit Name', value=next((h['name'] for h in st.session_state.habits if h['id'] == st.session_state.editing_habit), ''), placeholder='e.g. Read 10 pages')
        limit = st.number_input('Daily Goal (Target Count)', value=next((h['limit'] for h in st.session_state.habits if h['id'] == st.session_state.editing_habit), 1), min_value=1, placeholder='e.g. 8')
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button('Cancel'):
                close_modal()
        with col2:
            if st.form_submit_button('Update Habit' if st.session_state.editing_habit else 'Start Habit'):
                if name and limit > 0:
                    save_habit(name, limit)
                else:
                    st.error('Please enter a valid name and goal number!')
