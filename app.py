import streamlit as st

st.markdown("""
<style>
    /* Basic Reset and Body Styles */
    body {
        background: #f5f5f5; /* Light background for minimalism */
        color: #333; /* Dark text for contrast */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
    }

    /* Container for overall padding */
    .main {
        padding: 2rem;
        max-width: 1000px;
        margin: auto;
    }

    /* Headings */
    h1, h2, h3 {
        font-weight: 700;
        margin-bottom: 0.5em;
        letter-spacing: -0.02em;
    }

    /* Subtle global styles for text */
    p {
        margin-bottom: 1em;
        font-size: 1rem;
    }

    /* Buttons - Flat, Minimal */
    .stButton>button {
        background: transparent;
        border: none;
        padding: 0.75em 1.5em;
        border-radius: 4px;
        font-weight: 500;
        font-size: 0.95rem;
        cursor: pointer;
        transition: background 0.2s, transform 0.2s;
        color: #4f46e5; /* Primary color for buttons */
    }

    /* Hover effect for buttons */
    .stButton>button:hover {
        background: #e0e0e0;
        transform: translateY(-2px);
    }

    /* Primary Button (start, add, check-in) styles */
    .stButton>button[data-testid*='START'],
    .stButton>button[data-testid*='add_habit'],
    .stButton>button[data-testid*='checkin'],
    .stButton>button[data-testid*='Start Habit'],
    .stButton>button[data-testid*='Update Habit'] {
        background-color: #4f46e5;
        color: white;
        padding: 0.75em 2em;
        border-radius: 6px;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: none;
    }

    /* Hover for primary buttons */
    .stButton>button[data-testid*='START']:hover,
    .stButton>button[data-testid*='add_habit']:hover,
    .stButton>button[data-testid*='checkin']:hover,
    .stButton>button[data-testid*='Start Habit']:hover,
    .stButton>button[data-testid*='Update Habit']:hover {
        background-color: #4338ca;
        box-shadow: none;
        transform: translateY(-1px);
    }

    /* Secondary buttons (Back, Cancel) styles */
    .stButton>button[data-testid*='←'],
    .stButton>button[data-testid*='Cancel'] {
        background: transparent;
        color: #555;
        padding: 0.75em 1.5em;
    }
    .stButton>button[data-testid*='←']:hover,
    .stButton>button[data-testid*='Cancel']:hover {
        background: #e0e0e0;
        border-radius: 4px;
        transform: translateY(-1px);
    }

    /* Edit and Delete buttons (small icons) */
    .stButton>button[data-testid*='edit'] {
        background: transparent;
        color: #4f46e5;
        font-size: 1.2rem;
        padding: 0.2em 0.4em;
    }
    .stButton>button[data-testid*='edit']:hover {
        color: #3b82f6;
    }

    .stButton>button[data-testid*='delete'] {
        background: transparent;
        color: #ef4444;
        font-size: 1.2rem;
        padding: 0.2em 0.4em;
    }
    .stButton>button[data-testid*='delete']:hover {
        color: #dc2626;
    }

    /* Habit Card Style */
    .habit-card {
        background: #fff;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        border: 1px solid #e0e0e0;
        transition: box-shadow 0.2s;
    }
    .habit-card:hover {
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    /* Habit Header */
    .habit-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }

    /* Progress Bar */
    .progress-bar-bg {
        background: #e0e0e0;
        border-radius: 4px;
        height: 8px;
        width: 100%;
        overflow: hidden;
    }

    .progress-bar-fill {
        background: #4f46e5;
        height: 100%;
        width: 0;
        transition: width 0.3s ease;
    }

    /* Completed Habit Card */
    .habit-card.done {
        background-color: #f0fff4;
        border-color: #48bb78;
        opacity: 0.95;
    }
    .habit-card.done .progress-bar-fill {
        background: #48bb78;
    }

    /* Modal Style */
    .modal-content {
        background: #fff;
        padding: 20px;
        border-radius: 12px;
        max-width: 500px;
        margin: auto;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        animation: fadeIn 0.3s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Navigation Bar */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }

    /* Profile Pic Placeholder */
    .profile-pic {
        width: 40px;
        height: 40px;
        background: #ddd;
        border-radius: 50%;
        border: 1px solid #ccc;
    }

    /* Add Habit Button (pill) */
    .add-habit-pill {
        background: #fff;
        color: #4f46e5;
        border: 2px dashed #4f46e5;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s, transform 0.2s;
    }
    .add-habit-pill:hover {
        background: #f0f0f0;
        transform: translateY(-1px);
    }

    /* Empty State Card */
    .empty-card {
        background: #fff;
        border-radius: 12px;
        padding: 40px 20px;
        text-align: center;
        border: 1px solid #e0e0e0;
        font-size: 1.1rem;
        color: #555;
    }

    /* Celebration Text */
    .celebration {
        text-align: center;
        color: #48bb78;
        font-weight: 600;
        font-size: 1.2rem;
        margin: 10px 0;
    }

    /* Page Title */
    .page-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 20px;
        letter-spacing: -0.02em;
    }
</style>
""", unsafe_allow_html=True)
