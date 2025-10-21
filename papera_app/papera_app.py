import streamlit as st
import time
from datetime import datetime

# Configurazione pagina
st.set_page_config(
    page_title="Contatore di Papere 🦆",
    page_icon="🦆",
    layout="centered"
)

# CSS personalizzato per colori e animazioni
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FF8C00, #FF6347);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .duck-counter {
        font-size: 5rem;
        font-weight: bold;
        text-align: center;
        color: #FF8C00;
        transition: all 0.3s ease;
    }
    .duck-message {
        font-size: 1.5rem;
        text-align: center;
        margin: 1rem 0;
        color: #666;
    }
    .duck-image {
        border-radius: 50%;
        border: 5px solid #FFD700;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        transition: transform 0.3s ease;
        cursor: pointer;
        display: block;
        margin: 0 auto;
    }
    .duck-image:hover {
        transform: scale(1.05);
    }
    .button-success {
        background: linear-gradient(45deg, #10B981, #059669) !important;
        color: white !important;
        border: none !important;
    }
    .button-danger {
        background: linear-gradient(45deg, #EF4444, #DC2626) !important;
        color: white !important;
        border: none !important;
    }
    .button-warning {
        background: linear-gradient(45deg, #F59E0B, #D97706) !important;
        color: white !important;
        border: none !important;
    }
    .button-quick {
        background: linear-gradient(45deg, #FBBF24, #F59E0B) !important;
        color: white !important;
        border: none !important;
    }
    .toast {
        background: linear-gradient(45deg, #FFD700, #FF8C00);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        text-align: center;
        animation: slideIn 0.5s ease;
    }
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Inizializzazione session state
if 'papera_count' not in st.session_state:
    st.session_state.papera_count = 0
if 'show_quack' not in st.session_state:
    st.session_state.show_quack = False
if 'toasts' not in st.session_state:
    st.session_state.toasts = []

# Funzioni
def aggiungi_papera(num=1):
    st.session_state.papera_count += num
    mostra_toast(f"🦆 {'Papera' if num == 1 else str(num) + ' papere'} aggiunta!")
    
def rimuovi_papera():
    if st.session_state.papera_count > 0:
        st.session_state.papera_count -= 1
        mostra_toast("🦆 Papera rimossa!")
    else:
        mostra_toast("❌ Nessuna papera da rimuovere!", is_error=True)

def reset_contatore():
    st.session_state.papera_count = 0
    mostra_toast("🔄 Reset completato!")

def quack():
    st.session_state.show_quack = True
    mostra_toast("🦆 Quack Quack! La papera ti saluta!")
    # Simula suono con delay
    time.sleep(0.1)

def mostra_toast(messaggio, is_error=False):
    toast_class = "toast-error" if is_error else "toast"
    st.session_state.toasts.append({
        "message": messaggio,
        "time": datetime.now(),
        "is_error": is_error
    })

# Header
st.markdown('<div class="main-header">🦆 Contatore di Papere</div>', unsafe_allow_html=True)

# Papera cliccabile
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("", key="duck_button"):
        quack()
    st.markdown(
        '<img src="https://cdn-icons-png.flaticon.com/512/616/616430.png" class="duck-image" width="150" height="150">',
        unsafe_allow_html=True
    )
    
    if st.session_state.show_quack:
        st.markdown('<div class="duck-message" style="color: #FF8C00; animation: pulse 0.5s;">QUACK! 🦆</div>', unsafe_allow_html=True)
        # Reset dopo 2 secondi
        if time.time() % 10 < 0.1:  # Semplice modo per resettare
            st.session_state.show_quack = False

# Contatore
st.markdown(f'<div class="duck-counter">{st.session_state.papera_count}</div>', unsafe_allow_html=True)

# Messaggio dinamico
if st.session_state.papera_count == 0:
    messaggio = "Nessuna papera ancora!"
elif st.session_state.papera_count == 1:
    messaggio = "Hai una papera!"
else:
    messaggio = f"Hai {st.session_state.papera_count} papere!"
    
st.markdown(f'<div class="duck-message">{messaggio}</div>', unsafe_allow_html=True)

# Pulsanti principali
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Reset", use_container_width=True, type="secondary"):
        reset_contatore()

with col2:
    if st.button("➖ Rimuovi Papera", use_container_width=True, 
                disabled=st.session_state.papera_count == 0,
                type="primary"):
        rimuovi_papera()

with col3:
    if st.button("➕ Aggiungi Papera", use_container_width=True, type="primary"):
        aggiungi_papera()

# Tasti rapidi
st.markdown("### ⚡ Tasti Rapidi")
quick_col1, quick_col2, quick_col3 = st.columns(3)

with quick_col1:
    if st.button("+5 Papere", use_container_width=True):
        aggiungi_papera(5)

with quick_col2:
    if st.button("+10 Papere", use_container_width=True):
        aggiungi_papera(10)

with quick_col3:
    if st.button("+20 Papere", use_container_width=True):
        aggiungi_papera(20)

# Notifiche (Toasts)
if st.session_state.toasts:
    st.markdown("---")
    st.markdown("### 📢 Notifiche")
    
    # Mostra solo gli ultimi 5 toasts
    for toast in list(st.session_state.toasts)[-5:]:
        color = "#EF4444" if toast["is_error"] else "#10B981"
        st.markdown(
            f'<div style="background: {color}; color: white; padding: 0.5rem; border-radius: 5px; margin: 0.2rem 0; text-align: center;">{toast["message"]}</div>',
            unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.markdown("🎨 *Fatto con Streamlit e ❤️ per le papere*")

# Pulsante per pulire notifiche
if st.session_state.toasts:
    if st.button("Pulisci Notifiche"):
        st.session_state.toasts = []
        st.rerun()